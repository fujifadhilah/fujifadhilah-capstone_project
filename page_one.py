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

# 1. membuat line chart pendapatan dan pengeluaran
st.header("Tren Rata-rata Pendapatan dan Rata-rata Pengeluaran Pekerja Informal")

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


# Create dictionary baru bernama data 
# Variabel province berisi key province_year, variabel income berisi selectedIncomes, variabel outcome berisi selectedOutcomes
# Ketiga variabel tersebut sudah difilter berdasarkan pendapatan < pengeluaran
data = {
    "province": incomeUnderOutcomes,
    "income": selectedIncomes,
    "outcome": selectedOutcomes
}

# Create dataframe/table dari dictionary data
source = pd.DataFrame(data)

# Join kolom incomes dan kolom outcomes menjadi satu group kolom bernama lineChartValues
lineChartGroupProvinces = []
lineChartGroupYears = []
lineChartCategories = []
lineChartValues = []
# set row data income
i = 0 
for i in range(len(selectedProvince)):
    lineChartGroupProvinces.append(selectedProvince[i])
    lineChartGroupYears.append(selectedYear[i])
    lineChartCategories.append("income")
    lineChartValues.append(selectedIncomes[i])
        
    i+=1

# set row data outcome
i = 0
for i in range(len(selectedProvince)):
    lineChartGroupProvinces.append(selectedProvince[i])
    lineChartGroupYears.append(selectedYear[i])
    lineChartCategories.append("outcome")
    lineChartValues.append(selectedOutcomes[i])      
        
    i+=1


# Create dataframe 
dfLineChart = pd.DataFrame({
    "provinces": lineChartGroupProvinces,
    "years": lineChartGroupYears,
    "categories": lineChartCategories,
    "values": lineChartValues
})

# Create plot with plotly
fig = px.line(dfLineChart, x="years", y="values", color='categories', facet_col="provinces", facet_col_spacing=0.12, markers=True)
# Update Line & Markers
fig.update_traces(line=dict(width=3),marker=dict(size=8))
# Show plot
st.plotly_chart(fig, theme="streamlit", use_container_width=False)

