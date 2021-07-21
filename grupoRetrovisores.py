import re


text = '<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div>oi</div>'


print(re.findall(r'(<([dpiv]{1,3})>.+?<\/\2>)', text))


cpf = '132.323.232-54'

print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))

print(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'\1 MAIS \3 COISAS \4', text))