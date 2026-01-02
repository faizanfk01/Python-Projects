import qrcode

qr = qrcode.QRCode(version = 1,
                   error_correction = qrcode.ERROR_CORRECT_H,
                   box_size = 10, border = 4)

url = "https://example.com"

qr.add_data(url)
qr.make(fit = True)
image = qr.make_image(fill_color = "black", back_color = "white")

image.save("qrcode.png")