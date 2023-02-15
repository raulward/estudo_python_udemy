# import random, sys, os    

# def gerador_cpf():
#     global nove_digitos
#     nove_digitos = ''
#     digito = 0
#     digito_str = ''

#     for i in range(9):
#         digito = random.randint(0, 9)
#         digito_str = str(digito)
#         nove_digitos += digito_str
#         i += 1

#     print(nove_digitos)



# def validador_cpf():    
#     contador_regressivo_1 = 10
#     resul_digito_1 = 0

#     for digito_1 in nove_digitos:
#         resul_digito_1 += int(digito_1) * contador_regressivo_1
#         contador_regressivo_1 -= 1


#     digito_1 = (resul_digito_1 * 10) % 11 
#     digito_1 = digito_1 if digito_1 <= 9 else 0

#     dez_digitos = nove_digitos + str(digito_1)
#     contandor_regressivo_2 = 11

#     resul_digito2 = 0
#     for digito_2 in dez_digitos:
#         resul_digito2 += int(digito_2) * contandor_regressivo_2
#         contandor_regressivo_2 -= 1

#     digito_2 = (resul_digito2 * 10) % 11
#     digito_2 = digito_2 if digito_2 <= 9 else 0 

#     os.system('cls')

#     cpf_valido = f'{nove_digitos}{digito_1}{digito_2}'

#     if nove_digitos == cpf_valido:
#         print(f'O cpf {nove_digitos} eh valido')
#     else:
#         print(f'O cpf {nove_digitos} eh invalido')


# def cpf():
#     escolha_usario = input('Para validar seu cpf, digite: 1, para gerar um cpf, digite: 2') 

#     if escolha_usario == '1':


#     gerador_cpf()
#     escolha_usario2 = input('Deseja validar o cpf gerado? [S]im ou [N]ao: ')
    
#     escolha_usario.upper()
    
#     if escolha_usario == 'S':
#         validador_cpf()
#     elif escolha_usario == 'N':
#         print(f'Obrigado! Seu cpf gerado foi {nove_digitos}')
#     else:
#         print('Por favor digite um comando valido.')        
            

# cpf()            