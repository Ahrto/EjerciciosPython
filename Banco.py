# En un banco tienen clientes que pueden hacer depósitos y extracciones de dinero.
# -El banco requiere también al final del día calcular la cantidad de dinero que se ha depositado.
# -Se deberán crear dos clases, la clase cliente y la clase banco. La clase cliente tendrá los atributos
# nombre y cantidad y los métodos __ init __, depositar, extraer, mostrar_total
# -La clase banco tendrá como atributos 3 objetos de la clase cliente y los métodos __ init __, operar y
# deposito_total

# Clase Banco
def opciones():
    opcion = int(input("1-\n2-\n3-\n4-\n"))
    if opcion == 1:
        print("Opcion 1")
        return 1
    if opcion == 2:
        print("Opcion 2")
        return 2
    if opcion == 3:
        print("Opcion 3")
        return 3
    if opcion == 4:
        print("Opcion 4")
        return 4


class Banco:
    def __init__(self):
        self.cliente1 = Cliente("Alberto")
        self.cliente2 = Cliente("Pepe")
        self.cliente3 = Cliente("Lola")

    def operacion(self):
        print("______Operaciones______")
        print("--Depositos")
        self.cliente1.depositar(1000)
        self.cliente2.depositar(300)
        self.cliente3.depositar(43)
        self.cliente2.depositar(300)
        self.cliente3.depositar(800)
        print("--Extractos")
        self.cliente1.extraer(100)
        self.cliente2.extraer(100)
        self.cliente3.extraer(3)
        print("______Mostrar totales______")
        self.cliente1.mostrar_total()
        self.cliente2.mostrar_total()
        self.cliente3.mostrar_total()


# Clase Cliente
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cantidad = 0

    def depositar(self, deposito):
        print(f"{self.nombre} ha ingresado {deposito} €")
        self.cantidad = self.cantidad + deposito

    def extraer(self, resta):
        print(f"{self.nombre} ha extraido {resta} €")
        self.cantidad = self.cantidad - resta

    def mostrar_total(self):
        print(f"{self.nombre} tiene: {self.cantidad} €")


banco = Banco()
banco.operacion()
