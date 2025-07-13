import qrcode

# Asking user to input the URL
url = input("Enter the URL to generate QR Code: ")

# Generating QR code
qr = qrcode.make(url)

# Saving the QR code as an image
qr.save("my_qrcode.png")

#Show the QR code
qr.show()
