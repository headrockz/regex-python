import re 


text = '''
131.768.460-53 DFD
055.123.060-50
955.123.060-90
'''


print(re.findall(r'\d{3}\.\d{3}\.\d{2}', text, flags=re.MULTILINE))