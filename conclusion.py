# Import library data manipulasi dan visualisasi
import streamlit as st
import pandas as pd
import altair as alt
import plotly.graph_objects as go
import plotly.express as px

# Mengatur tampilan tata letak halaman menjadi lebar
st.set_page_config(layout='wide')

st.header("Kesimpulan")
st.markdown("""
1. Dari **34 provinsi di Indonesia pada tahun 2019-2023**, rata-rata pendapatan pekerja informal di Indonesia terhitung aman dari kesenjangan pendapatan, namun terdapat beberapa provinsi yang memiliki rata-rata pendapatan yang lebih rendah daripada rata-rata pengeluaran. Provinsi tersebut adalah **DKI Jakarta (2021, 2023), DI Yogyakarta (2020,2021,2022,2023), Bali (2020,2021), Nusa Tenggara Barat (2021,2023)**.             
2. Provinsi **DI Yogyakarta** menunjukkan kesenjangan pendapatan yang signifikan pada tahun 2020, 2021, 2022, 2023 bagi pekerja informal, dengan **tingkat pengeluaran yang terus meningkat dan pendapatan yang fluktuatif**.
3. **Bali** mengalami penurunan ekonomi pada tahun 2021 bagi pekerja informal, tetapi tidak mengalami kesenjangan pada tahun 2022-2023, **menandakan adanya perbaikan ekonomi**.
4. **DKI Jakarta** memiliki tingkat pengeluaran dan pendapatan tertinggi, tetapi juga mengalami peningkatan kesenjangan yang **mengindikasikan penurunan ekonomi pekerja informal**.
5. Di **Nusa Tenggara Barat**, terjadi kesenjangan pendapatan pada tahun 2021 dan 2023, tetapi adanya penurunan signifikan pada tahun 2023 **menunjukkan perbaikan ekonomi**.
6. Pengeluaran pekerja informal untuk kebutuhan **non-makanan lebih besar daripada pengeluaran untuk makanan**, sekitar dua kali lipat lebih banyak.
7. Pendapatan pekerja informal dari sektor **pertanian cenderung lebih rendah** dibandingkan dengan sektor-sektor lainnya.
8. Di **Yogyakarta**, kesenjangan **pendapatan** antara pekerja informal dan buruh yang mendapatkan **UMP tidak terlalu besar**. 
9. Di **Bali, DKI Jakarta, dan Nusa Tenggara Barat**, perbandingan pendapatan pekerja informal dengan UMP **menunjukkan kesenjangan yang cukup besar, mencerminkan ketidaksetaraan pendapatan antara pekerja informal dan buruh formal**.
""")