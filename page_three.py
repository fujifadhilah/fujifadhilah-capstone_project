# Import library data manipulasi dan visualisasi
import streamlit as st
import pandas as pd
import altair as alt
import plotly.graph_objects as go
import plotly.express as px

# Mengatur tampilan tata letak halaman menjadi lebar
st.set_page_config(layout='wide')

# Membaca file csv
df = pd.read_csv('income_outcome.csv')

# Menggabungkan kolom province_tahun untuk dijadikan sebagai PK, karena semua kolom di file income_outcome tidak ada yang unik
provinces = df["province"]
years = df["year"]
keys = []
i = 0
for province in provinces:
    dataKey = province + "_" + str(years[i])
    keys.append(dataKey)
    i+=1

# Mengambil kolom income, kemudian dijadikan dictionary dengan variabel incomes sebagai value dengan key berupa keys
incomes = df["income"]
incomeDictionary = dict(zip(keys, incomes))
# Mengambil kolom outcome, kemudian dijadikan dictionary dengan variabel outcomes sebagai value dengan key berupa keys
outcomes = df["outcome"]
outcomeDictionary = dict(zip(keys, outcomes))


# Create variabel incomeUnderOutcomes yang berisi keys dengan syarat pendapatan < pengeluaran 
incomeUnderOutcomes = []
for key, value in incomeDictionary.items() :
    if value < outcomeDictionary[key]:
        incomeUnderOutcomes.append(key)

# Ambil values dari key incomeUnderOutcomes. Assign ke variabel selectedIncomes dan selectedOutcomes
selectedIncomes = []
selectedOutcomes = []
for key in incomeUnderOutcomes:
    selectedIncomes.append(incomeDictionary[key])
    selectedOutcomes.append(outcomeDictionary[key])


# Memecah key incomeUnderOutcomes yang berisi "province_year" dengan pemisah "_" 
# Terbuat array dengan 2 data yaitu index-0 yang berisi province dan index-1 yang berisi year
# Pemisah "_" nya dihilangkan
# Assign province kedalam variabel selectedProvince dan year kedalam variabel selectedYear
selectedYear = []
selectedProvince = []
for key in incomeUnderOutcomes:
    splittedKey = key.split("_") 
    selectedProvince.append(splittedKey[0])
    selectedYear.append(splittedKey[1])


# 3. Membuat donut_chart untuk mengetahui komposisi pendapatan di masing-masing sektor pekerjaan
# Create dictionary yang berisikan {"provinsi_tahun" : agricultural_income} dari df
agriculturalIncome = df["agricultural_income"]
agriculturalIncomeDictionary = dict(zip(keys, agriculturalIncome))

# Create dictionary yang berisikan {"provinsi_tahun" : industry_income} dari df
industryIncome = df["industry_income"]
industryIncomeDictionary = dict(zip(keys, industryIncome))

# Create dictionary yang berisikan {"provinsi_tahun" : services_income} dari df
servicesIncome = df["services_income"]
servicesIncomeDictionary = dict(zip(keys, servicesIncome))

# Looping untuk mengambil {'key':value} dengan filter pendapatan < pengeluaran 
selectedAgriculturalIncome = []
selectedIndustryIncome = []
selectedServicesIncome = []
for key in incomeUnderOutcomes:
    selectedAgriculturalIncome.append(agriculturalIncomeDictionary[key])
    selectedIndustryIncome.append(industryIncomeDictionary[key])
    selectedServicesIncome.append(servicesIncomeDictionary[key])

# Hitung rata-rata dari tiap sektor pekerjaan
dataMeanDonutChart = {
    "agricultural_income": sum(selectedAgriculturalIncome) / len(selectedAgriculturalIncome),
    "industry_income": sum(selectedIndustryIncome) / len(selectedIndustryIncome),
    "services_income": sum(selectedServicesIncome) / len(selectedServicesIncome)
}

# Create new list untuk dilakukan visualisasi
donutChartLabels = ["agricultural_income", "industry_income", "services_income"]
donutChartValues = [dataMeanDonutChart["agricultural_income"], dataMeanDonutChart["industry_income"], dataMeanDonutChart["services_income"]]

st.header("Komposisi Rata-rata Pendapatan tiap Sektor Pekerjaan")
# Create plot
fig_donut = go.Figure(data=[go.Pie(labels=donutChartLabels, values=donutChartValues, hole=0.5)])
# Update traces
fig_donut.update_traces(textposition="inside", textfont=dict(color="white", size=13),textinfo="percent", pull=[0.1,0,0], rotation=-115)
# Add Annotation
fig_donut.add_annotation(text="<b>Informal Worker Sectors</b>",showarrow=False, font=dict(size=10))
# Show plot
st.plotly_chart(fig_donut, theme="streamlit", use_container_width=False)

st.markdown("""
Lapangan usaha berdasarkan Klasifikasi Baku Lapangan Usaha Indonesia (KBLI) 2015 dikelompokkan ke dalam 3 kelompok besar, yaitu:
1. Pertanian terdiri atas sektor pertanian, perkebunan, kehutanan, perburuan, dan perikanan.
2. Insdustri terdiri atas sektor pertambangan, penggalian, industri pengolahan, listrik, gas, air, bangunan.
3. Jasa terdiri atas sektor perdagangan besar, eceran, rumah makan, angkutan, keuangan, usaha persewaan bangunan atau tanah, jasa kemasyarakatan, sosial, perorangan.
 
<p style='text-align: justify; text-indent: 40px;'>Insight: 
Pendapatan pekerja informal dari sektor pertanian cenderung lebih rendah dibandingkan dengan sektor-sektor lainnya.</p>
""", unsafe_allow_html=True)


