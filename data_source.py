# Import library data manipulasi dan visualisasi
import streamlit as st
import pandas as pd
import altair as alt
import plotly.graph_objects as go
import plotly.express as px

# Mengatur tampilan tata letak halaman menjadi lebar
st.set_page_config(layout='wide')

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