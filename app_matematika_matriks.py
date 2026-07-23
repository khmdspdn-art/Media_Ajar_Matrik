import streamlit as st
import numpy as np
import pandas as pd

# -----------------------------------------------------------------------------
# KONFIGURASI HALAMAN
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Aplikasi Pembelajaran Matriks Interaktif",
    page_icon="🔢",
    layout="wide"
)

# Initialize Session State untuk Score & Badges
if "score_mat" not in st.session_state:
    st.session_state.score_mat = 0
if "badge_mat" not in st.session_state:
    st.session_state.badge_mat = "Pemula Matriks 🐣"

def update_badge_mat():
    score = st.session_state.score_mat
    if score >= 130:
        st.session_state.badge_mat = "Master Matriks 🏆"
    elif score >= 90:
        st.session_state.badge_mat = "Ahli Matriks 🥈"
    elif score >= 50:
        st.session_state.badge_mat = "Penjelajah Matriks 🥉"
    else:
        st.session_state.badge_mat = "Pemula Matriks 🐣"

# -----------------------------------------------------------------------------
# SIDEBAR NAVIGATION & PROFILE
# -----------------------------------------------------------------------------
st.sidebar.title("📌 Navigasi Modul")
menu = st.sidebar.radio(
    "Pilih Zona Pembelajaran:",
    [
        "📘 Modul Materi & Konsep",
        "🧮 Lab Simulasi Interaktif",
        "🎯 Kuis Evaluasi (15 Soal PG)"
    ]
)

st.sidebar.divider()
st.sidebar.subheader("👤 Profil Pembelajar")
st.sidebar.metric("Total Skor (XP)", f"{st.session_state.score_mat} / 150")
st.sidebar.info(f"Lencana: **{st.session_state.badge_mat}**")

# -----------------------------------------------------------------------------
# ZONA 1: MODUL MATERI & KONSEP
# -----------------------------------------------------------------------------
if menu == "📘 Modul Materi & Konsep":
    st.header("📘 Modul Operasi Matriks")
    st.write("Pelajari konsep dasar operasi matriks sebelum mencoba simulasi dan kuis!")

    tab1, tab2, tab3, tab4 = st.tabs([
        "1. Penjumlahan & Pengurangan",
        "2. Perkalian Skalar",
        "3. Perkalian Matriks",
        "4. Transpose & Sifat"
    ])

    with tab1:
        st.subheader("Penjumlahan dan Pengurangan Matriks")
        st.markdown("""
        Dua matriks dapat dijumlahkan atau dikurangi **hanya jika memiliki ordo (ukuran) yang sama**.
        Proses dilakukan dengan menjumlahkan/mengurangi elemen-elemen yang seletak.
        """)
        st.latex(r"""
        \begin{pmatrix} a & b \\ c & d \end{pmatrix} \pm \begin{pmatrix} e & f \\ g & h \end{pmatrix} 
        = \begin{pmatrix} a \pm e & b \pm f \\ c \pm g & d \pm h \end{pmatrix}
        """)

    with tab2:
        st.subheader("Perkalian Matriks dengan Skalar")
        st.markdown("""
        Perkalian skalar dilakukan dengan mengalikan sebuah bilangan real ($k$) ke **setiap elemen** di dalam matriks.
        """)
        st.latex(r"""
        k \times \begin{pmatrix} a & b \\ c & d \end{pmatrix} = \begin{pmatrix} k \cdot a & k \cdot b \\ k \cdot c & k \cdot d \end{pmatrix}
        """)

    with tab3:
        st.subheader("Perkalian Matriks dengan Matriks")
        st.markdown("""
        Syarat perkalian matriks $A \times B$: **Jumlah kolom matriks A harus sama dengan jumlah baris matriks B**.
        Perkalian dilakukan dengan mengalikan elemen **Baris pada Matriks A** dengan **Kolom pada Matriks B**.
        """)
        st.latex(r"""
        \begin{pmatrix} a & b \\ c & d \end{pmatrix} \times \begin{pmatrix} e & f \\ g & h \end{pmatrix}
        = \begin{pmatrix} (ae + bg) & (af + bh) \\ (ce + dg) & (cf + dh) \end{pmatrix}
        """)

    with tab4:
        st.subheader("Transpose Matriks")
        st.markdown("""
        Transpose matriks ($A^T$) dilakukan dengan **menukar posisi baris menjadi kolom** dan sebaliknya.
        """)
        st.latex(r"""
        A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \implies A^T = \begin{pmatrix} a & c \\ b & d \end{pmatrix}
        """)

