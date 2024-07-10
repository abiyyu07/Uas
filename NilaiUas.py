import streamlit as st

def categorize_score(score):
    if score <= 40:
        return "Nilai Rendah"
    elif 41 <= score <= 70:
        return "Nilai Sedang"
    else:
        return "Nilai Tinggi"

def main():
    st.title("Kategori Penilaian Siswa")

    # Input: Get the student's daily score
    score = st.number_input("Masukkan jumlah poin yang diperoleh siswa dalam sehari:", min_value=0)

    # Determine the category based on the score
    category = categorize_score(score)

    # Output: Display the category
    st.write("Kategori nilai: ", category)

if __name__ == "__main__":
    main()
