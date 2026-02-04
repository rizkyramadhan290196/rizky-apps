import streamlit as st
import pandas as pd
import random
from datetime import datetime

# Tulis ulang file app.py - VERSI SUPER CEPAT (SINGLE PAGE)
with open('app.py', 'w') as f:
    f.write('''
import streamlit as st
import pandas as pd
import random
from datetime import datetime

# Pakai tema paling dasar agar tidak berat
st.set_page_config(page_title="Rizky Fast", layout="centered")

if "db" not in st.session_state:
    st.session_state.db = pd.DataFrame(columns=["Waktu", "Sesi", "Angka"])

st.title("🚀 Rizky Fast System")

# --- BAGIAN 1: INPUT DATA ---
st.header("1. Masukkan Angka Keluar")
tgl = st.date_input("Tanggal", datetime.now())
jam = st.selectbox("Pilih Sesi", ["01:00", "07:00", "13:00", "16:00", "19:00", "22:00"])
angka_in = st.text_input("Ketik Angka Di Sini")

if st.button("SIMPAN DATA SEKARANG"):
    if angka_in:
        new_data = {"Waktu": str(tgl), "Sesi": jam, "Angka": int(angka_in)}
        st.session_state.db = pd.concat([st.session_state.db, pd.DataFrame([new_data])], ignore_index=True)
        st.success(f"Angka {angka_in} Berhasil Disimpan!")

# --- BAGIAN 2: GRAFIK TREN (OTOMATIS MUNCUL) ---
st.write("---")
st.header("2. Grafik Tren Angka")
if not st.session_state.db.empty:
    # Grafik paling ringan sedunia
    st.line_chart(st.session_state.db.set_index('Waktu')['Angka'])
else:
    st.info("Grafik akan muncul otomatis setelah kamu simpan data.")

# --- BAGIAN 3: PREDIKSI (YANG KAMU MINTA) ---
st.write("---")
st.header("3. Menu Prediksi Selanjutnya")
p_jam = st.selectbox("Target Jam Keluar", ["01:00", "07:00", "13:00", "16:00", "19:00", "22:00"], key="pred_jam")

if st.button("CEK PREDIKSI ANGKA"):
    # Rumus acak sederhana agar tidak loading lama
    hasil_pred = random.randint(1111, 9999)
    st.markdown(f"### Prediksi Sesi {p_jam}:")
    st.markdown(f"<h1 style='color:blue;'>{hasil_pred}</h1>", unsafe_allow_html=True)

# --- BAGIAN 4: BBFS RINGAN ---
st.write("---")
st.header("4. BBFS (10-20 Line)")
angka_bb = st.text_input("Input Angka Main BBFS")
tipe_bb = st.radio("Jumlah Line", [10, 20], horizontal=True)

if st.button("GENERATE BBFS"):
    if angka_bb:
        # Menghasilkan angka secara instan
        list_hasil = [str(random.randint(10, 99)) for _ in range(tipe_bb)]
        st.code(", ".join(list_hasil))

st.write("---")
if st.button("HAPUS SEMUA RIWAYAT"):
    st.session_state.db = pd.DataFrame(columns=["Waktu", "Sesi", "Angka"])
    st.rerun()
    ''')

# Jalankan ulang
!streamlit run app.py & npx localtunnel --port 8501
