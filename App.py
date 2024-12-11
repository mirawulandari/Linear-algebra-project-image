import streamlit as st
from PIL import Image, ImageFilter
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
        ["Blur", "Grayscale", "Contour"]
    )

    # Terapkan efek
    if option == "Blur":
        processed_image = image.filter(ImageFilter.BLUR)
    elif option == "Grayscale":
        processed_image = image.convert("L")
    elif option == "Contour":
        processed_image = image.filter(ImageFilter.CONTOUR)

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
