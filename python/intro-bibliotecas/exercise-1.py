paises = input("escribi una lista de paises separados por comas:")
paises = paises.split(",")
print(sorted(set(paises)))