# -----------------------------------------------------------------------------
# ZONA 2: LAB SIMULASI INTERAKTIF
# -----------------------------------------------------------------------------
elif menu == "🧮 Lab Simulasi Interaktif":
    st.header("🧮 Lab Simulasi Operasi Matriks Interaktif")
    st.write("Ubah nilai elemen matriks dan amati hasilnya secara langsung!")

    st.subheader("Input Elemen Matriks Ordo 2x2")
    col_a, col_b = st.columns(2)

    with col_a:
        st.markdown("**Matriks A**")
        a11 = st.number_input("A[1,1]", value=2, key="a11")
        a12 = st.number_input("A[1,2]", value=3, key="a12")
        a21 = st.number_input("A[2,1]", value=1, key="a21")
        a22 = st.number_input("A[2,2]", value=4, key="a22")
        A = np.array([[a11, a12], [a21, a22]])

    with col_b:
        st.markdown("**Matriks B**")
        b11 = st.number_input("B[1,1]", value=1, key="b11")
        b12 = st.number_input("B[1,2]", value=2, key="b12")
        b21 = st.number_input("B[2,1]", value=3, key="b21")
        b22 = st.number_input("B[2,2]", value=5, key="b22")
        B = np.array([[b11, b12], [b21, b22]])

    op = st.selectbox("Pilih Operasi Matriks:", ["Penjumlahan (A + B)", "Pengurangan (A - B)", "Perkalian Matriks (A x B)", "Perkalian Skalar (k x A)"])

    st.divider()
    st.subheader("Hasil Perhitungan & Tampilan Matriks")

    if op == "Penjumlahan (A + B)":
        C = A + B
        st.latex(rf"\begin{{pmatrix}} {a11} & {a12} \\ {a21} & {a22} \end{{pmatrix}} + \begin{{pmatrix}} {b11} & {b12} \\ {b21} & {b22} \end{{pmatrix}} = \begin{{pmatrix}} {C[0,0]} & {C[0,1]} \\ {C[1,0]} & {C[1,1]} \end{{pmatrix}}")
    elif op == "Pengurangan (A - B)":
        C = A - B
        st.latex(rf"\begin{{pmatrix}} {a11} & {a12} \\ {a21} & {a22} \end{{pmatrix}} - \begin{{pmatrix}} {b11} & {b12} \\ {b21} & {b22} \end{{pmatrix}} = \begin{{pmatrix}} {C[0,0]} & {C[0,1]} \\ {C[1,0]} & {C[1,1]} \end{{pmatrix}}")
    elif op == "Perkalian Matriks (A x B)":
        C = np.dot(A, B)
        st.latex(rf"\begin{{pmatrix}} {a11} & {a12} \\ {a21} & {a22} \end{{pmatrix}} \times \begin{{pmatrix}} {b11} & {b12} \\ {b21} & {b22} \end{{pmatrix}} = \begin{{pmatrix}} {C[0,0]} & {C[0,1]} \\ {C[1,0]} & {C[1,1]} \end{{pmatrix}}")
    elif op == "Perkalian Skalar (k x A)":
        k = st.slider("Pilih Nilai Skalar (k):", -10, 10, 3)
        C = k * A
        st.latex(rf"{k} \times \begin{{pmatrix}} {a11} & {a12} \\ {a21} & {a22} \end{{pmatrix}} = \begin{{pmatrix}} {C[0,0]} & {C[0,1]} \\ {C[1,0]} & {C[1,1]} \end{{pmatrix}}")

