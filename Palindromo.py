# Función que reciba un string y retorne True si es un palíndromo (esto es, si se lee igual de izquierda a
# derecha o de derecha a izquierda), False en caso contrario. Utilizar esta función en un programa que
# permita al usuario ingresar palabras hasta que ingrese la palabra “fin” (suponer que todas las
# palabras son en minúsculas o todas en mayúsculas, de forma consistente).


def palindromo(cadena):
    if len(cadena) == 1:
        print("Es un palindromo")
        return True
    else:
        nueva = ""
        i = len(cadena) - 1
        while i >= 0:
            nueva = nueva + cadena[i]
            i = i - 1
        if cadena == nueva:
            print("Es un palindromo")
            return True
        else:
            print("No es un palindromo")
            return False


print(
    "__________COMPROBACIÓN DE PALÍNDROMOS__________\nComprueba si la palabra introducida es un "
    "palíndromo.\nPara salir del programa escribe 'fin' sin comillas\n")
contador = 0
cadena = input("Cadena: ")
while cadena != "fin":
    if palindromo(cadena):
        contador = contador + 1
    cadena = input("Cadena: ")
print(f"Cantidad de palindromos: {contador}")
