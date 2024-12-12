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
    st.image(image, caption="Gambar Asli", use_container_width=True)

    # Pilihan efek pemrosesan
    option = st.selectbox(
        "Pilih efek gambar:",
        ["Rotasi", "Translasi", "Skala", "Distorsi", "Kontur", "Greyscale"]
    )

    # Terapkan efek
    if option == "Rotasi":
        angle = st.slider("Pilih Sudut Rotasi (derajat)", -180, 180, 0)
        processed_image = image.rotate(angle)

    elif option == "Translasi":
        # Kontrol untuk translasi
        x_shift = st.slider("Geser Horizontal (px)", -500, 500, 0)
        y_shift = st.slider("Geser Vertikal (px)", -500, 500, 0)
        # Translasi menggunakan transformasi afine
        processed_image = image.transform(
            image.size,
            Image.AFFINE,
            (1, 0, x_shift, 0, 1, y_shift),
            resample=Image.NEAREST
        )

    elif option == "Skala":
        # Kontrol untuk skala
        scale_factor = st.slider("Faktor Skala", 0.1, 3.0, 1.0)
        width, height = image.size
        new_size = (int(width * scale_factor), int(height * scale_factor))
        processed_image = image.resize(new_size)

    elif option == "Distorsi":
        # Kontrol untuk tingkat distorsi
        blur_radius = st.slider("Tingkat Blur (radius)", 0, 10, 5)
        processed_image = image.filter(ImageFilter.GaussianBlur(blur_radius))

    elif option == "Kontur":
        # Efek Kontur menggunakan ImageFilter.CONTOUR
        processed_image = image.filter(ImageFilter.CONTOUR)

    elif option == "Greyscale":
        # Efek Greyscale untuk mengubah gambar menjadi hitam-putih
        processed_image = image.convert("L")

    # Tampilkan hasil
    st.image(processed_image, caption="Gambar Diproses", use_container_width=True)

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