# -----------------------------------------------------------------------------
# ZONA 3: KUIS EVALUASI MATRIKS (SOAL BERFORMAT MATRIKS VISUAL)
# -----------------------------------------------------------------------------
elif menu == "🎯 Kuis Evaluasi (15 Soal PG)":
    st.header("🎯 Kuis Evaluasi Matriks (15 Soal PG)")
    st.write("Jawablah pertanyaan-pertanyaan berikut dengan memilih salah satu opsi jawaban yang benar!")

    questions = [
        {
            "q": "1. Hasil penjumlahan matriks berikut adalah:",
            "latex_expr": r"\begin{pmatrix} 2 & 3 \\ 1 & 4 \end{pmatrix} + \begin{pmatrix} 1 & 2 \\ 3 & 5 \end{pmatrix} = \dots",
            "options": ["\\begin{pmatrix} 3 & 5 \\ 4 & 9 \\end{pmatrix}", "\\begin{pmatrix} 1 & 1 \\ -2 & -1 \\end{pmatrix}", "\\begin{pmatrix} 2 & 6 \\ 3 & 20 \\end{pmatrix}", "\\begin{pmatrix} 3 & 1 \\ 4 & 9 \\end{pmatrix}"],
            "answer": "\\begin{pmatrix} 3 & 5 \\ 4 & 9 \\end{pmatrix}"
        },
        {
            "q": "2. Syarat utama dua buah matriks dapat dijumlahkan atau dikurangkan adalah...",
            "latex_expr": None,
            "options": ["Mempunyai determinan yang sama", "Memiliki ordo yang sama", "Jumlah baris lebih banyak dari kolom", "Keduanya berupa matriks persegi"],
            "answer": "Memiliki ordo yang sama"
        },
        {
            "q": "3. Hasil pengurangan matriks berikut adalah:",
            "latex_expr": r"\begin{pmatrix} 5 & 7 \\ 2 & 9 \end{pmatrix} - \begin{pmatrix} 3 & 2 \\ 1 & 4 \end{pmatrix} = \dots",
            "options": ["\\begin{pmatrix} 8 & 9 \\ 3 & 13 \\end{pmatrix}", "\\begin{pmatrix} 2 & 5 \\ 1 & 5 \\end{pmatrix}", "\\begin{pmatrix} 2 & 5 \\ 1 & -5 \\end{pmatrix}", "\\begin{pmatrix} 15 & 14 \\ 2 & 36 \\end{pmatrix}"],
            "answer": "\\begin{pmatrix} 2 & 5 \\ 1 & 5 \\end{pmatrix}"
        },
        {
            "q": "4. Jika k = 3, maka hasil perkalian skalar berikut adalah:",
            "latex_expr": r"3 \times \begin{pmatrix} 2 & -1 \\ 4 & 0 \end{pmatrix} = \dots",
            "options": ["\\begin{pmatrix} 6 & -3 \\ 12 & 0 \\end{pmatrix}", "\\begin{pmatrix} 5 & 2 \\ 7 & 3 \\end{pmatrix}", "\\begin{pmatrix} 6 & -1 \\ 12 & 0 \\end{pmatrix}", "\\begin{pmatrix} 2 & -3 \\ 4 & 0 \\end{pmatrix}"],
            "answer": "\\begin{pmatrix} 6 & -3 \\ 12 & 0 \\end{pmatrix}"
        },
        {
            "q": "5. Syarat dua matriks A (ordo m x n) dan B (ordo p x q) dapat dikalikan (A x B) adalah...",
            "latex_expr": None,
            "options": ["m = p", "n = p", "n = q", "m = q"],
            "answer": "n = p"
        },
        {
            "q": "6. Jika matriks A berordo 2x3 dan matriks B berordo 3x4, maka hasil kali matriks A x B akan menghasilkan matriks berordo...",
            "latex_expr": None,
            "options": ["2x3", "3x3", "2x4", "3x2"],
            "answer": "2x4"
        },
        {
            "q": "7. Hasil perkalian matriks dengan matriks identitas berikut adalah:",
            "latex_expr": r"\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \times \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = \dots",
            "options": ["\\begin{pmatrix} 1 & 0 \\ 0 & 4 \\end{pmatrix}", "\\begin{pmatrix} 1 & 2 \\ 3 & 4 \\end{pmatrix}", "\\begin{pmatrix} 2 & 2 \\ 3 & 5 \\end{pmatrix}", "\\begin{pmatrix} 0 & 0 \\ 0 & 0 \\end{pmatrix}"],
            "answer": "\\begin{pmatrix} 1 & 2 \\ 3 & 4 \\end{pmatrix}"
        },
        {
            "q": "8. Matriks berikut dinamakan sebagai matriks...",
            "latex_expr": r"I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}",
            "options": ["Nol", "Identitas", "Diagonalkan", "Skalar"],
            "answer": "Identitas"
        },
        {
            "q": "9. Berapakah elemen baris 1 kolom 1 dari hasil perkalian matriks berikut:",
            "latex_expr": r"\begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} \times \begin{pmatrix} 2 & 0 \\ 1 & 3 \end{pmatrix}",
            "options": ["4", "2", "3", "1"],
            "answer": "4"
        },
        {
            "q": "10. Sifat perkalian matriks pada umumnya adalah TIDAK komutatif, yang berarti...",
            "latex_expr": None,
            "options": ["A + B ≠ B + A", "A × B ≠ B × A", "A - B = B - A", "k A ≠ A k"],
            "answer": "A × B ≠ B × A"
        },
        {
            "q": "11. Tentukan hasil dari A² (yaitu A × A) jika diketahui:",
            "latex_expr": r"A = \begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix}",
            "options": ["\\begin{pmatrix} 4 & 1 \\ 0 & 9 \\end{pmatrix}", "\\begin{pmatrix} 4 & 5 \\ 0 & 9 \\end{pmatrix}", "\\begin{pmatrix} 4 & 3 \\ 0 & 9 \\end{pmatrix}", "\\begin{pmatrix} 2 & 2 \\ 0 & 6 \\end{pmatrix}"],
            "answer": "\\begin{pmatrix} 4 & 5 \\ 0 & 9 \\end{pmatrix}"
        },
        {
            "q": "12. Tentukan nilai x dari kesamaan matriks berikut:",
            "latex_expr": r"\begin{pmatrix} x & 4 \\ 2 & 1 \end{pmatrix} + \begin{pmatrix} 3 & 1 \\ 1 & 2 \end{pmatrix} = \begin{pmatrix} 7 & 5 \\ 3 & 3 \end{pmatrix}",
            "options": ["2", "3", "4", "5"],
            "answer": "4"
        },
        {
            "q": "13. Transpose dari matriks P berikut adalah:",
            "latex_expr": r"P = \begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix} \implies P^T = \dots",
            "options": ["\\begin{pmatrix} 1 & 2 \\ 3 & 4 \\end{pmatrix}", "\\begin{pmatrix} 4 & 3 \\ 2 & 1 \\end{pmatrix}", "\\begin{pmatrix} 1 & 3 \\ 2 & 4 \\end{pmatrix}", "\\begin{pmatrix} 3 & 1 \\ 4 & 2 \\end{pmatrix}"],
            "answer": "\\begin{pmatrix} 1 & 2 \\ 3 & 4 \\end{pmatrix}"
        },
        {
            "q": "14. Jika A adalah matriks ordo 2x2, maka bentuk (2A - A) akan menghasilkan matriks...",
            "latex_expr": None,
            "options": ["A", "2A", "Matriks Nol", "Matriks Identitas"],
            "answer": "A"
        },
        {
            "q": "15. Dalam kehidupan nyata, perkalian matriks sangat berguna untuk...",
            "latex_expr": None,
            "options": ["Menghitung total tagihan belanja barang dengan variasi harga", "Membagi kue sama rata", "Mengukur panjang jalan raya", "Menentukan jam keberangkatan bus"],
            "answer": "Menghitung total tagihan belanja barang dengan variasi harga"
        }
    ]

    with st.form("quiz_matriks_form"):
        user_answers = []
        for i, q in enumerate(questions):
            st.markdown(f"**{q['q']}**")
            
            # Tampilkan matriks asli jika ada
            if q["latex_expr"]:
                st.latex(q["latex_expr"])
                
            ans = st.radio(
                f"Pilih jawaban nomor {i+1}:",
                q["options"],
                key=f"q_mat_{i}",
                index=None
            )
            user_answers.append(ans)
            st.divider()

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
