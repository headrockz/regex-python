import re

text = 'Este é um teste de oi expressoes regulares oi'
print(re.search(r'oi', text))
print(re.findall(r'oi', text))
print(re.sub(r'oi', 'ola', text))

regexp = re.compile(r'oi')
print(regexp.search(text))
print(regexp.findall(text))
print(regexp.sub('Hello', text))