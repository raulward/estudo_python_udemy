# def riscu(powerA, powerB):
#     if powerA > powerB:
#         print('Jogador A vence')
#     elif powerB > powerA:
#         print('Jogador B vence')
#     else:
#         print('Dois jogadores igualmente fracos')    

# def sedeDeMelancia(w):
#     resul = int(w / 2)
#     resul_checker = resul % 2 == 0
#     if resul_checker:
#          return 'SIM'
#     else: 
#         return 'NAO'   

# print(sedeDeMelancia(10))

# def qtdcopos(n):
#     n_checker = n % 4 == 0 and n != 0
#     n_fltm = n % 4
    
#     if n_checker:
#         print('Pode levar pros calourinhos, deivis!')
#     else:
#         print(f'Pode voltar pro ceubinho, deivis! Falta(m) {n_fltm} copo(s)!')

# print(qtdcopos(0)) 


# def maravilhosos(x):
#     while x != 1:     
#         if x % 2 and x != 0:
#             x = 3 * x + 1
#             print(x)   
#         else:
#             x / 2
#             print(x)
#     else:
#         print(x)            

# print(maravilhosos(7))

"""
def pitorestico(a, b, c):
    a_checker = int(a % 2 == 0)
    b_checker = int(b % 3 == 0)
    c_checker = int(c % 5 == 0)

    if a_checker and b_checker and c_checker:
        print('Pitorestico!!!')
    else:
        print('Nao foi dessa vez')"""


# def dinheiros(n, a, b): 
#     litros_a = 1
#     litros_b = 2

#     if n == 1:
     
#         print(a)
    
#     elif n > 1:
        
#         divisao = n // b
#         resto = n % b
        
#         if divisao != 0: 
#             total = a * resto + divisao
#             print(total)

def formamisteriosa(a = 2, b = 1, c = 1):
    if a != b:
        print('pode ser retangulo')
        if not ((a + b < c) or (a + c < b) or (b + c < a)):            
            if a==b and b==c :
                print('pode ser triangulo equilatero')
            elif (a==b) or (a==c) or (b==c):
                print('pode ser triangulo isosceles')
            else:
                print('pode ser triangulo escaleno')
    else:   
        print('pode ser quadrado')  
        if not (a + b < c) or (a + c < b) or (b + c < a):                
            if a==b and b==c :
                print('pode ser triangulo equilatero')
            elif (a==b) or (a==c) or (b==c):
                print('pode ser triangulo isosceles')
            else:
                print('pode ser triangulo escaleno')        

print(formamisteriosa())
