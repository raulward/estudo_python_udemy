import os

# Implementar preco e categorias de produtos

lista_de_compra = []
indicie_int = 0
opcao = ''

while True:
    print('Selecione uma opcao: ')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        
        os.system('cls')

        lista_de_compra.append(input(''))
    
    elif opcao == 'a':

        os.system('cls')
        
        indice = input('Informe o indice do item que deseja apagar: ')
        
        indice_int = int(indice)
          
        del lista_de_compra[indice_int]    
   
    elif opcao == 'l':

        if len(lista_de_compra) == 0:
            
            print('Nada para listar')
        
        os.system('cls')
        
        for item, nome in enumerate(lista_de_compra):
            print(item, nome) 
    
    else:
        print('Por favor digite um comando valido')              