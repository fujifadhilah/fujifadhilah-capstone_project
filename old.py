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

# 2. Membuat bar_chart perbandingan antara jumlah pengeluaran untuk makanan dan non makanan

# Create dictionary dengan mengambil kolom food_outcome, not_food_outcome 
foodOutcome = df["food_outcome"]
foodOutcomeDictionary = dict(zip(keys, foodOutcome))
notFoodOutcome = df["not_food_outcome"]
notFoodOutcomeDictionary = dict(zip(keys, notFoodOutcome))

# Assign foodOutcomes dan notFoodOutcomes kedalam selectedFoodOutcomes dan selectedNotFoodOutcomes dengan filter pendapatan < pengeluaran
selectedFoodOutcomes = []
selectedNotFoodOutcomes = []
for key in incomeUnderOutcomes:
    selectedFoodOutcomes.append(foodOutcomeDictionary[key])
    selectedNotFoodOutcomes.append(notFoodOutcomeDictionary[key])


# Create new dataframe yang berisi kolom-kolom yang sudah difilter sebelumnya
sourceBarChart = pd.DataFrame({
    "province": selectedProvince,
    "year": selectedYear,
    "food_outcome": selectedFoodOutcomes,
    "not_food_outcome": selectedNotFoodOutcomes
})


# Create plot
st.header("Rata-rata Total Pengeluaran Berdasarkan Jenis Pengeluaran")
# 'year:N' karena grafik akan dikategorikan berdasarkan tahun. Q -> numerik, N -> Kategorik
bar_chart = alt.Chart(sourceBarChart).mark_bar(size=18).encode(
    x='Pengeluaran (Rp):Q', 
    y='year:N',
    color='type:N'
).transform_fold(
    as_=['type', 'Pengeluaran (Rp)'],
    fold=['food_outcome', 'not_food_outcome']
)

# Show plot
st.altair_chart(bar_chart, theme="streamlit", use_container_width=False)
st.markdown("""
 <p style='text-align: justify; text-indent: 40px;'>Insight: Pengeluaran pekerja informal untuk kebutuhan non-makanan lebih besar daripada pengeluaran untuk makanan, sekitar dua kali lipat lebih banyak. Contoh pengeluaran non-makanan meliputi fasilitas rumah tangga, perumahan, barang tahan lama, kesehatan, pendidikan, pakaian, keperluan kenduri, dan sebagainya.</p>
""", unsafe_allow_html=True)



