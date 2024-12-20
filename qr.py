import qrcode
import qrcode.constants

#Data to be encoded in the QRcode
data = "www.google.com"

#create a QRCode instance

qr = qrcode.QRCode(
    version= 1, #controls the size of the QR code (1 is the smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_L, #controls error correction level
    box_size = 10,#size of the each box (pixels)
    border = 10,#size of border (boxes)
)
#Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

#creating an image from the QR code
img = qr.make_image(fill = 'red' , back_color = 'White')

# save the image
img.save("qrcode_example.png")

#Display the image
img.show()