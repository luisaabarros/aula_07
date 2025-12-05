lista_numeros = []

for n in range(5):
    num = float(input('Informe o numero: '))
    lista_numeros.append(num)


print(lista_numeros[0])

lista_numeros[0] = 22 # Altera o valor do índice 0
lista_numeros.pop(-2)  # Deleta o último
lista_numeros.remove(30) # Deleta pelo valor
del lista_numeros[0]
print(lista_numeros)