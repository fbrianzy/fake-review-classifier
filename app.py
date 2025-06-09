import streamlit as st
import pickle
from scipy.sparse import hstack, csr_matrix
from utils.preprocess import clean_text
import pandas as pd

model_dir = "./models/"

# Load semua model dan komponen
with open(f'{model_dir}model_nb.pkl', 'rb') as f:
    model_nb = pickle.load(f)
with open(f'{model_dir}model_rf.pkl', 'rb') as f:
    model_rf = pickle.load(f)
with open(f'{model_dir}model_dt.pkl', 'rb') as f:
    model_dtr = pickle.load(f)
with open(f'{model_dir}tf_idf.pkl', 'rb') as f:
    tfidf = pickle.load(f)
with open(f'{model_dir}username_encoder.pkl', 'rb') as f:
    username_encoder = pickle.load(f)

# Fungsi prediksi
def predict_review(username, ulasan_clean, model):
    # encode username
    if username in username_encoder.classes_:
        username_encoded = username_encoder.transform([username])[0]
    else:
        username_encoded = -1  # Untuk username baru/asing

    # bersihkan ulasan
    ulasan_clean = clean_text(ulasan_clean)
    
    # hitung panjang ulasan
    ulasan_length = len(ulasan_clean.split())

    # TF-IDF
    ulasan_tfidf = tfidf.transform([ulasan_clean])

    # Fitur tambahan
    additional = csr_matrix([[username_encoded, ulasan_length]])

    # Gabungkan
    final_input = hstack([ulasan_tfidf, additional])

    # Prediksi
    prediction = model.predict(final_input)
    return prediction[0]

# Streamlit UI
st.title('🕵️‍♂️ Fake Review Classifier')

# Input dari user
username = st.text_input('Masukkan Username')
ulasan = st.text_area('Masukkan Ulasan')

# Pilih model
model_choice = st.selectbox('Pilih Model untuk Prediksi', ['Naive Bayes', 'Random Forest', 'Decision Tree'])

# Tombol Prediksi
if st.button('Prediksi'):
    if not username or not ulasan:
        st.warning('Mohon lengkapi semua input.')
    else:
        if model_choice == 'Naive Bayes':
            model = model_nb
        elif model_choice == 'Decision Tree':
            model = model_dtr
        else:
            model = model_rf

        result = predict_review(username, ulasan, model)
        label = 'Fake' if result == 1 else 'Real'
        if label == 'Fake':
            st.error(f'Prediksi: {label} Review')
        else:
            st.success(f'Prediksi: {label} Review')
        
        