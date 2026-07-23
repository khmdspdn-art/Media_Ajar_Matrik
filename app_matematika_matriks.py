import streamlit as st
import pandas as pd
import numpy as np

# -----------------------------------------------------------------------------
# 1. KONFIGURASI HALAMAN & STATE INITIALIZATION
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Petualangan Matematika Interaktif - Matriks",
    page_icon="🧮",
    layout="wide"
)

# Inisialisasi Gamifikasi & Skor XP
if 'score_mat' not in st.session_state:
    st.session_state.score_mat = 0
if 'badge_mat' not in st.session_state:
    st.session_state.badge_mat = "Novice Mathematician 🐣"

def update_badge_mat():
    if st.session_state.score_mat >= 130:
        st.session_state.badge_mat = "Matrix Master 🧙‍♂️"
    elif st.session_state.score_mat >= 90:
        st.session_state.badge_mat = "Algebra Knight ⚔️"
    elif st.session_state.score_mat >= 50:
        st.session_state.badge_mat = "Math Explorer 🧭"
    else:
        st.session_state.badge_mat = "Novice Mathematician 🐣"

# -----------------------------------------------------------------------------
# 2. SIDEBAR (GAMIFICATION & NAVIGASI)
# -----------------------------------------------------------------------------
st.sidebar.title("🎮 Status Profil Siswa")
st.sidebar.info("**Pemain:** Pembelajar Matematika")
st.sidebar.metric(label="Total XP (Poin)", value=f"{st.session_state.score_mat} XP")
st.sidebar.markdown(f"**Gelar:** `{st.session_state.badge_mat}`")
st.sidebar.divider()

menu = st.sidebar.radio(
    "Navigasi Zona Belajar:",
    [
        "🏠 Beranda Utama",
        "1. Konsep Dasar & Contoh Nyata",
        "2. Simulasi Kalkulator Matriks",
        "🎯 Kuis Evaluasi (15 Soal PG)"
    ]
)

# -----------------------------------------------------------------------------
# ZONA 0: BERANDA UTAMA
# -----------------------------------------------------------------------------
if menu == "🏠 Beranda Utama":
    st.title("🧮 Petualangan Matematika: Operasi Matriks Interaktif")
    st.write(
        "Selamat datang di media pembelajaran matematika! Aplikasi ini dirancang untuk "
        "membantu Anda menguasai **Operasi Matriks** melalui konsep nyata, kalkulator visual interaktif, dan kuis berhadiah XP."
    )

    st.subheader("🎯 Capaian Tujuan Pembelajaran (TP):")
    st.success("✅ **Peserta didik mampu menentukan hasil operasi matriks (penjumlahan, pengurangan, dan perkalian matriks) dengan benar.**")

    st.divider()
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("➕ **1. Penjumlahan Matriks**\n\nMenjumlahkan elemen-elemen yang seletak pada matriks berordo sama.")
    with col2:
        st.warning("➖ **2. Pengurangan Matriks**\n\nMengurangkan elemen-elemen yang seletak pada matriks berordo sama.")
    with col3:
        st.error("✖️ **3. Perkalian Matriks**\n\nPerkalian skalar dan perkalian antar-matriks (Baris × Kolom).")

    st.divider()
    st.info("💡 **Petunjuk:** Silakan pilih menu di sidebar kiri untuk mulai belajar!")

