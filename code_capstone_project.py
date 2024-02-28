# Import library data manipulasi dan visualisasi
import streamlit as st
import pandas as pd
import altair as alt
import plotly.graph_objects as go
import plotly.express as px

# Mengatur tampilan tata letak halaman menjadi lebar
st.set_page_config(layout='wide')

# Judul dashboard
st.markdown("<h1 style='text-align: center; color: black; margin-bottom: 100px;}'>Dilema Pekerja Informal dalam Mengatasi Kesenjangan Pendapatan</h1>", unsafe_allow_html=True)
# Sub-judul
st.header("Problem Statement")
st.markdown("""<p style='text-align: justify; text-indent: 40px;'>Dalam arti sesungguhnya, tujuan orang bekerja adalah untuk memperoleh penghasilan guna memenuhi kebutuhan hidup, baik itu kebutuhan pangan maupun kebutuhan lainnya. Kebijakan pengaturan upah di Indonesia, yaitu melalui Upah Minimum Provinsi (UMP), namun hanya berlaku untuk buruh/karyawan/pegawai. Dalam kenyataan, pekerja yang hanya mendapatkan upah sebesar UMP saja sering mengalami kesulitan, apalagi bagi mereka yang bekerja sebagai non-buruh.
Pada Agustus 2023, terdapat kenyataan bahwa jumlah pekerja informal atau pekerja non-buruh mendominasi dengan mencapai 59,11% di Indonesia. </p>

<p style='text-align: justify; text-indent: 40px;'>Pekerja informal seringkali menghadapi berbagai tantangan dan dilema. Bagi mereka, pendapatan hanya diperoleh saat mereka bekerja, sehingga ketidakhadiran karena izin, sakit, atau alasan lainnya berarti kehilangan pendapatan. Karakteristik pekerjaan informal sering tidak menentu dan tidak stabil, menyulitkan perencanaan keuangan. Hal ini dapat mengakibatkan terjadinya kesenjangan yang lebih besar antara pendapatan dan pengeluaran.
Pekerja informal juga menghadapi pendapatan dari pekerjaan yang tidak tetap seiring dengan biaya hidup yang semakin meningkat. Kurangnya akses ke layanan keuangan formal seperti kredit atau pinjaman bank membuat pekerja informal terjebak dalam lingkaran kemiskinan, karena sulit bagi mereka untuk mendapatkan modal untuk meningkatkan atau memperluas usaha mereka.</p>

<p style='text-align: justify; text-indent: 40px;'>Lantas, Bagaimana jika pengeluaran mereka melebihi pendapatannya? Apa kebijakan yang sebaiknya diterapkan oleh pemerintah untuk mengatasi situasi tersebut? Dan tindakan apa yang harus diambil oleh pekerja informal untuk mengatasi ketidakseimbangan tersebut?</p> 
""", unsafe_allow_html=True)

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
st.header("Tren Rata-rata Pendapatan dan Rata-rata Pengeluaran")

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
    color='type:N',
    row=alt.Row('province', spacing=50)
).transform_fold(
    as_=['type', 'Pengeluaran (Rp)'],
    fold=['food_outcome', 'not_food_outcome']
)

# Show plot
st.altair_chart(bar_chart, theme="streamlit", use_container_width=False)
st.markdown("""
 <p style='text-align: justify; text-indent: 40px;'>Insight: Pengeluaran pekerja informal untuk kebutuhan non-makanan lebih besar daripada pengeluaran untuk makanan, sekitar dua kali lipat lebih banyak. Contoh pengeluaran non-makanan meliputi fasilitas rumah tangga, perumahan, barang tahan lama, kesehatan, pendidikan, pakaian, keperluan kenduri, dan sebagainya.</p>
""", unsafe_allow_html=True)



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

st.header("Kesimpulan")
st.markdown("""
1. Provinsi DI Yogyakarta menunjukkan kesenjangan pendapatan yang signifikan pada tahun 2020 hingga 2023 bagi pekerja informal, dengan tingkat pengeluaran yang terus meningkat dan pendapatan yang fluktuatif.
2. Bali mengalami penurunan ekonomi pada tahun 2021 bagi pekerja informal, tetapi tidak mengalami kesenjangan pada tahun 2022-2023, menandakan adanya perbaikan ekonomi.
3. DKI Jakarta memiliki tingkat pengeluaran dan pendapatan tertinggi, tetapi juga mengalami peningkatan kesenjangan yang mengindikasikan penurunan ekonomi pekerja informal.
4. Di Nusa Tenggara Barat, terjadi kesenjangan pendapatan pada tahun 2021 dan 2023, tetapi adanya penurunan signifikan pada tahun 2023 menunjukkan perbaikan ekonomi.
5. Pengeluaran pekerja informal untuk kebutuhan non-makanan lebih besar daripada pengeluaran untuk makanan, sekitar dua kali lipat lebih banyak.
6. Pendapatan pekerja informal dari sektor pertanian cenderung lebih rendah dibandingkan dengan sektor-sektor lainnya.
7. Di Yogyakarta, kesenjangan pendapatan antara pekerja informal dan buruh yang mendapatkan UMP tidak terlalu besar. 
8. Di Bali, DKI Jakarta, dan Nusa Tenggara Barat, perbandingan pendapatan pekerja informal dengan UMP menunjukkan kesenjangan yang cukup besar, mencerminkan ketidaksetaraan pendapatan antara pekerja informal dan buruh formal.
""")


