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
1. Provinsi DI Yogyakarta menunjukkan kesenjangan pendapatan yang signifikan pada tahun 2020 hingga 2023 bagi pekerja informal, dengan tingkat pengeluaran yang terus meningkat dan pendapatan yang fluktuatif.
2. Bali mengalami penurunan ekonomi pada tahun 2021 bagi pekerja informal, tetapi tidak mengalami kesenjangan pada tahun 2022-2023, menandakan adanya perbaikan ekonomi.
3. DKI Jakarta memiliki tingkat pengeluaran dan pendapatan tertinggi, tetapi juga mengalami peningkatan kesenjangan yang mengindikasikan penurunan ekonomi pekerja informal.
4. Di Nusa Tenggara Barat, terjadi kesenjangan pendapatan pada tahun 2021 dan 2023, tetapi adanya penurunan signifikan pada tahun 2023 menunjukkan perbaikan ekonomi.
5. Pengeluaran pekerja informal untuk kebutuhan non-makanan lebih besar daripada pengeluaran untuk makanan, sekitar dua kali lipat lebih banyak.
6. Pendapatan pekerja informal dari sektor pertanian cenderung lebih rendah dibandingkan dengan sektor-sektor lainnya.
7. Di Yogyakarta, kesenjangan pendapatan antara pekerja informal dan buruh yang mendapatkan UMP tidak terlalu besar. 
8. Di Bali, DKI Jakarta, dan Nusa Tenggara Barat, perbandingan pendapatan pekerja informal dengan UMP menunjukkan kesenjangan yang cukup besar, mencerminkan ketidaksetaraan pendapatan antara pekerja informal dan buruh formal.
""")