# -----------------------------------------------------------------------------
# ZONA 1: KONSEP DASAR & CONTOH NYATA
# -----------------------------------------------------------------------------
elif menu == "1. Konsep Dasar & Contoh Nyata":
    st.header("📚 Misi 1: Memahami Konsep Operasi Matriks")
    st.write("Matriks adalah susunan bilangan berbentuk persegi atau persegi panjang yang diatur dalam baris dan kolom.")

    st.subheader("1. Ringkasan Aturan Operasi Matriks")
    
    matriks_data = {
        "Jenis Operasi": [
            "Penjumlahan Matriks",
            "Pengurangan Matriks",
            "Perkalian Skalar",
            "Perkalian Antar-Matriks"
        ],
        "Syarat Operasi": [
            "Ordo kedua matriks harus SAMA (misal: sama-sama 2x2).",
            "Ordo kedua matriks harus SAMA.",
            "Dapat dilakukan pada matriks ordo berapapun.",
            "Jumlah KOLOM matriks pertama = Jumlah BARIS matriks kedua."
        ],
        "Cara Penyelesaian": [
            "Jumlahkan elemen yang SELETAK (posisi baris dan kolomnya sama).",
            "Kurangkan elemen yang SELETAK.",
            "Kalikan setiap elemen matriks dengan angka skalar k.",
            "Kalikan elemen BARIS matriks A dengan KOLOM matriks B, lalu jumlahkan."
        ],
        "Contoh Penerapan Nyata": [
            "Menggabungkan data stok barang dari dua cabang toko yang berbeda.",
            "Menghitung selisih penjualan bulan ini dengan bulan lalu untuk setiap barang.",
            "Menghitung total harga setelah kenaikan persen/kelipatan harga barang.",
            "Menghitung total biaya belanja barang berdasarkan kuantitas dan harga satuan."
        ]
    }
    df_mat = pd.DataFrame(matriks_data)
    st.dataframe(df_mat, use_container_width=True, hide_index=True)

    st.divider()
    st.subheader("2. Formulasi Matematis")
    
    st.markdown("#### a. Penjumlahan & Pengurangan (Ordo 2x2)")
    st.latex(r'''
    \begin{pmatrix} a & b \\ c & d \end{pmatrix} \pm \begin{pmatrix} e & f \\ g & h \end{pmatrix} = \begin{pmatrix} a \pm e & b \pm f \\ c \pm g & d \pm h \end{pmatrix}
    ''')

    st.markdown("#### b. Perkalian Antar-Matriks (Baris × Kolom)")
    st.latex(r'''
    \begin{pmatrix} a & b \\ c & d \end{pmatrix} \times \begin{pmatrix} e & f \\ g & h \end{pmatrix} = \begin{pmatrix} (a\cdot e + b\cdot g) & (a\cdot f + b\cdot h) \\ (c\cdot e + d\cdot g) & (c\cdot f + d\cdot h) \end{pmatrix}
    ''')

# -----------------------------------------------------------------------------
# ZONA 2: SIMULASI KALKULATOR MATRIKS INTERAKTIF
# -----------------------------------------------------------------------------
elif menu == "2. Simulasi Kalkulator Matriks":
    st.header("🧮 Misi 2: Simulasi Kalkulator Matriks Interaktif")
    st.write("Masukkan nilai elemen-elemen Matriks A dan Matriks B di bawah ini untuk melihat proses perhitungannya secara langsung!")

    st.subheader("1. Input Elemen Matriks A dan B (Ordo 2x2)")
    
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.markdown("### 🟦 Matriks A")
        c1, c2 = st.columns(2)
        a11 = c1.number_input("A[1,1]", value=3, key="a11")
        a12 = c2.number_input("A[1,2]", value=2, key="a12")
        a21 = c1.number_input("A[2,1]", value=1, key="a21")
        a22 = c2.number_input("A[2,2]", value=4, key="a22")

    with col_b:
        st.markdown("### 🟩 Matriks B")
        c3, c4 = st.columns(2)
        b11 = c3.number_input("B[1,1]", value=5, key="b11")
        b12 = c4.number_input("B[1,2]", value=1, key="b12")
        b21 = c3.number_input("B[2,1]", value=2, key="b21")
        b22 = c4.number_input("B[2,2]", value=3, key="b22")

    mat_A = np.array([[a11, a12], [a21, a22]])
    mat_B = np.array([[b11, b12], [b21, b22]])

    st.divider()
    st.subheader("2. Hasil Operasi Matriks")

    tab1, tab2, tab3 = st.tabs(["➕ Penjumlahan (A + B)", "➖ Pengurangan (A - B)", "✖️ Perkalian (A × B)"])

    with tab1:
        st.markdown("### Hasil Penjumlahan: Matriks A + Matriks B")
        res_add = mat_A + mat_B
        
        st.write("**Langkah Perhitungan:**")
        st.latex(f'''
        \\begin{{pmatrix}} {a11} & {a12} \\\\ {a21} & {a22} \\end{{pmatrix}} + \\begin{{pmatrix}} {b11} & {b12} \\\\ {b21} & {b22} \\end{{pmatrix}} = \\begin{{pmatrix}} {a11}+{b11} & {a12}+{b12} \\\\ {a21}+{b21} & {a22}+{b22} \\end{{pmatrix}}
        ''')
        
        st.success(f"**Hasil Akhir:**\n\n [[{res_add[0,0]}, {res_add[0,1]}], [{res_add[1,0]}, {res_add[1,1]}]]")

    with tab2:
        st.markdown("### Hasil Pengurangan: Matriks A - Matriks B")
        res_sub = mat_A - mat_B
        
        st.write("**Langkah Perhitungan:**")
        st.latex(f'''
        \\begin{{pmatrix}} {a11} & {a12} \\\\ {a21} & {a22} \\end{{pmatrix}} - \\begin{{pmatrix}} {b11} & {b12} \\\\ {b21} & {b22} \\end{{pmatrix}} = \\begin{{pmatrix}} {a11}-{b11} & {a12}-{b12} \\\\ {a21}-{b21} & {a22}-{b22} \\end{{pmatrix}}
        ''')
        
        st.warning(f"**Hasil Akhir:**\n\n [[{res_sub[0,0]}, {res_sub[0,1]}], [{res_sub[1,0]}, {res_sub[1,1]}]]")

    with tab3:
        st.markdown("### Hasil Perkalian: Matriks A × Matriks B")
        res_mul = np.dot(mat_A, mat_B)
        
        st.write("**Langkah Perhitungan (Baris × Kolom):**")
        st.latex(f'''
        \\begin{{pmatrix}} {a11} & {a12} \\\\ {a21} & {a22} \\end{{pmatrix}} \\times \\begin{{pmatrix}} {b11} & {b12} \\\\ {b21} & {b22} \\end{{pmatrix}} = \\begin{{pmatrix}} ({a11}\\cdot{b11} + {a12}\\cdot{b21}) & ({a11}\\cdot{b12} + {a12}\\cdot{b22}) \\\\ ({a21}\\cdot{b11} + {a22}\\cdot{b21}) & ({a21}\\cdot{b12} + {a22}\\cdot{b22}) \\end{{pmatrix}}
        ''')
        
        st.info(f"**Hasil Akhir:**\n\n [[{res_mul[0,0]}, {res_mul[0,1]}], [{res_mul[1,0]}, {res_mul[1,1]}]]")

