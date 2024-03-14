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

# Memecah key incomeUnderOutcomes yang berisi "province_year" dengan pemisah "_" 
# Terbuat array dengan 2 data yaitu index-0 yang berisi province dan index-1 yang berisi year
# Pemisah "_" nya dihilangkan
# Assign province kedalam variabel selectedProvince
selectedProvince = []
for key in incomeUnderOutcomes:
    splittedKey = key.split("_") 
    selectedProvince.append(splittedKey[0])

# Create plot
st.header("Rata-rata Total Pengeluaran Berdasarkan Jenis Pengeluaran")
selectedProvinceSet = set(selectedProvince)

for province in selectedProvinceSet:
    st.subheader(province)
    dataset = df.loc[(df['province'] == province) & (df['income'] < df['outcome'])]

    # altair bar chart
    sourceBarChart = pd.DataFrame({
        "year": dataset['year'],
        "food_outcome": dataset['food_outcome'],
        "not_food_outcome": dataset['not_food_outcome']
    })

    bar_chart = alt.Chart(sourceBarChart).mark_bar(size=18).encode(
        alt.Y('year:N', sort=alt.EncodingSortField(field="year", order='descending')),
        x='Outcome (Rp):Q',
        color='type:N'
    ).transform_fold(
        as_=['type', 'Outcome (Rp)'],
        fold=['food_outcome', 'not_food_outcome']
    )

    # Show plot
    st.altair_chart(bar_chart, theme="streamlit", use_container_width=False)

# Show plot
st.markdown("""
**Dari provinsi yang mengalami defisit pendapatan**, pengeluaran untuk kebutuhan **non-makanan lebih besar daripada pengeluaran untuk makanan**, sekitar **dua kali lipat lebih banyak**. Contoh pengeluaran non-makanan meliputi fasilitas rumah tangga, perumahan, barang tahan lama, kesehatan, pendidikan, pakaian, keperluan kenduri, dan sebagainya.
""", unsafe_allow_html=True)