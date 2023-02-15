# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'

# if (entrada == 'E' or entrada) == 'e' and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')    

#  Avaliacao de curto circuito
# print(True and False and True)

print(True or 1 or False)
print(True or True or False)
print(True or True or True)
print(True or True or True)
print(False or False or False)

senha = input('Digite a senha: ') or 'Sem senha'
print(senha)