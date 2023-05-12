from functools import reduce

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_filtrada = filter(lambda x: x % 2 == 1, lista)

suma = reduce(lambda a, b: a + b, lista_filtrada)

print(suma)
