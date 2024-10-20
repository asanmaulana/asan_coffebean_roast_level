import streamlit as st
from PIL import Image
import numpy as np
from keras.preprocessing.image import load_img, img_to_array 
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.vgg16 import preprocess_input

# load model
model = load_model('my_model.h5')

with open('classes.txt', 'r') as file:
    class_names = [line.strip() for line in file]

def app():
    # deskripsi model

    st.title('*Model CNN Deteksi Level Roasting Kopi*')
             
    st.write('''
    **Machine Learning Model Prediksi Roasting Level Kopi**
    Model ini digunakan untuk melihat klasifikasi antara 3 varietas kopi.
    - Lao typica bolaven dipanggang Light
    - Doi Chaang dipanggang Medium
    - Brazil Cerrado dipanggang Dark
    - Penggunaan framework model cnn lain yaitu VGG16 untuk improve hasil akurasi dari model.
    - Model bisa menyentuh akurasi 100% pada data test untuk foto-foto yang berisi foto studio (dalam notebook)
    ''')
    
    st.divider()
    
    # upload file
    input_file = st.file_uploader("Upload gambar yang ingin dianalisa!", type=["jpg", "jpeg", "png"])

    # display gambar
    if input_file is not None:
        image = Image.open(input_file) 
        image = image.resize((220, 220))  
        st.image(image, caption='Gambar yang di Upload', use_column_width=True)
    else:
        st.write("Silahkan Upload Gambar Anda")

    st.divider()

    # predict
    if st.button("Classify Gambar"):
        if input_file is not None:
            # Read dan preprocess image
            img = load_img(input_file, target_size=(220, 220)) 
            img_array = img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array = preprocess_input(img_array)

            # masukkan image ke  model
            classes = model.predict(img_array)
            class_idx = np.argmax(classes, axis=-1)

            # display result di center
            st.write('<h1 style="text-align: center"> Predicted Class:<br> {}'.format(class_names[class_idx[0]]), unsafe_allow_html=True)  
    
        else:
            st.error("Silahkan Upload Gambar Dahulu.")
        
if __name__ == '__main__':
  app()
