import qrcode

# 1. La dirección de tu menú (cuando lo subas a internet será tu link real)
# Por ahora usaremos la dirección local de tu computadora
url_menu = "https://menu-club-oficial.onrender.com/"

# 2. Configurar el diseño del QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# 3. Agregar el link
qr.add_data(url_menu)
qr.make(fit=True)

# 4. Crear la imagen (usando tus colores: Negro y Verde)
# Nota: "fill_color" es el color del QR, "back_color" el fondo
img = qr.make_image(fill_color="#121212", back_color="white")

# 5. Guardar el archivo
img.save("qr_menu_club-definitivo.png")

print("¡Éxito! El código QR se ha guardado como 'qr_menu_club.png'")