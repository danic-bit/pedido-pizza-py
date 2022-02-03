from pizza import *

#a
"""print que muestre en pantalla los
valores de los atributos de clase de la clase importada, sin crear una
instancia de ella."""
print("Los valores de la clase importada son:", Pizza.tamanio, Pizza.precio)

#b
"""Usar la función print(), para que al ejecutar el script se muestre en pantalla
si el elemento “salsa de tomate” se encuentra presente en la lista [“salsa de
tomate", "salsa bbq"]. Para ello use el método creado en el requerimiento
2, sin crear una instancia de la clase importada."""

lista_salsas = ["salsa de tomate", "salsa bbq"]
print(Pizza.validar_elemento("salsa de tomate",lista_salsas))

#c
"""Crear una instancia de la clase importada, y luego llamar al método del
requerimiento 3 (pedir, es no estatico), para que al ejecutar el script se solicite ingredientes y tipo de
masa al usuario."""
pizza01 = Pizza()

pizza01.pedir()

#d
"""Usar la función print(), que muestre en pantalla los
ingredientes vegetales, el ingrediente proteico y el tipo de masa de la
instancia creada en el paso anterior, y si esa instancia es una pizza válida o
no."""

pizza01.mostrar_resumen()

#e
"""Usar la función print(), mostrar que: si la clase Pizza es una
pizza válida o no, haciendo uso del atributo pizza_valida, sin
crear una instancia de la clase. En este punto, la ejecución del script debe
mostrar un error (todos los pasos anteriores se deben haber ejecutado
correctamente)."""
#print(Pizza.validar_elemento(Pizza,lista_salsas)) # AttributeError: type object 'Pizza' has no attribute 'lower'

