# Ejemplo de clase en Python
# Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y
# la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un
# mensaje con el resultado de la nota y si ha aprobado o no.

# Inicializamos la clase
class Alumno:
    # Inicializamos atributos
    def inicializar(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    # Funcion para imprimir los datos
    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Nota:", self.nota)

    # Funcion para obtener el resultado
    def resultado(self):
        if self.nota < 5:
            print(f"El alumno {self.nombre} ha suspendido")
        else:
            print(f"El alumno {self.nombre} ha aprobado")


# Bloque principal (tambien está importado en la clase main)
# Creacion de objetos Alumno
# alumno1 = Alumno()
# alumno2 = Alumno()
#
# # Inicializacion de los atributos
# alumno1.inicializar("Alberto", 10)
# alumno2.inicializar("Lola", 3)
#
# # Imprimir los datos
# alumno1.imprimir()
# alumno2.imprimir()
#
# # Mostrar resultados de las notas
# alumno1.resultado()
# alumno2.resultado()
