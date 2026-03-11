aluno = {"nome":"marcelo","idade":39,"nota":9}


# exercicio 1
print("ola " + aluno.get("nome") + " e nota: " + str(aluno.get("nota")))

# exercicio 2
aluno["estoque"]=15
print(aluno)

# exercicio 3

notas = {"Ana": 8, "Carlos": 6, "João": 9, "Maria": 7}

for aprovados, notas in notas.items():
    if notas == 7:
        print(aprovados, notas)

# exercicio 4

numeros = [1,2,3,4,5]
