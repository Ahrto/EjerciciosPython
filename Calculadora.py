# Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método
# __init__.
# Calcular después la suma, resta, multiplicación y división.
# Utilizar un método para cada una e imprimir los resultados obtenidos.
# Llamar a la clase Calculadora.

class Calculadora:
    def __init__(self):
        self.n1 = int(input("Número 1: "))
        self.n2 = int(input("Número 2: "))

    def suma(self):
        print("La suma de los números es: ", self.n1 + self.n2)

    def resta(self):
        print("La resta de los números es: ", self.n1 - self.n2)

    def multiplicacion(self):
        print("La multiplicacion de los números es: ", self.n1 * self.n2)

    def division(self):
        print("La division de los números es: ", self.n1 / self.n2)


calculadora = Calculadora()
calculadora.suma()
calculadora.resta()
calculadora.multiplicacion()
calculadora.division()
