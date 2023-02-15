def media_alunos(a):
    soma = 0
    notas_float = 0
    for i in range(a):
        notas = input('').split
        notas_float = for a in notas
        as1, as2, as3 = float(notas_float[0]), float(notas_float[1]), float_int(notas_float[2])
        soma = as1 + as2 + as3
        if soma >= 7:
            return f'O ALUNO {i} FOI APROVADO'
        else:
            return f'O ALUNO {i} FOI REPROVADO'
        
        i += 1

print(media_alunos(2))