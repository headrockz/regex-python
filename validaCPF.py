import re


cpf = '025.025.054-76'
cpf_regex = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')

# print(cpf_regex.search(cpf))
