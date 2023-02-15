# variaveis

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
     print(f'Seu nome é: {nome}') 
     print(f'Seu nome invertido é: {nome[::-1]}')
     print(f'Seu nome contem espaços: {nome.isspace()}')   
     print(f'Seu nome possui {len(nome)} letras')
     print(f'A primeira letra do seu nome é: {nome[:1]}')
     print(f'A última letra do seu nome é: {nome[-1]}')
      
else:
    print('Desculpe, voce deixou esses campos vazios.')