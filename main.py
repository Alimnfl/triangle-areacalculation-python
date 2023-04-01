import streamlit as st

st.write("""
# Aplikasi Luas Segitiga
Ini adalah aplikasi menghitung luas segitiga sederhana menggunakan Streamlit
""")

Alas = st.number_input("Masukkan Alas", 0)
Tinggi = st.number_input("Masukkan Tinggi", 0)
Hitung = st.button("Hitung Luas")

if Hitung:
    Luas = 0.5 * Alas * Tinggi
    st.success(f"Luas segitiganya adalah {Luas}")
    st.balloons()