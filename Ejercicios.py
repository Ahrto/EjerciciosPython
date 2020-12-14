# Solicitar nombre y mostrar por pantalla
nombre = input("¿Cómo te llamas? ")
print("Hola", nombre)
#
# Multiplicar dos numeros
print("\nVamos a multiplicar dos números")
n1 = input("Introduce un primer número: ")
n2 = input("Introduce el segundo número: ")
print("El resultado de la multiplicacíon es:", int(n1) * int(n2))

# Solicita km recorridos y litros de combustible consumidos, programa muestra el consumo por km
print("\nVoy a calcular tu consumo de combustible")
km = float(input("Kilometros recorridos: "))
litros = float(input("Litros consumidos: "))
print("El consumo por kilómetro es de", km / litros)

# Condicionales Programa que solicita una letra, si es vocal muestra el mensaje "Es vocal". Verificar si el usuario
# ingreso un string de mas de un caracter y, en ese caso, informarle de que no se puede procesar el dato
print("\nIntroduce una letra y te diré si es una vocal")
letra = input("Letra: ")
if len(letra) != 1:
    print("Introduce SOLO una letra")
else:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u" or letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
        print("La letra introducida es una vocal")
    else:
        print("La letra es una consonante")

# Se pueden evaluar condiciones en el print()
# Introduce dos números, dice si es menor o mayor que 10
valor = int(input("\nIntroduce un número y te diré si es mayor o menor que 10: "))
print("Menor o igual que 10" if (valor < 10) else "Mayor o igual a 10")

# Bucle for
# Permite al usuario ingresar 6 numeros positivos o negativos.
# Muestra sumatoria de numeros negativos y promedio de positivos.
# No se puede dividir entre 0
print("\nIntroduce seis número (positivos o negativos), te daré la media de los positivos y la suma de los negativos")
positivos = 0
sumaPositivos = 0
negativos = 0
sumaNegativos = 0
for i in range(6):
    num = int(input("Número: "))
    if num >= 0:
        positivos = positivos + 1
        sumaPositivos = sumaPositivos + num
    else:
        negativos = negativos + 1
        sumaNegativos = sumaNegativos + num

if negativos != 0:
    print("La suma de los números negativos es: ", sumaNegativos)

if positivos != 0:
    print("La media de los números positivos es: ", sumaPositivos / positivos)

# While
# Programa que, dada una frase por el usuario, la muestre invertida
print("\nIntroduce una frase y la daré la vuelta")
frase = input("Frase: ")
nueva = ""
i = len(frase) - 1
while i >= 0:
    nueva = nueva + frase[i]
    i = i - 1
print(nueva)
