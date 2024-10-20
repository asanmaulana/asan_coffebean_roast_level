import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image


def app():
    # title
    st.title('*Model CNN Deteksi Level Roasting Kopi*')

    # subheader
    st.subheader('Exploratory Data Analysis (EDA) dari Model')

    # add image
    image = Image.open('brewing_kopi.jpg')
    st.image(image)

    st.markdown('----')

    # penjelasan dataset 

    st.write ('''  Model ini akan membahas mengenai 3 biji kopi yaitu Laos Typica Bolaven, Doi Chaang, 
    dan Brazil Cerrado. Setiap varietas ini tentunya akan membutuhkan handling berbeda-beda tergantung 
    dari tingkat kematangannya. Semua kopi ini merupakan kopi yang berkualitas unggul dan memiliki daya 
    tarik tersendiri untuk komunitas kopi internasional. Sebagai informasi harga. Laos Typica itu sekitaran 
    20-30 dolar [link harga](https://laocoffee.nl/our-coffee/). Doi chaang harga perkilo sekitar 50 dolar - 70 dolar 
    [link harga](https://www.amazon.com/s?k=doi+chang+coffee&crid=2CBYQAFFVAAXK&sprefix=doi+chang+cof%2Caps%2C807&ref=nb_sb_ss_ts-doa-p_1_13).
     Dan kopi brazil cerado 30an dolar per kilonya [link harga](https://www.amazon.com/s?k=brazil+cerado&crid=23I2RT49UVCPW&sprefix=brazil+cerad%2Caps%2C733&ref=nb_sb_noss).
      Dengan harga segitu harusnya sebagai penikmat kopi harus memastikan bahwa setiap kopi yang di roasting harus memenuhi target tertentu.

    ''')

    st.write (''' Biji kopi ini hanya difokuskan pada 3 varietas tersebut. Dataset diambil dari JJ Mall Jatujak’s, “Bona Coffee.” di bangkok.  
    saya kurang tau mengapa alasan pengambilan dari 3 biji varietas tertentu itu. Asumsi saya mungkin di mall tersebut itu mungkin varietas 
    yang sering laku merupakan varietas kopi tersebut. Oleh karena itu kemungkinan model ini digunakan untuk memberi panduan kepada pegawai
     dari mall tersebut. Alasan saya membikin model ini untuk sebagai panduan kepada pecinta 3 biji kopi tersebut bagaimana level roasting yang benar.

Dataset ini berisi
*   Lao typica bolaven hijau (green bean / belum dipanggang)
*   Lao typica bolaven dipanggang Light
*   Doi Chaang dipanggang Medium
*   Brazil Cerrado dipanggang Dark   

    Di bawah ini akan digambarkan seperti apa biji kopi green bean, light roast, medium roast, dan dark roast.
    ''')

    # add image
    image = Image.open('dark.png')
    st.image(image,caption = 'Dark Roast Varietas Brazil Cerrado')

    st.markdown('----')

    # add image
    image = Image.open('green.png')
    st.image(image,caption = 'Green Bean Varietas Lao Typica Bolaven')

    st.markdown('----')

    # add image
    image = Image.open('light.png')
    st.image(image,caption = 'Light Roast Lao Typica Bolaven')

    st.markdown('----')

    # add image
    image = Image.open('medium.png')
    st.image(image,caption = 'Medium Roast Doi Chaang')

    st.markdown('----')

    st.write (''' Model ini memang ditujukan khusus 3 biji kopi ini saja. Memang pada biji kopi lain bisa untuk mendeteksi 
    namun sepertinya itu kurang powerfull masih ada beberapa missklasifikasi. Untuk mengoptimalkan kapasitas prediksi model ini lebih baik digunakan dengan 
    foto sesuai dengan foto studio. Kalau bisa hanya tampilkan satu biji kopi saja. Jangan lupa perlihatkan garis tengah dari biji kopi juga . 

    ''')







    


if __name__ == '__main__':
    app()
