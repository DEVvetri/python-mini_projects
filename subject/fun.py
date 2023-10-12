import re
mail="vetrivelmpp004@gmial.com"
pattren=re.compile(r'([a-z0-9]+[.-_])*[a-z0-9]+@[a-z]')
if re.search(pattren,mail):
    print("ok")

else:
    print("not")
name="C3iududsd"
if name.isalpha():
    print("yes")

else:
    print("no")