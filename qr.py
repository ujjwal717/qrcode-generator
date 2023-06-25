import qrcode

data = input("Enter the data whose qr code you want to generate :- ")

generated_image = qrcode.make(data)
type(generated_image)
generated_image.save("generated qr.png")