st.markdown("""
Pekerja informal yang akan dibahas meiliputi pekerja bebas dan pekerja berusaha sendiri. 

1. Definisi pekerja bebas adalah pekerja yang tidak memiliki majikan tetap (lebih dari 1 majikan dalam sebulan terakhir, khusus pada sektor bangunan biasanya tiga bulan). Contoh: pekerja di bidang jasa pertanian, perkebunan, perikanan, bangunan, dll.
2. Definisi pekerja berusaha sendiri adalah bekerja atau berusaha dengan menanggung resiko sendiri, serta tidak menggunakan pekerja dibayar maupun pekerja tak dibayar, termasuk yang sifat pekerjaannya memerlukan teknologi atau keahlian khusus. Contoh: pedagang kecil di pasar tradisional, pemilik warung makan kecil, petani, penjahit lepas, pengemudi ojek online dll.

<p style='text-align: justify; text-indent: 40px;'>Berdasarkan data BPS, terdapat perbandingan yang signifikan antara rata-rata pendapatan bersih dan pengeluaran per kapita setiap bulan bagi pekerja informal di daerah perkotaan dan pedesaan menurut provinsi dari tahun 2019 hingga 2023. Hanya pada tahun 2019, dari total 34 provinsi di Indonesia, situasi tergolong aman karena rata-rata pengeluaran lebih rendah daripada pendapatan.</p>

<p style='text-align: justify; text-indent: 40px;'>Kesenjangan mulai dirasakan pada tahun 2020, sebagai dampak dari pandemi COVID-19 yang berkelanjutan hingga tahun 2023. Dalam periode tersebut, terdapat empat provinsi di Indonesia di mana pengeluaran melebihi pendapatan, yaitu DI Yogyakarta, Bali, DKI Jakarta, dan Nusa Tenggara Barat.</p>

<p style='text-align: justify; text-indent: 40px;'>Rata-rata pengeluaran pekerja informal di DI Yogyakarta telah melebihi rata-rata pendapatannya sepanjang tahun 2020 hingga 2023. Pada tahun 2020, rata-rata pengeluaran per kapita sebulan adalah Rp1.411.972, sedangkan rata-rata pendapatannya adalah Rp1.217.474. Persentase selisih antara pendapatan dan pengeluaran sebesar 15.97%. Pada tahun 2021, rata-rata pengeluaran meningkat menjadi Rp1.417.870, sementara rata-rata pendapatan turun menjadi Rp1.135.371, dengan persentase selisih sebesar 24.88%. Pada tahun 2022, rata-rata pengeluaran meningkat lagi menjadi Rp1.480.374, sementara rata-rata pendapatan meningkat menjadi Rp1.323.700, dengan persentase selisih sebesar 11.84%. Di tahun 2023, rata-rata pengeluaran mencapai Rp1.731.560, sementara rata-rata pendapatan hanya Rp1.348.833, dengan persentase selisih sebesar 28.37%.</p>
            Insight: 

1. Provinsi DI Yogyakarta di antara 34 provinsi di Indonesia pada periode tahun 2020 hingga 2023, menunjukkan kesenjangan terbesar bagi pekerja informal. Ini disebabkan oleh peningkatan terus-menerus dalam jumlah pengeluaran, sementara pendapatan cenderung fluktuatif.
2. Persentase selisih antara pendapatan dan pengeluaran tergolong besar hingga mencapai 28.37% dari pendapatan pada tahun 2023.
3. Perekonomian pekerja informal di DI Yogyakarta masih belum membaik.


<p style='text-align: justify; text-indent: 40px;'>Rata-rata pengeluaran pekerja informal di Bali melebihi rata-rata pendapatannya pada tahun 2020 hingga 2021. Pada tahun 2020, rata-rata pengeluaran per kapita sebulan adalah Rp1.509.666, sementara rata-rata pendapatannya adalah Rp1.481.653. Persentase selisih antara pendapatan dan pengeluaran sebesar 1.89%. Di tahun 2021, rata-rata pengeluaran turun menjadi Rp1.468.624, sementara rata-rata pendapatannya juga turun menjadi Rp1.264.271, dengan persentase selisih sebesar 16.16%.</p>
            Insight:

1. Kesenjangan di Bali pada tahun 2020 tidak terlalu terlihat, hanya sebesar 1.89% saja.
2. Bali mengalami penurunan secara ekonomi bagi pekerja informal pada tahun 2021.
3. Meskipun mengalami penurunan, dari tahun 2022 hingga 2023 Bali tidak mengalami kesenjangan. Hal ini mencerminkan peningkatan tingkat kesejahteraan yang dinikmati oleh pekerja informal di Bali sebagai hasil perbaikan ekonomi yang terjadi.


<p style='text-align: justify; text-indent: 40px;'>Rata-rata pengeluaran pekerja informal di DKI Jakarta melebihi rata-rata pendapatannya pada tahun 2021 dan 2023. Pada tahun 2021, rata-rata pengeluaran per kapita sebulan adalah Rp2.336.429, sedangkan rata-rata pendapatannya adalah Rp2.202.002, dengan persentase selisih sebesar 6.10%. Pada tahun 2023, rata-rata pengeluaran meningkat menjadi Rp2.791.716, sementara rata-rata pendapatannya adalah Rp2.340.000, dengan persentase selisih sebesar 19.30%.</p>
            Insight:

1. DKI Jakarta menonjol sebagai provinsi dengan tingkat pengeluaran dan pendapatan tertinggi dibandingkan provinsi lainnya. 
2. Kesenjangan meningkat dari 6.10% pada tahun 2021 menjadi 19.30% pada tahun 2023, menunjukkan penurunan perekonomian pekerja informal di DKI Jakarta.


<p style='text-align: justify; text-indent: 40px;'>Rata-rata pengeluaran pekerja informal di Nusa Tenggara Barat melebihi rata-rata pendapatannya pada tahun 2021 dan 2023. Pada tahun 2021, rata-rata pengeluaran per kapita sebulan adalah Rp1.197.548, sedangkan rata-rata pendapatannya adalah Rp1.065.663, dengan persentase selisih sebesar 12.37%. Pada tahun 2023, rata-rata pengeluaran meningkat menjadi Rp1.260.820, sementara rata-rata pendapatannya adalah Rp1.216.067, dengan persentase selisih sebesar 3.68%.</p>      
            Insight:

1. Kesenjangan terjadi di Nusa Tenggara Barat pada tahun 2021 dan 2023. Namun, perekonomian pekerja informal di sana telah menunjukkan tanda-tanda perbaikan karena persentase selisih telah menurun secara signifikan dari 12.37% menjadi 3.68%.
 """, unsafe_allow_html=True)
