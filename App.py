import streamlit as st
from PIL import Image, ImageOps, ImageFilter
import io

st.title("Aplikasi Pemrosesan Gambar")
st.write("Unggah gambar Anda dan pilih efek pemrosesan yang diinginkan.")

# Upload file gambar
uploaded_file = st.file_uploader("Unggah gambar Anda", type=["jpg", "png", "jpeg"])
if uploaded_file:
    # Membuka gambar
    image = Image.open(uploaded_file)
    st.image(image, caption="Gambar Asli", use_column_width=True)

    # Pilihan efek pemrosesan
    option = st.selectbox(
        "Pilih efek gambar:",
        ["Rotasi", "Translasi", "Skala", "Distorsi"]
    )

    # Terapkan efek
    if option == "Rotasi":
        angle = st.slider("Pilih Sudut Rotasi", -180, 180, 90)
        processed_image = image.rotate(angle)

    elif option == "Translasi":
        # Menambahkan input untuk translasi (pergeseran)
        x_shift = st.slider("Pergeseran horizontal", -30, 30, 0)
        y_shift = st.slider("Pergeseran vertikal", -30, 30, 0)
        processed_image = ImageOps.offset(image, x_shift, y_shift)

    elif option == "Skala":
        # Mengatur faktor skala
        scale_factor = st.slider("Faktor Skala", 0.1, 3.0, 1.0)
        width, height = image.size
        new_size = (int(width * scale_factor), int(height * scale_factor))
        processed_image = image.resize(new_size)

    elif option == "Distorsi":
        # Distorsi menggunakan efek filter
        processed_image = image.filter(ImageFilter.GaussianBlur(5))

    # Tampilkan hasil
    st.image(processed_image, caption="Gambar Diproses", use_column_width=True)

    # Konversi gambar ke format byte untuk unduhan
    buf = io.BytesIO()
    processed_image.save(buf, format="PNG")
    byte_im = buf.getvalue()

    # Tombol unduh
    st.download_button(
        label="Unduh Gambar",
        data=byte_im,
        file_name="processed_image.png",
        mime="image/png"
    )
else:
    st.warning("Harap unggah gambar terlebih dahulu!")