st.header("Saran")
st.markdown("""
<p style='text-align: justify; text-indent: 40px;'>Pemerintah Indonesia khususnya provinsi DI Yogyakarta, Bali, DKI Jakarta, Nusa
Tenggara Barat perlu memperhatikan upaya untuk meningkatkan pendapatan pekerja
informal terutama di sektor pertanian. Pemerintah juga perlu melakukan analisis
mendalam untuk memahami penyebab pengeluaran yang melebihi pendapatan bagi
pekerja informal. Program-program pelatihan dan pengembangan keterampilan dapat
membantu pekerja informal meningkatkan kualifikasi mereka dan meningkatkan
pendapatan mereka. Perlunya pemantauan dan evaluasi yang berkelanjutan terhadap
implementasi kebijakan ekonomi yang memengaruhi kondisi pekerja informal.</p>
            
Pekerja informal dapat mengurangi pengeluaran, terutama pada kategori nonmakanan, karena jenis pengeluaran ini menyumbang sebagian besar alokasi pengeluaran
mereka.
            
Diperlukan keterlibatan dari berbagai pihak untuk memastikan bahwa pekerja
informal mendapatkan hak-haknya dan untuk meningkatkan peluang mereka menjadi
pekerja tetap.
""", unsafe_allow_html=True)


st.header("Sumber Data")
st.markdown("""
1. https://www.bps.go.id/id/statistics-table/3/VVhCTlptdExibkpyV25WM2NFNWFXa3czVDFvdmR6MDkjMw==/rata-rata-pendapatan-bersih-sebulan-pekerja-informal-sup-1-sup-menurut-provinsi-dan-lapangan-pekerjaan-utama-rupiah-.html?year=2019
2. https://www.bps.go.id/id/statistics-table/3/VVhCTlptdExibkpyV25WM2NFNWFXa3czVDFvdmR6MDkjMw==/rata-rata-pendapatan-bersih-sebulan-pekerja-informal-sup-1-sup-menurut-provinsi-dan-lapangan-pekerjaan-utama-rupiah-.html?year=2020
3. https://www.bps.go.id/id/statistics-table/3/VVhCTlptdExibkpyV25WM2NFNWFXa3czVDFvdmR6MDkjMw==/rata-rata-pendapatan-bersih-sebulan-pekerja-informal-sup-1-sup-menurut-provinsi-dan-lapangan-pekerjaan-utama-rupiah-.html?year=2021
4. https://www.bps.go.id/id/statistics-table/3/VVhCTlptdExibkpyV25WM2NFNWFXa3czVDFvdmR6MDkjMw==/rata-rata-pendapatan-bersih-sebulan-pekerja-informal-sup-1-sup-menurut-provinsi-dan-lapangan-pekerjaan-utama-rupiah-.html?year=2022
5. https://www.bps.go.id/id/statistics-table/1/MjE5NyMx/rata-rata-pendapatan-bersih-pekerja-bebas-menurut-provinsi-dan-lapangan-pekerjaan-utama-2023.html
6. https://www.bps.go.id/id/statistics-table/1/OTQ1IzE=/rata-rata-pengeluaran-per-kapita-sebulan-untuk-makanan-dan-bukan-makanan-di-daerah-perkotaan-dan-perdesaan-menurut-provinsi-rupiah-2011-2023.html
7. https://www.kompas.id/baca/ekonomi/2023/12/28/tetap-bisa-bekerja-di-tengah-perekonomian-dan-kebijakan-perburuhan-yang-menantang
8. https://yogyakarta.bps.go.id/indicator/6/272/2/upah-minimum-kabupaten-upah-minimum-provinsi-di-di-yogyakarta.html
9. https://bali.bps.go.id/indicator/13/61/2/upah-minimum-kabupaten-kota-di-provinsi-bali.html
10. https://jakarta.bps.go.id/indicator/13/1236/1/upah-minimum-provinsi-dki-jakarta.html
11. https://www.cnbcindonesia.com/news/20231121170022-4-490810/cuma-naik-36-ump-dki-2024-jadi-tertinggi-se-indonesia#:~:text=Tahun%202023%2C%20UMP%20DKI%20Jakarta,125.897%2C61%20pada%20tahun%202024
12. https://ntb.bpk.go.id/wp-content/uploads/2021/12/RRA_11_4_UMP-NTB-Tahun-2022-naik-107-persen.pdf
13. https://disnakertrans.ntbprov.go.id/ump-ntb-2024-sebesar-rp-2-444-067-naik-3-06-atau-rp-72-660-dari-ump-2023/#:~:text=UMP%20NTB%202024%20sebesar%20Rp,Transmigrasi%20Provinsi%20Nusa%20Tenggara%20Barat
""")


st.header("Contact")
st.markdown("""
Halo, Nama saya Nur Fuji Fadhilah. Terima kasih telah mengunjungi project saya.

Saya lulusan Institut Pertanian Bogor jurusan Matematika. Saya telah bekerja di sebuah perusahaan pertambangan selama 1 tahun lebih 2 bulan sebagai SAP PM analyst divisi Technology Solution. Saya membuat visualisasi untuk mengetahui perbedaan antara pendapatan dan pengeluaran pekerja informal di Indonesia.

Saya juga memiliki pengalaman intern di Badan Pusat Statistik Kabupaten Batang pada divisi Integrasi Pengolahan dan Diseminasi Statistik. Ketika kuliah, saya mengajar matematika siswa SD, SMP dan SMA secara privat dan bimbel. Saya tertarik untuk mengupgrade skills terutama di bidang data.

Silakan hubungi saya untuk saran apa pun pada project ini atau cukup hubungi saya.

Terima kasih
""")

st.markdown("""
nurfujifadhilah04@gmail.com
            
https://www.linkedin.com/in/nur-fuji-fadhilah
            """)
