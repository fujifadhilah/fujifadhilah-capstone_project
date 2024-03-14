# Import library data manipulasi dan visualisasi
import streamlit as st
import pandas as pd
import altair as alt
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

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

# 1. membuat line chart selisih pendapatan dan pengeluaran
st.header("Rata-rata Pendapatan vs Pengeluaran Pekerja Informal")

# Cari selisih antara pendapatan dan pengeluaran
selisihList = incomes - outcomes

# Grouping menjadi selisihPlus dan selisihMins
selisihPlus = []
selisihMins = []
for selisih in selisihList:
    if selisih < 0:
        selisihMins.append(selisih)
    else:
        selisihPlus.append(selisih)
    i+=1


st.markdown("""
Pekerja informal yang akan dibahas meiliputi pekerja bebas dan pekerja berusaha sendiri. 
1. Definisi **pekerja bebas** adalah pekerja yang tidak memiliki majikan tetap (lebih dari 1 majikan dalam sebulan terakhir, khusus pada sektor bangunan biasanya tiga bulan). Contoh: pekerja di bidang jasa pertanian, perkebunan, perikanan, bangunan, dll.
2. Definisi **pekerja berusaha sendiri** adalah bekerja atau berusaha dengan menanggung resiko sendiri, serta tidak menggunakan pekerja dibayar maupun pekerja tak dibayar, termasuk yang sifat pekerjaannya memerlukan teknologi atau keahlian khusus. Contoh: pedagang kecil di pasar tradisional, pemilik warung makan kecil, petani, penjahit lepas, pengemudi ojek online dll.
""", unsafe_allow_html=True)


tab1, tab2, tab3, tab4, tab5 = st.tabs(['2019', '2020', '2021', '2022', '2023'])

with tab1:
    st.subheader("Tahun 2019")

    # df 2019
    df2019 = df.loc[df['year'] == 2019]
    # convert income from series to list
    income2019 = df2019['income'].tolist()
    outcome2019 = df2019['outcome'].tolist()
    # Mengambil kolom provinsi dan dijadikan list mengguntakan tolist(), karena bentuk sebelumnya adalah series
    province2019 = df2019['province'].tolist()
    incomeColors = ['#B4B4B8', ] * 34
    outcomeColors = ['#C7C8CC', ] * 34
    for index in range(len(province2019)):
        if (income2019[index] < outcome2019[index]):
            incomeColors[index] = '#387ADF'
            outcomeColors[index] = '#50C4ED'
            
    image2 = go.Figure()
    image2.add_trace(go.Bar(
        x=province2019,
        y=income2019,
        name='Income',
        marker_color=incomeColors,
        text=income2019,
        texttemplate='%{text:.2s}',
        textfont_size=12,
        textangle=0, 
        textposition="outside", 
        cliponaxis=False
    ))
    image2.add_trace(go.Bar(
        x=province2019,
        y=outcome2019,
        name='Outcome',
        marker_color=outcomeColors,
        text=outcome2019,
        texttemplate='%{text:.2s}',
        textfont_size=12,
        textangle=0, 
        textposition="outside", 
        cliponaxis=False
    ))
    # Here we modify the tickangle of the xaxis, resulting in rotated labels.
    image2.update_layout(barmode='group', xaxis_tickangle=-45, width=1400)
   
    #Update X & Y Labels
    image2.update_xaxes(title="<b>Province</b>",title_font=dict(size=13,family="arial"))
    image2.update_yaxes(title="<b>Value (Rp) </b>", title_font=dict(size=13,family="arial"))

    st.plotly_chart(image2, theme="streamlit")
    
    custom_container = st.container(border=True)
    with custom_container:
        st.markdown("Berdasarkan data rata-rata pendapatan bersih dan pengeluaran per kapita setiap bulan bagi pekerja informal di daerah perkotaan dan pedesaan menurut provinsi, pada tahun 2019 dari total 34 provinsi di Indonesia, situasi tergolong **aman** karena **tingkat pengeluaran lebih rendah daripada pendapatan**.")




