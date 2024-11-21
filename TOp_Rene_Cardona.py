'''
A) Crea un programa que ante la introducción de un string únicamente numérico (incluyendo el símbolo menos(-)
puesto que forma parte de los elementos válidos de un entero), cree una variable de tipo entero (int) equivalente al
valor numérico de dicho string.
(P.e.  El string palabra="-1234"  devuelve el int numero=-1234)
'''

cadena1 = str(input("Ingresa un número entero (este puede ser positivo o negativo):"))
caracteres = len(cadena1)
contador = len(cadena1)
enterot = 0

while contador > 0:
    contador = contador - 1
    entero = (cadena1[(caracteres - 1) - contador])
    if entero == "1":
        entero1 = 1
        enterot = enterot + (entero1*10**contador)
    elif entero =="2":
        entero2 = 2
        enterot = enterot + (entero2*10**contador)
    elif entero =="3":
        entero3 = 3
        enterot = enterot + (entero3*10**contador)
    elif entero =="4":
        entero4 = 4
        enterot = enterot + (entero4*10**contador)
    elif entero =="5":
        entero5 = 5
        enterot = enterot + (entero5*10**contador)
    elif entero =="6":
        entero6 = 6
        enterot = enterot + (entero6*10**contador)
    elif entero =="7":
        entero7 = 7
        enterot = enterot + (entero7*10**contador)
    elif entero =="8":
        entero8 = 8
        enterot = enterot + (entero8*10**contador)
    elif entero =="9":
        entero9 = 9
        enterot = enterot + (entero9*10**contador)
if cadena1[0] == "-":
    enterot = -1 * enterot
print(enterot)