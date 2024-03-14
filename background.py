# Import library data manipulasi dan visualisasi
import streamlit as st
import pandas as pd
import altair as alt
import plotly.graph_objects as go
import plotly.express as px

# Mengatur tampilan tata letak halaman menjadi lebar
st.set_page_config(layout='wide')

# Judul dashboard
st.markdown("<h1 style='text-align: center; margin-bottom: 100px;}'>Dilema Pekerja Informal dalam Mengatasi Kesenjangan Pendapatan</h1>", unsafe_allow_html=True)

# Add image
from PIL import Image

image = Image.open("informal_worker.png")
st.image(
    image,
    use_column_width=True
)

