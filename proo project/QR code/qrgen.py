import pyqrcode
import png

context="https://mail.google.com"

link=pyqrcode.create(context)

link.png("mail.png",scale=10)