import qrcode
qr=qrcode.QRCode()
a="95739706432-2ybl"
qr.add_data(a)
qr.make(fit=True)
res=qr.make_image(fill_colour="black",black_colour="white")
res.save("rajesh.png")
print("created Qr")