from Restaurant import Restaurant

class Drink(Restaurant):

    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def showInformation(self):
        return print(f"\nNombre de la bebida: {(self.name).capitalize()} \nTamaño de la bebida: {(self.size).capitalize()} \nPrecio: {self.price}$")

    def setProduct(self):

        while True: 
            try:
                change_drink = int(input("¿Qué desea cambiar de la información del alimento? \n1.Nombre \n2.Clase de alimento \n3.Precio \n>>> "))
                if change_drink not in range(1,4):
                    raise ValueError
                break 
            except ValueError:
                print("Error: El dato ingresado no forma parte de las opciones")

        if change_drink == 1:

            self.name = input("Ingrese el nuevo nombre: ")
            while not (self.name).isalpha():
                self.name = input("Ingrese un nombre válido sin espacios: ")

        elif change_drink == 2:

            while True:
                try: 
                    self.size = int(input("\n¿Cuál es el tamaño de la bebida? \n1.Pequeño \n2.Mediano \n3.Grande \n>>> "))
                    if self.size not in range(1,4):
                        raise ValueError
                    break 
                except ValueError:
                    print("\nError: ¡Dato inválido!\n")
        
        elif change_drink == 3:

            while True:
                try: 
                    self.price = float(input("Ingrese el nuevo precio: "))
                    if self.price<0:
                        raise ValueError
                    break 
                except ValueError:
                    print("\nError: Dato inválido\n")
            
            self.price = self.price*1.16
