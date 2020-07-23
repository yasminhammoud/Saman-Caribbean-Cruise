from Restaurant import Restaurant

class Dish(Restaurant):

    def __init__(self, name, price, typeDish):
        super().__init__(name, price)
        self.typeDish = typeDish
    
    def showInformation(self):
        return print(f"\nNombre del alimento: {(self.name).capitalize()} \nTipo de alimento: {(self.typeDish).capitalize()} \nPrecio: {self.price}$")
    
    def setProduct(self):

        while True: 
            
            try:
                change_dish = int(input("\n¿Qué desea cambiar de la información del alimento? \n1.Nombre \n2.Clase de alimento \n3.Precio \n>>> "))
                if change_dish not in range(1,4):
                    raise ValueError
                break 
            except ValueError:
                print("Error: El dato ingresado no forma parte de las opciones")

        if change_dish == 1:

            self.name = input("Ingrese el nuevo nombre: ")
            while not (self.name).isalpha():
                self.name = input("Ingrese un nombre válido sin espacios: ")

        elif change_dish == 2:

            while True: 
                try:
                    self.typeDish = int(input("\n¿Qué clase de alimento es? \n1.De empaque \n2.De preparación \n>>> "))
                    if self.typeDish not in range(1,3):
                        raise ValueError
                    break 
                except ValueError:
                    print("\nError: ¡Dato inválido!\n")
        
        elif change_dish == 3:

            while True:
                try: 
                    self.price = float(input("Ingrese el nuevo precio: "))
                    if self.price<0:
                        raise ValueError
                    break 
                except ValueError:
                    print("\nError: Dato inválido\n")
            
            self.price = self.price*1.16
            