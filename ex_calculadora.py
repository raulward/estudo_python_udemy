""" Calculadora com while """

while True:   
    numero_1 = input('Digite um numero: ')
    numero_2 = input('Digite outro numero: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None
    
    num_1_float = 0
    num_2_float = 0
    resul = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os numeros sao invalidos') 
        continue   

    operadores_permitidos = '+/*-'

    if operador not in operadores_permitidos:
        print('Digite um operador valido.')

    if len(operador) > 1:
        print('Digite apenas um operador.')

    if operador == '+':
        resul = num_1_float + num_2_float
        print(f'O resultado da soma foi {resul}')
    elif operador == '-':
        resul = num_1_float - num_2_float
        print(f'O resultado da subtracao foi {resul}')
    elif operador == '*':
        resul = num_1_float * num_2_float    
        print(f'O resultado da multiplicacao foi {resul}')
    elif operador == '/':
        resul = num_1_float / num_2_float
        print(f'O resultado da divisao foi {resul}')                   

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break