# Chart 2
with tab2:
    st.subheader("Tahun 2020")

    df2020 = df.loc[df["year"]==2020]
    income2020 = df2020["income"].tolist()
    outcome2020 = df2020["outcome"].tolist()

    province2020 = df2020["province"].tolist()
    incomeColors = ['#B4B4B8', ] * 34
    outcomeColors = ['#C7C8CC', ] * 34
    for index in range(len(province2020)):
        if (income2020[index] < outcome2020[index]):
            incomeColors[index] = '#387ADF'
            outcomeColors[index] = '#50C4ED'
            
    image1 = go.Figure()
    image1.add_trace(go.Bar(
        x=province2020,
        y=income2020,
        name='Income',
        marker_color=incomeColors,
        text=income2020,
        texttemplate='%{text:.2s}',
        textfont_size=12,
        textangle=0, 
        textposition="outside", 
        cliponaxis=False
    ))
    image1.add_trace(go.Bar(
        x=province2020,
        y=outcome2020,
        name='Outcome',
        marker_color=outcomeColors,
        text=outcome2020,
        texttemplate='%{text:.2s}',
        textfont_size=12,
        textangle=0, 
        textposition="outside", 
        cliponaxis=False
    ))
    
    # Here we modify the tickangle of the xaxis, resulting in rotated labels.
    image1.update_layout(barmode='group', xaxis_tickangle=-45, width=1400)
    
    #Update X & Y Labels
    image1.update_xaxes(title="<b>Province</b>",title_font=dict(size=13,family="arial"))
    image1.update_yaxes(title="<b>Value (Rp) </b>", title_font=dict(size=13,family="arial"))

    st.plotly_chart(image1, theme="streamlit")
    
    st.markdown("""
            * biru tua : income
            * biru muda : outcome
            """)

    custom_container = st.container(border=True)
    with custom_container:
        st.markdown("Pada tahun 2020 terdapat **2 dari 34 provinsi yang mengalami defisit pendapatan** yaitu **DI Yogyakarta** dengan selisih sebesar **Rp194.498** dan **Bali** dengan selisih sebesar **Rp28.013** hal tersebut terjadi beriringan dengan mulainya pandemi COVID-19 di Indonesia.")

# Chart 3
with tab3:
    st.subheader("Tahun 2021")
    # df 2021
    df2021 = df.loc[df["year"]==2021]
    income2021 = df2021["income"].tolist()
    outcome2021 = df2021["outcome"].tolist()
    # Mengambil kolom provinsi dan dijadikan list mengguntakan tolist(), karena bentuk sebelumnya adalah series
    province2021 = df2021["province"].tolist()
    incomeColors = ['#B4B4B8', ] * 34
    outcomeColors = ['#C7C8CC', ] * 34
    for index in range(len(province2021)):
        if (income2021[index] < outcome2021[index]):
            incomeColors[index] = '#387ADF'
            outcomeColors[index] = '#50C4ED'
            
    image3 = go.Figure()
    image3.add_trace(go.Bar(
        x=province2021,
        y=income2021,
        name='Income',
        marker_color=incomeColors,
        text=income2021,
        texttemplate='%{text:.2s}',
        textfont_size=12,
        textangle=0, 
        textposition="outside", 
        cliponaxis=False
    ))
    image3.add_trace(go.Bar(
        x=province2021,
        y=outcome2021,
        name='Outcome',
        marker_color=outcomeColors,
        text=outcome2021,
        texttemplate='%{text:.2s}',
        textfont_size=12,
        textangle=0, 
        textposition="outside", 
        cliponaxis=False
    ))
    # Here we modify the tickangle of the xaxis, resulting in rotated labels.
    image3.update_layout(barmode='group', xaxis_tickangle=-45, width=1400)
    
    #Update X & Y Labels
    image3.update_xaxes(title="<b>Province </b>",title_font=dict(size=13,family="arial"))
    image3.update_yaxes(title="<b>Value (Rp) </b>", title_font=dict(size=13,family="arial"))

    st.plotly_chart(image3, theme="streamlit")
    
    st.markdown("""
            * biru tua : income
            * biru muda : outcome
            """)

    custom_container = st.container(border=True)
    with custom_container:
        st.markdown("Pada tahun 2021 terdapat **4 dari 34 provinsi yang mengalami defisit pendapatan** yaitu **DKI Jakarta** dengan selisih sebesar **Rp134.427**, **DI Yogyakarta** dengan selisih sebesar **Rp282.499**, **Bali** dengan selisih sebesar **Rp204.353**, **Nusa Tenggara Barat** dengan selisih sebesar **131.885**.")

