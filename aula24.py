lista = ['Maria', 'Helena', 'Luiz']
lista.append('Raul')


lista_enumerada = enumerate(lista)
# print(next(lista_enumerada))
# print(next(lista_enumerada))
# print(next(lista_enumerada))
# print(next(lista_enumerada))

for item, nome in lista_enumerada:
    print(item, nome)
