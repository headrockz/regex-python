import re


text = '<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div></div>'


print(re.findall(r'<[pdiv]{1,3}>.*<\/[pdiv]{1,3}>', text))
print(re.findall(r'<[pdiv]{1,3}>.*?<\/[pdiv]{1,3}>', text))
print(re.findall(r'<[pdiv]{1,3}>.+?<\/[pdiv]{1,3}>', text))