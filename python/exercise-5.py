def bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 !=0) or (anio % 400 == 0):
        return "Es anio bisiesto"
    else:
        return "No es anio bisiesto"
    
print(bisiesto(2010))