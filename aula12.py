# Exercicio

primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite um outro valor: ')

if primeiro_valor > segundo_valor:
    print(
        f'O primeiro valor {primeiro_valor} é maior do que o segundo valor {segundo_valor}.')
elif segundo_valor > primeiro_valor:
    print(
        f'O segundo valor {segundo_valor} é maior do que o primeiro valor {primeiro_valor}.')
else:
    print(f'Os valores {primeiro_valor} e {segundo_valor} são iguais.')
