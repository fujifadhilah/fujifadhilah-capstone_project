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
    

# 4. Membuat grouped_bar_chart untuk membandingan pendapatan pekerja informal vs UMP
# Assign incomeUnderOutcomes kedalam selectedIncomes
selectedIncomes = []
for key in incomeUnderOutcomes:
    selectedIncomes.append(incomeDictionary[key])

# Add kolom UMP menggunakan list 
selectedUMP = [1704608, 2493523, 4416186, 1765000, 2493523, 2183883, 1840916, 4900798, 1981782, 2371407]
# Create list dengan mengelompokkan provinsi, tahun, kategori pendapatan, nilai pendapatan
groupProvinces = []
groupYears = []
incomeCategories = []
incomeValues = []
for i in range(len(selectedProvince)):
    for j in range(2):
        groupProvinces.append(selectedProvince[i])
        groupYears.append(selectedYear[i])
        if (j == 0):
            incomeCategories.append("Income_Informal")
            incomeValues.append(selectedIncomes[i])
        elif (j == 1):
            incomeCategories.append("UMP")
            incomeValues.append(selectedUMP[i])
        
    i+=1

# Create dictionary dari list diatas
dataGroupBarChart = {
    "province": groupProvinces,
    "year": groupYears,
    "income_category": incomeCategories,
    "income_values": incomeValues
}

st.header("Rata-rata Pendapatan Pekerja Informal vs UMP")

# Create dataframe
sourceGroupBarChart = pd.DataFrame(dataGroupBarChart)
# Create plot
fig2 = px.bar(sourceGroupBarChart, x="province", y="income_values", color="income_category", facet_col="year", facet_col_spacing=0.12, barmode="group", width=1200, height=400)
st.plotly_chart(fig2, theme="streamlit", use_container_width= False)

st.markdown("""
Insight:
1. Perbandingan pendapatan pekerja informal dengan Upah Minimum Provinsi (UMP) DI Yogyakarta tidak terlalu jauh berbeda, dengan rata-rata selisih sebesar Rp566.732 per kapita sebulan. Kemungkinan buruh yang mendapatkan UMP DI Yogyakarta juga mengalami kesenjangan pendapatan yang serupa dengan pekerja informal.
2. Perbandingan pendapatan pekerja informal dengan UMP Bali cukup signifikan, dengan gaji buruh hampir 2 kali lipat lebih tinggi dari pendapatan pekerja informal. Rata-rata selisihnya adalah Rp1.120.561 per kapita sebulan. Ini menunjukkan perbedaan pendapatan yang cukup nyata antara pekerja informal dan buruh di Bali.
3. Perbandingan pendapatan pekerja informal dengan UMP DKI Jakarta sangat signifikan, dengan gaji buruh 2 kali lipat lebih tinggi dari pendapatan pekerja informal. Rata-rata selisihnya mencapai Rp2.387.491 per kapita sebulan. Hal ini mencerminkan perbedaan pendapatan yang sangat nyata antara pekerja informal dan buruh di DKI Jakarta.
4. Perbandingan pendapatan pekerja informal dengan UMP Nusa Tenggara Barat juga cukup signifikan, dengan gaji buruh hampir 2 kali lipat lebih tinggi dari pendapatan pekerja informal. Rata-rata selisihnya adalah Rp1.136.780 per kapita sebulan. Ini menunjukkan perbedaan pendapatan yang cukup nyata antara pekerja informal dan buruh di Nusa Tenggara Barat.
""")