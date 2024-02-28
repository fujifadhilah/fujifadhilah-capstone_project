# Import library data manipulasi dan visualisasi
import streamlit as st
import pandas as pd
import altair as alt
import plotly.graph_objects as go
import plotly.express as px

# Mengatur tampilan tata letak halaman menjadi lebar
st.set_page_config(layout='wide')

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
