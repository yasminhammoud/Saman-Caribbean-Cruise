from Restaurant import Restaurant

class Combo(Restaurant):

    def __init__(self, name, price, comboProducts):
        super().__init__(name, price)
        self.comboProducts = comboProducts
#REVIEW      
    def showInformation(self):
        print(f"\nNombre del combo: {self.name} \nPrecio: {self.price}")
        products_combo = ', '.join(self.comboProducts)
        print(f"Productos del combo: {products_combo}")

    def setCombo(self):

        while True: 
            try:
                change_combo = int(input("\n¿Qué desea cambiar de la información del combo? \n1.Nombre \n2.Clase de alimento \n3.Precio \n>>> "))
                if change_combo not in range(1,4):
                    raise ValueError
                break 
            except ValueError:
                print("Error: El dato ingresado no forma parte de las opciones")

        if change_combo == 1:

            self.name = input("Ingrese el nuevo nombre: ")
            while not (self.name).isalpha():
                self.name = input("Ingrese un nombre válido sin espacios: ")

        elif change_combo == 2:

            while True: 
                try:
                    products_amount = int(input("\nIngrese la cantidad de productos que tendrá el combo (min: 2 y max: 10): "))
                    if products_amount not in range(2,10):
                        raise ValueError
                    break 
                except ValueError as identifier:
                    print("Error: Dato ingresado no es válido")

            print("\nIngrese un solo producto a medida que le vaya preguntando el sistema")
            for i in range(products_amount):
                combo_product = input("Ingrese el nombre del producto: ")
                self.comboProducts.append(combo_product)
        
        elif change_combo == 3:

            while True:
                try: 
                    self.price = float(input("Ingrese el nuevo precio: "))
                    if self.price<0:
                        raise ValueError
                    break 
                except ValueError:
                    print("\nError: Dato inválido\n")
            
            self.price = self.price*1.16
    

