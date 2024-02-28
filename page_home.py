# Import library data manipulasi dan visualisasi
import streamlit as st
import pandas as pd
import altair as alt
import plotly.graph_objects as go
import plotly.express as px

# Mengatur tampilan tata letak halaman menjadi lebar
st.set_page_config(layout='wide')

# Sub-judul
st.header("Problem Statement")
st.markdown("""<p style='text-align: justify; text-indent: 40px;'>Dalam arti sesungguhnya, tujuan orang bekerja adalah untuk memperoleh penghasilan guna memenuhi kebutuhan hidup, baik itu kebutuhan pangan maupun kebutuhan lainnya. Kebijakan pengaturan upah di Indonesia, yaitu melalui Upah Minimum Provinsi (UMP), namun hanya berlaku untuk buruh/karyawan/pegawai. Dalam kenyataan, pekerja yang hanya mendapatkan upah sebesar UMP saja sering mengalami kesulitan, apalagi bagi mereka yang bekerja sebagai non-buruh.
Pada Agustus 2023, terdapat kenyataan bahwa jumlah pekerja informal atau pekerja non-buruh mendominasi dengan mencapai 59,11% di Indonesia. </p>

<p style='text-align: justify; text-indent: 40px;'>Pekerja informal seringkali menghadapi berbagai tantangan dan dilema. Bagi mereka, pendapatan hanya diperoleh saat mereka bekerja, sehingga ketidakhadiran karena izin, sakit, atau alasan lainnya berarti kehilangan pendapatan. Karakteristik pekerjaan informal sering tidak menentu dan tidak stabil, menyulitkan perencanaan keuangan. Hal ini dapat mengakibatkan terjadinya kesenjangan yang lebih besar antara pendapatan dan pengeluaran.
Pekerja informal juga menghadapi pendapatan dari pekerjaan yang tidak tetap seiring dengan biaya hidup yang semakin meningkat. Kurangnya akses ke layanan keuangan formal seperti kredit atau pinjaman bank membuat pekerja informal terjebak dalam lingkaran kemiskinan, karena sulit bagi mereka untuk mendapatkan modal untuk meningkatkan atau memperluas usaha mereka.</p>

<p style='text-align: justify; text-indent: 40px;'>Lantas, Bagaimana jika pengeluaran mereka melebihi pendapatannya? Apa kebijakan yang sebaiknya diterapkan oleh pemerintah untuk mengatasi situasi tersebut? Dan tindakan apa yang harus diambil oleh pekerja informal untuk mengatasi ketidakseimbangan tersebut?</p> 
""", unsafe_allow_html=True)
