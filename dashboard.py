import pandas as pd
import streamlit as st 
import seaborn as sns 
import matplotlib.pyplot as plt


st.title('Dashboard Sederhana')
 
with st.sidebar:
    st.text('FADLAN BAHAR')
    st.text('LinkedIn : fadlanbahar')
    st.text('E-mail : fadlanbahar1@gmail.com')
 

# Load your data (ganti dengan kode pengambilan data Anda)
rel_path = './E-Commerce Public Dataset/customers_dataset.csv'
customerdf = pd.read_csv(rel_path)
customerdf.head()

rel_path1 = './E-Commerce Public Dataset/order_payments_dataset.csv'
order_payment = pd.read_csv(rel_path1)
order_payment.head()



st.write("Database Customer")
customerdf
st.write("Database Order Payment")
order_payment


#Assesing data
customerdf.info()
customerdf.isna().sum()
customerdf.describe() 
order_payment.info()
order_payment.isna().sum()
order_payment.describe()

#Cleansing Data
customerdf.dropna(inplace=True)
customerdf.isna().sum()
order_payment.dropna(inplace=True)
order_payment.isna().sum()

#Explorasi
customer_count = customerdf.groupby('customer_city')['customer_id'].nunique().reset_index(name='CustomerCount')
sorted_df = customer_count.sort_values(by='CustomerCount', ascending=False)
top_5 = sorted_df.head(5)
payment_counts = order_payment['payment_type'].value_counts()




# Visualisasi pertanyaan 1
st.title('TOP 5 Higher Customer by City')
plt.figure(figsize=(8, 6))
sns.barplot(x='customer_city', y='CustomerCount', data=top_5, palette='viridis')
plt.title('Frekuensi Customer per Wilayah')
plt.xlabel('Wilayah')
plt.ylabel('Jumlah Customer')
plt.show()
st.pyplot(plt)
st.caption('Copyright (c) 2023 ')


# Visualisasi pertanyaan 2
plt.figure(figsize=(8, 6))
sns.countplot(x='payment_type', data=order_payment, order=order_payment["payment_type"].value_counts().index)
plt.title('Frekuensi Tipe Pembayaran')
plt.xlabel('Metode Pembayaran')
plt.ylabel('Jumlah Penggunaan')
plt.show()
st.pyplot(plt)
st.caption('Copyright (c) 2023 ')


st.text('TERIMA KASIH DICODING')


