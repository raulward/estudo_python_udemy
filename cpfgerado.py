import random, sys

nove_digitos = ''
digito = 0
digito_str = ''

for i in range(9):
    digito = random.randint(0, 9)
    digito_str = str(digito)
    nove_digitos += digito_str
    i += 1

print(nove_digitos)