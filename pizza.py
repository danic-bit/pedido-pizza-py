from ingredientes import *
import time

class Pizza():
    tamanio = "familiar"
    precio = 10000
    resumen_pedido = []

    @staticmethod
    def validar_elemento(elemento,lista):
        return elemento.lower() in lista #si lo encuentra, el return es True. Se le agrega .lower() al elemento para que lo que se ingrese lo muestre en minuscula (tambien puede colocarse en el input) 


    def pedir(self):

        self.proteina = input ('''Ingrese la proteina deseada. Las opciones son:
        -Pollo
        -Vacuno
        -Carne vegetal
        >''').lower()

        self.vegetal1 = input ('''Ingrese el vegetal 1. Las opciones son:
        -Tomate
        -Aceitunas
        -Champinones
        >''').lower()

        self.vegetal2 = input ('''Ingrese el vegetal 1. Las opciones son:
        -Tomate
        -Aceitunas
        -Champinones
        >''').lower()

        self.masa = input ('''Ingrese la masa. Las opciones son:
        -Tradicional
        -Delgada
        >''').lower()

# se procede a la validacion del los input, llamando al metodo estatico validar_elemento
        self.pizza_valida = self.validar_elemento(self.proteina, proteinas) and \
            self.validar_elemento(self.vegetal1, vegetales) and \
            self.validar_elemento(self.vegetal2, vegetales) and \
            self.validar_elemento(self.masa, masas)
            #si todas son verdaderas, retornara True

    def mostrar_resumen(self):
        if self.pizza_valida: 
            print(f"___Resumen del pedido___ \n Los ingredientes de su pizza son: \n Masa = {self.masa} \n Proteina = {self.proteina} \n Vegetal 1 = {self.vegetal1}, \n Vegetal 2 = {self.vegetal2}, ")
        else:
            print("Error en ingreso de ingredientes. Intente nuevamente")
            time.sleep(1)
            self.pedir()
