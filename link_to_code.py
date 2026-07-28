# qr code generator

import qrcode

data = input("enter the url of site :")  # name of url you want to make qrcode of

filename = input(
    "enter the name of file you want :"
)  # name of file where picture of qr will be stored
# WRITE ".PNG "ALONG WITH NAME
qr = qrcode.QRCode(box_size=10, border=5)
qr.add_data(data)

image = qr.make_image(fill_color="black", back_color="white")
image.save(filename)
print(f"QR CODE saved as {filename}")
