import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os

# --- Konfigurasi Aplikasi ---
st.set_page_config(
    page_title="Live Word Cloud",
    page_icon="☁️",
    layout="centered",
    initial_sidebar_state="auto",
)

# --- Nama File untuk Menyimpan Data ---
WORDS_FILE = "submitted_words.txt"

# --- Fungsi untuk Membaca dan Menulis Kata ---
def add_words(text):
    """Menambahkan teks baru ke file."""
    with open(WORDS_FILE, "a", encoding="utf-8") as f:
        f.write(text + "\n")

def get_all_text():
    """Membaca semua teks dari file."""
    if not os.path.exists(WORDS_FILE):
        return ""
    with open(WORDS_FILE, "r", encoding="utf-8") as f:
        return f.read()

# --- Tampilan Utama Aplikasi ---
st.title("☁️ PEKERTI UNY 2025 - Kelompok 1")
st.write(
    "Simpulkan pembelajaran kita saat ini. Buat kalimat pendek yang anda ingat..."
)

# --- Form Input ---
with st.form(key="word_form", clear_on_submit=True):
    user_input = st.text_area("Ketik di sini:", height=100)
    submit_button = st.form_submit_button(label="Tambahkan ke Word Cloud")

# --- Logika Aplikasi ---
if submit_button and user_input:
    add_words(user_input)
    st.success(f"Teks Anda '{user_input[:30]}...' telah ditambahkan!")

# --- Menampilkan Word Cloud ---
all_text = get_all_text()

if all_text.strip():
    #st.header("Kelas hari ini")
    try:
        # Membuat dan menampilkan word cloud
        wordcloud = WordCloud(
            width=800,
            height=400,
            background_color="white",
            colormap="viridis",
            contour_width=1,
            contour_color="steelblue",
            min_font_size=10,
        ).generate(all_text)

        fig, ax = plt.subplots()
        ax.imshow(wordcloud, interpolation="bilinear")
        ax.axis("off")
        st.pyplot(fig)

        # Tombol untuk mengosongkan data
        if st.button("Reset Word Cloud (Hapus Semua Data)"):
            # Mengosongkan file
            with open(WORDS_FILE, "w") as f:
                f.write("")
            st.rerun()

    except Exception as e:
        st.error(f"Gagal membuat word cloud. Pastikan ada cukup kata unik. Error: {e}")

else:
    st.info("Belum ada kata yang dimasukkan. Jadilah yang pertama!")

st.markdown(f"""
    <center>
      dibuat sambil ☕️ oleh broto <br>
      <b>januari 2025<b> <br>
      <span style="font-size: 0.75em;">Google & Semanticscholar.org</span> <br>
    </center>
    """, unsafe_allow_html=True)

# --- Menampilkan Teks Mentah (Opsional) ---
with st.expander("Lihat semua teks yang sudah dimasukkan"):
    st.text_area("", value=all_text, height=200, disabled=True)
