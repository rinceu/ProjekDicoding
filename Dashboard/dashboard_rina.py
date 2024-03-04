import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import seaborn as sns

# INPUT DATA
day_df = pd.read_csv('https://raw.githubusercontent.com/rinceu/ProjekDicoding/main/Dashboard/day_data%20(1).csv')

#EDA
weekday_sum = day_df.groupby(['weekday']).agg({'cnt':'sum'}).reset_index()
day_sum = day_df.groupby(['season']).agg({'cnt':'sum'}).reset_index()

# Display the resulting DataFrame
print(day_df)

st.header('Proyek Analisis Data Dashboard :sparkles:')

with st.sidebar:
    # Menambahkan gambar
    st.image("https://cdn-icons-png.flaticon.com/512/171/171253.png")
    st.subheader("Rina Adhista as student at Bangkit Academy")
    st.write("Analisis data pada dataset berjudul Bike Sharing Dataset")
tab1, tab2 = st.tabs(["Tab 1","Tab 2"])

with tab1 :
    st.title("Perbandingan jumlah penyewa berdasarkan musim pada data")
    plt.figure(figsize=(10, 5))

    sns.barplot(
        x="season",
        y="cnt",
        data=day_sum.sort_values(by="cnt", ascending=False),
    )

    plt.title("Perbandingan jumlah penyewa berdasarkan musim pada data", loc="center", fontsize=15)
    plt.xlabel("Musim")
    plt.ylabel("Jumlah Penyewa")
    plt.tick_params(axis='x', labelsize=12)

    # Display the plot using Streamlit
    st.pyplot(plt)
    with st.expander("Lihat Penjelasan"):
        st.write("Pada eksplor data tersebut tertera bahwa penyewaan sepeda banyak terjadi pada season 3 yatu pada season fall dan penyewaan paling sedikit terjadi pada season 1 yaitu springer")

with tab2:
    st.title("Perbandingan jumlah penyewa berdasarkan hari pada data")
    plt.figure(figsize=(10, 5))

    sns.barplot(
        x="weekday",
        y="cnt",
    data=weekday_sum.sort_values(by="cnt", ascending=False),
    )

    plt.title("Perbandingan jumlah penyewa berdasarkan hari pada data", loc="center", fontsize=15)
    plt.xlabel("Hari")
    plt.ylabel("Jumlah Penyewa")
    plt.tick_params(axis='x', labelsize=12)

    # Display menggunakan pyplot
    st.pyplot(plt)

    with st.expander("Lihat Penjelasan"):
        st.write("Melalui hasil di atas maka dari itu banyak terjadi penyewaan pada saat weekday pada hari ke 5 atau bisa diasumsikan hari jumat dengan total yaitu 487790 dan paling sedikit pada hari ke 0 atau bisa diasumsikan hari minggu dengan total 444027")