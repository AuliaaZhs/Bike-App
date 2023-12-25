import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Baca dataset
df = pd.read_csv('day.csv')  # Gantilah 'path_to_your_dataset.csv' dengan path yang sesuai

# Konversi kolom 'dteday' ke tipe data datetime
df['dteday'] = pd.to_datetime(df['dteday']).dt.date

# Set judul dashboard
st.title('Dashboard Analisis Penyewaan Sepeda')

# Sidebar untuk pemilihan rentang waktu
st.sidebar.header('Pilih Rentang Waktu')
date_range = st.sidebar.date_input('Pilih Rentang Waktu', [pd.Timestamp(df['dteday'].min()), pd.Timestamp(df['dteday'].max())])

# Filter data berdasarkan rentang waktu
filtered_df = df[(df['dteday'] >= date_range[0]) & (df['dteday'] <= date_range[1])]

# Tampilkan data yang dipilih
st.write(f"Menampilkan data dari {date_range[0]} hingga {date_range[1]}")

# Pengelompokan berdasarkan musim dan menghitung total penyewaan sepeda
distribusi_musim = filtered_df.groupby('season')['cnt'].sum()

# Plot distribusi penyewaan sepeda di setiap musim dengan warna berbeda
plt.figure(figsize=(8, 6))
sns.barplot(x=distribusi_musim.index, y=distribusi_musim.values, palette='viridis')  # Ganti 'viridis' dengan palet warna yang diinginkan
plt.title('Distribusi Penyewaan Sepeda di Setiap Musim')
plt.xlabel('Musim')
plt.ylabel('Total Penyewaan Sepeda')

# Tampilkan plot pada dashboard
st.pyplot(plt)

# Pengelompokan berdasarkan tanggal dan menghitung total penyewaan sepeda
distribusi_waktu = filtered_df.groupby('dteday')['cnt'].sum()

# Plot jumlah penyewaan sepeda pada rentang waktu
plt.figure(figsize=(12, 8))
plt.plot(distribusi_waktu.index, distribusi_waktu.values, linestyle='-')
plt.title('Jumlah Penyewaan Sepeda pada Rentang Waktu')
plt.xlabel('Tanggal')
plt.ylabel('Total Penyewaan Sepeda')
plt.xticks(rotation=45)  # Rotasi label tanggal untuk memudahkan membaca
plt.tight_layout()

# Tampilkan plot pada dashboard
st.pyplot(plt)