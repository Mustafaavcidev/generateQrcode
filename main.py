import pyqrcode

url = input("enter url : ")

url = pyqrcode.create(url)

url.svg('url.svg', scale=7)
