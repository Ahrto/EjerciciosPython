# Herencia
# Realizar un programa que conste de un clase Persona con dos atributos nombre y edad. Los atributos
# se introducirán por teclado y habrá otro método para imprimir los datos. Declarar una segunda clase
# llama Empleado que hereda de la clase Persona y agrega el atributo sueldo. Debe mostrar si tiene
# que pagar impuestos o no (sueldo superior a 3000).

# Clase Persona
class Persona:
    # Metodo para inicializar
    def __init__(self):
        self.nombre = input("Nombre: ")
        self.edad = int(input("Edad: "))

    def imprimir(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)

# Clase empleado que Hereda de Persona
class Empleado(Persona):
    # Metodo para inicializar
    def __init__(self):
        # Llamamos al metoso "init" de la clase padre
        # Utilizamos la funcion super() para hacer referencia al padre
        super().__init__()
        # Agregamos atributo sueldo
        self.sueldo = float(input("Sueldo del empleado: "))

    #Metodo para imprimir
    def imprimir(self):
        super().imprimir()
        print("El sueldo es de: ", self.sueldo)

    # Metodo para comprobar si debe de pagar impuestos
    def impuestos(self):
        if self.sueldo > 3000:
            print(f"El empleado {self.nombre} tiene que pagar impuestos")
        else:
            print(f"El empleado {self.nombre} no tiene que pagar impuestos")


# persona = Persona()
# persona.imprimir()
#
# empleado = Empleado()
# empleado.imprimir()
# empleado.impuestos()

