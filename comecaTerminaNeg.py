import re


cpf = '132.323.232-54'
# cpf = 'a 132.323.232-54 aaa'

print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', cpf))
print(re.findall(r'[^0-9]+', cpf))