# Chart 4
with tab4:
    st.subheader("Tahun 2022")

    df2022 = df.loc[df["year"]==2022]
    income2022 = df2022['income'].tolist()
    outcome2022 = df2022['outcome'].tolist()

    province2022 = df2022["province"].tolist()
    incomeColors = ['#B4B4B8', ] * 34
    outcomeColors = ['#C7C8CC', ] * 34
    for index in range(len(province2022)):
        if (income2022[index] < outcome2022[index]):
            incomeColors[index] = '#387ADF'
            outcomeColors[index] = '#50C4ED'
            
    image3 = go.Figure()
    image3.add_trace(go.Bar(
        x=province2022,
        y=income2022,
        name='Income',
        marker_color=incomeColors,
        text=income2022,
        texttemplate='%{text:.2s}',
        textfont_size=12,
        textangle=0, 
        textposition="outside", 
        cliponaxis=False
    ))
    image3.add_trace(go.Bar(
        x=province2022,
        y=outcome2022,
        name='Outcome',
        marker_color=outcomeColors,
        text=outcome2022,
        texttemplate='%{text:.2s}',
        textfont_size=12,
        textangle=0, 
        textposition="outside", 
        cliponaxis=False
    ))
    # Here we modify the tickangle of the xaxis, resulting in rotated labels.
    image3.update_layout(barmode='group', xaxis_tickangle=-45, width=1400)
    
    #Update X & Y Labels
    image3.update_xaxes(title="<b>Province</b>",title_font=dict(size=13,family="arial"))
    image3.update_yaxes(title="<b>Value (Rp) </b>", title_font=dict(size=13,family="arial"))
    
    st.plotly_chart(image3, theme="streamlit")
    
    st.markdown("""
            * biru tua : income
            * biru muda : outcome
            """)

    custom_container = st.container(border=True)
    with custom_container:
        st.markdown(" Pada tahun 2022 terdapat **1 dari 34 provinsi yang mengalami defisit pendapatan** yaitu **DI Yogyakarta** dengan selisih sebesar **Rp156.674**.")


# Chart 5
with tab5:
    st.subheader("Tahun 2023")

    df2023 = df.loc[df["year"]==2023]
    income2023 = df2023['income'].tolist()
    outcome2023 = df2023['outcome'].tolist()

    province2023 = df2023["province"].tolist()
    incomeColors = ['#B4B4B8', ] * 34
    outcomeColors = ['#C7C8CC', ] * 34
    for index in range(len(province2023)):
        if (income2023[index] < outcome2023[index]):
            incomeColors[index] = '#387ADF'
            outcomeColors[index] = '#50C4ED'
            
    image4 = go.Figure()
    image4.add_trace(go.Bar(
        x=province2023,
        y=income2023,
        name='Income',
        marker_color=incomeColors,
        text=income2023,
        texttemplate='%{text:.2s}',
        textfont_size=12,
        textangle=0, 
        textposition="outside", 
        cliponaxis=False
    ))
    image4.add_trace(go.Bar(
        x=province2023,
        y=outcome2023,
        name='Outcome',
        marker_color=outcomeColors,
        text=outcome2023,
        texttemplate='%{text:.2s}',
        textfont_size=12,
        textangle=0, 
        textposition="outside", 
        cliponaxis=False
    ))
    # Here we modify the tickangle of the xaxis, resulting in rotated labels.
    image4.update_layout(barmode='group', xaxis_tickangle=-45, width=1400)
    
    #Update X & Y Labels
    image4.update_xaxes(title="<b>Province</b>",title_font=dict(size=13,family="arial"))
    image4.update_yaxes(title="<b>Value (Rp) </b>", title_font=dict(size=13,family="arial"))
    
    st.plotly_chart(image4, theme="streamlit")
    
    st.markdown("""
            * biru tua : income
            * biru muda : outcome
            """)

    custom_container = st.container(border=True)
    with custom_container:
        st.markdown(" Pada tahun 2023 terdapat **3 dari 34 provinsi yang mengalami defisit pendapatan** yaitu **DKI Jakarta** dengan selisih sebesar **Rp451.716**, **DI Yogyakarta** dengan selisih **Rp382.727**, dan **Nusa Tenggara Barat** dengan selisih sebesar **Rp44.753**.")

import plotly.express as px

default_color = "blue"
colors = {"China": "red"}

data = px.data.gapminder().query("year == 1952")

color_discrete_map = {
    c: colors.get(c, default_color) 
    for c in data.country.unique()}

fig = px.bar(data, x='country', y='pop', color='country',
             color_discrete_map=color_discrete_map)
fig.update_traces(showlegend=True)

# fig.show()