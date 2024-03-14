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

1. **Pemerintah Provinsi DI Yogyakarta** perlu memperhatikan **upaya meningkatkan pendapatan** pekerja informal, terutama di sektor **pertanian**. Selain itu, diperlukan analisis mendalam untuk memahami **penyebab** pengeluaran yang melebihi pendapatan bagi pekerja informal. Program **pelatihan dan pengembangan keterampilan** dapat membantu meningkatkan kualifikasi dan pendapatan pekerja informal mengingat **kesenjangan pendapatan pekerja informal di DI Yogyakarta tercatat dari tahun 2020 hingga 2023**.
            
2. Diperlukan **kebijakan pendapatan** bagi pekerja informal di **Pemerintah Provinsi DKI Jakarta** mengingat adanya **kesenjangan yang signifikan antara pendapatan mereka dengan UMP**.

3. Meskipun **Pemerintah Provinsi Bali dan NTB telah mengalami perbaikan ekonomi** bagi pekerja informal, **tetap diperlukan pemantauan, evaluasi yang berkelanjutan, serta kebijakan ekonomi** yang memengaruhi kondisi pekerja informal.          

4. Pekerja informal dapat **mengurangi pengeluaran, terutama pada kategori nonmakanan**, karena jenis pengeluaran ini menyumbang sebagian besar alokasi pengeluaran
mereka.

5. **Diperlukan keterlibatan dari berbagai pihak** untuk memastikan bahwa pekerja informal mendapatkan hak-haknya dan untuk meningkatkan peluang mereka menjadi
pekerja tetap.
""", unsafe_allow_html=True)