# -----------------------------------------------------------------------------
# ZONA 3: KUIS EVALUASI (15 SOAL PG)
# -----------------------------------------------------------------------------
elif menu == "🎯 Kuis Evaluasi (15 Soal PG)":
    st.header("🎯 Kuis Evaluasi Matriks (15 Soal PG)")

    questions = [
        {"q": "1. Jika A = [[2, 3], [1, 4]] dan B = [[1, 2], [3, 5]], maka A + B adalah...", "options": ["[[3, 5], [4, 9]]", "[[1, 1], [-2, -1]]", "[[2, 6], [3, 20]]", "[[3, 1], [4, 9]]"], "answer": "[[3, 5], [4, 9]]"},
        {"q": "2. Syarat utama dua buah matriks dapat dijumlahkan atau dikurangkan adalah...", "options": ["Mempunyai determinan yang sama", "Memiliki ordo yang sama", "Jumlah baris lebih banyak dari kolom", "Keduanya berupa matriks persegi"], "answer": "Memiliki ordo yang sama"},
        {"q": "3. Jika A = [[5, 7], [2, 9]] dan B = [[3, 2], [1, 4]], maka hasil A - B adalah...", "options": ["[[8, 9], [3, 13]]", "[[2, 5], [1, 5]]", "[[2, 5], [1, -5]]", "[[15, 14], [2, 36]]"], "answer": "[[2, 5], [1, 5]]"},
        {"q": "4. Jika k = 3 dan A = [[2, -1], [4, 0]], maka nilai dari kA adalah...", "options": ["[[6, -3], [12, 0]]", "[[5, 2], [7, 3]]", "[[6, -1], [12, 0]]", "[[2, -3], [4, 0]]"], "answer": "[[6, -3], [12, 0]]"},
        {"q": "5. Syarat dua matriks A (ordo m x n) dan B (ordo p x q) dapat dikalikan (A x B) adalah...", "options": ["m = p", "n = p", "n = q", "m = q"], "answer": "n = p"},
        {"q": "6. Jika A berordo 2x3 dan B berordo 3x4, maka hasil kali matriks A x B akan menghasilkan matriks berordo...", "options": ["2x3", "3x3", "2x4", "3x2"], "answer": "2x4"},
        {"q": "7. Diketahui A = [[1, 2], [3, 4]] dan B = [[1, 0], [0, 1]]. Hasil A x B adalah...", "options": ["[[1, 0], [0, 4]]", "[[1, 2], [3, 4]]", "[[2, 2], [3, 5]]", "[[0, 0], [0, 0]]"], "answer": "[[1, 2], [3, 4]]"},
        {"q": "8. Matriks B = [[1, 0], [0, 1]] pada soal nomor 7 dinamakan matriks...", "options": ["Nol", "Identitas", "Diagonalkan", "Skalar"], "answer": "Identitas"},
        {"q": "9. Jika A = [[1, 2], [0, 1]] dan B = [[2, 0], [1, 3]], elemen baris 1 kolom 1 dari A x B adalah...", "options": ["4", "2", "3", "1"], "answer": "4"},
        {"q": "10. Sifat perpangkatan/perkalian matriks pada umumnya adalah TIDAK komutatif, artinya...", "options": ["A + B ≠ B + A", "A x B ≠ B x A", "A - B = B - A", "kA ≠ Ak"], "answer": "A x B ≠ B x A"},
        {"q": "11. Diketahui A = [[2, 1], [0, 3]]. Nilai A² (yaitu A x A) adalah...", "options": ["[[4, 1], [0, 9]]", "[[4, 5], [0, 9]]", "[[4, 3], [0, 9]]", "[[2, 2], [0, 6]]"], "answer": "[[4, 5], [0, 9]]"},
        {"q": "12. Jika A = [[x, 4], [2, 1]] + [[3, 1], [1, 2]] = [[7, 5], [3, 3]], maka nilai x adalah...", "options": ["2", "3", "4", "5"], "answer": "4"},
        {"q": "13. Transpose dari matriks P = [[1, 3], [2, 4]] adalah Pᵀ = ...", "options": ["[[1, 2], [3, 4]]", "[[4, 3], [2, 1]]", "[[1, 3], [2, 4]]", "[[3, 1], [4, 2]]"], "answer": "[[1, 2], [3, 4]]"},
        {"q": "14. Jika A = [[2, 0], [0, 2]], maka 2A - A sama dengan...", "options": ["A", "2A", "Matriks Nol", "Matriks Identitas"], "answer": "A"},
        {"q": "15. Dalam kehidupan sehari-hari, operasi perkalian matriks sangat berguna untuk...", "options": ["Menghitung total tagihan belanja barang dengan variasi harga", "Membagi kue sama rata", "Mengukur panjang jalan raya", "Menentukan jam keberangkatan bus"], "answer": "Menghitung total tagihan belanja barang dengan variasi harga"}
    ]

    with st.form("quiz_matriks_form"):
        user_answers = []
        for i, q in enumerate(questions):
            st.markdown(f"**{q['q']}**")
            ans = st.radio(f"Pilih jawaban nomor {i+1}:", q["options"], key=f"q_mat_{i}", index=None)
            user_answers.append(ans)
            st.write("")

        submitted = st.form_submit_button("Kirim Jawaban & Hitung XP 🏆")

    if submitted:
        score_counter = 0
        unanswered = False

        for i, q in enumerate(questions):
            if user_answers[i] is None:
                unanswered = True
            elif user_answers[i] == q["answer"]:
                score_counter += 10

        if unanswered:
            st.warning("Harap jawab semua 15 pertanyaan terlebih dahulu!")
        else:
            st.session_state.score_mat = score_counter
            update_badge_mat()

            st.balloons()
            st.success(f"🎉 Kuis Selesai! Skor Anda: **{st.session_state.score_mat} / 150 XP**")
            st.info(f"Gelar Anda saat ini: **{st.session_state.badge_mat}**")

            recap_data = {
                "No": [i+1 for i in range(15)],
                "Jawaban Anda": user_answers,
                "Jawaban Benar": [q["answer"] for q in questions],
                "Status": ["✅ Benar" if user_answers[i] == questions[i]["answer"] else "❌ Salah" for i in range(15)]
            }
            df_recap = pd.DataFrame(recap_data)
            st.subheader("📊 Rekapitulasi Hasil Jawaban")
            st.dataframe(df_recap, use_container_width=True, hide_index=True)
