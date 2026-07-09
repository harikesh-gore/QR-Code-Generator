import qrcode

url =input("Enter Your url: ").strip()
file_path ="qrcode.png"

qr= qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

qr.add_data(url)
qr.make(fit=True)
img = qr.make_image()
img.save(file_path)

print("QR code was generated ")