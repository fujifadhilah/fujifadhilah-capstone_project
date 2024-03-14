# Import library data manipulasi dan visualisasi
import streamlit as st
import pandas as pd
import altair as alt
import plotly.graph_objects as go
import plotly.express as px

# Mengatur tampilan tata letak halaman menjadi lebar
st.set_page_config(layout='wide')

st.header("Rata-rata Pendapatan Informal vs UMP")

# Membaca file csv
df = pd.read_csv('income_outcome.csv')
ump_source = pd.read_csv("income_ump.csv")

# Menggabungkan kolom province_tahun untuk dijadikan sebagai PK, karena semua kolom di file income_outcome tidak ada yang unik
provinces = df["province"]
years = df["year"]
keys = []
i = 0
for province in provinces:
    dataKey = province + "_" + str(years[i])
    keys.append(dataKey)
    i+=1

selectedUMP = ump_source["ump"]

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
# Assign year kedalam variabel selectedYear
selectedProvince = []
for key in incomeUnderOutcomes:
    splittedKey = key.split("_") 
    selectedProvince.append(splittedKey[0])
    
selectedProvinceSet = set(selectedProvince)

for province in selectedProvinceSet:
    st.subheader(province)
    dataset = df.loc[(df['province'] == province) & (df['income'] < df['outcome'])]
    umpDataset = ump_source.loc[ump_source['province'] == province]
    years = dataset['year'].tolist()
    incomes = dataset['income'].tolist()
    yearData = []
    categoryData = []
    valueData = []
    i = 0
    for i in range(len(years)):
        year = years[i]
        ump = umpDataset.loc[umpDataset['year'] == year]
        umpList = ump['ump'].tolist()
        j = 0
        for j in range(2):
            yearData.append(year)
            if j == 0:
                categoryData.append("informal income")
                valueData.append(incomes[i])
            if j == 1:
                categoryData.append("ump")
                valueData.append(umpList[0])
            j+=1

    sourceBarChart = pd.DataFrame({
        "year": yearData,
        "category": categoryData,
        "value": valueData
    })

    bar_chart = alt.Chart(sourceBarChart).mark_bar(size=20).encode(
        alt.X('year:N', sort=alt.EncodingSortField(field="year", order='ascending'), axis=alt.Axis(labelAngle=0)),
        y='value:Q',
        xOffset="category:N",
        color='category:N'
    )
    

    st.altair_chart(bar_chart, theme="streamlit", use_container_width=False)
st.markdown("""
1. Perbandingan **rata-rata pendapatan pekerja informal** dengan **UMP Bali** cukup signifikan, dengan gaji buruh hampir 2 kali lipat lebih tinggi dari pendapatan pekerja informal. Rata-rata selisihnya adalah **Rp1.120.561** per kapita sebulan. Ini menunjukkan perbedaan pendapatan yang cukup nyata antara pekerja informal dan buruh di Bali.
2. Perbandingan **rata-rata pendapatan pekerja informal** dengan **UMP DI Yogyakarta** tidak terlalu jauh berbeda, dengan rata-rata selisih sebesar **Rp566.732** per kapita sebulan. Kemungkinan buruh yang mendapatkan upah sebesar UMP DI Yogyakarta juga mengalami defisit pendapatan yang serupa dengan pekerja informal, namun harus dilakukan analisa lanjutan.
3. Perbandingan **rata-rata pendapatan pekerja informal** dengan **UMP DKI Jakarta** sangat signifikan, dengan gaji buruh 2 kali lipat lebih tinggi dari pendapatan pekerja informal. Rata-rata selisihnya mencapai **Rp2.387.491** per kapita sebulan. Hal ini mencerminkan perbedaan pendapatan yang sangat nyata antara pekerja informal dan buruh di DKI Jakarta.
4. Perbandingan **rata-rata pendapatan pekerja informal** dengan **UMP Nusa Tenggara Barat** juga cukup signifikan, dengan gaji buruh hampir 2 kali lipat lebih tinggi dari pendapatan pekerja informal. Rata-rata selisihnya adalah **Rp1.136.780** per kapita sebulan. Ini menunjukkan perbedaan pendapatan yang cukup nyata antara pekerja informal dan buruh di Nusa Tenggara Barat.
""")