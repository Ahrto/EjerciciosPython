from Herencia import Persona, Empleado
from Poo import Alumno

# print("\n____________Desde clase main____________")
#
# # Creacion de Alumno de la clase Poo
# alumno1 = Alumno()
# alumno2 = Alumno()
#
# # Inicializacion de la clase
# alumno1.inicializar(nombre=input("Introduce el nombre del alumno 1: "),
#                     nota=int(input("Introduce la nota del alumno 1: ")))
# alumno2.inicializar(nombre=input("Introduce el nombre del alumno 2: "),
#                     nota=int(input("Introduce la nota del alumno 2: ")))
#
# # Imprimir atributos
# alumno1.imprimir()
# alumno2.imprimir()
#
# # Mostrar resultados
# alumno1.resultado()
# alumno2.resultado()

print("\n____________Clase Persona/Empleado____________")
persona = Persona()
persona.imprimir()

empleado = Empleado()
empleado.imprimir()
empleado.impuestos()
