numeros = [1, 2, 3, 4, 5]

#1 quadrado de cada numero

numeros_quadrado =[]

for i in numeros:
    numeros_quadrado.append(i*2)

print(numeros_quadrado)

#2 soma dos numeros pares
soma_par = 0
for num in numeros:
    if (num % 2) == 0:
        soma_par += num

print(soma_par)

#3 dicionario

lista_adicional = []

for num in numeros:
    lista_adicional.append(num * num)

for num in numeros:
    lista_adicional.append(num)
print(numeros)