lista = [12, 10, 7, 5]
lista_animal = ['cachorro','gato','elefante']

tupla = (1, 10, 12, 14,)
print(len(tupla))
print(len(lista_animal))
print(lista_animal[1])

lista.sort()
lista_animal.sort()
print(lista)
print(lista_animal)
lista_animal.reverse()
print(lista_animal)

if 'lobo' in lista_animal:
    print('existe um lobo na lista')
else:
    print('não existe um lobo na lista. Será incluido.')
    lista_animal.append('lobo')
    print(lista_animal)
lista_animal.pop(1)
print(lista_animal)
