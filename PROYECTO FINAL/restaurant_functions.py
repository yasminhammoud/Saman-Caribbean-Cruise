#REVIEW 
from Dish import Dish
from Drink import Drink
from Combo import Combo 
import pickle

def file_existence(file_name):
    """[Verifica si el archivo existe o no]

    Returns:
        [bool]: [Dependiendo de la existencia del archivo]
    """
    try: 
        with open(file_name) as f:
            return True
    except FileNotFoundError as e:
        return False 

def product_name():
    """[Verifica si un nombre es válido o existente]

    Returns:
        [str]: [Nombre del producto/combo]
    """
    name = input("Ingrese el nombre: ")
    while not name.isalpha():
        name = input("Ingrese un nombre válido sin espacios: ")
    return name 

def product_price():
    """[Verifica si el precio introducido es válido]

    Returns:
        [float]: [Precio del producto/combo con IVA incluida]
    """
    while True:
        try: 
            price = float(input("Ingrese el precio: "))
            if price<0:
                raise ValueError
            break 
        except ValueError:
            print("\nError: Dato inválido\n")
    price = price*1.16
    return price

def add_product_combo():
    """[Agregar combo o producto como objetos y con sus atributos en su archivo de texto respectivo ]
    """

    products_menu = []
    combos_menu = []

    while True:
        try:
            type_food = int(input("\n¿Qué quiere agregar al menú? \n1. Alimento \n2. Bebida \n3. Combo \n>>> ")) 
            if type_food not in range(1,4):
                raise ValueError
            break 
        except ValueError:
            print("\nError: Dato ingresado no forma parte de las opciones dadas")

    if type_food==1:

        name_dish = product_name()

        if file_existence("products_information.txt"):
            with open("products_information.txt", 'rb') as f:
                saved_products_list = pickle.load(f)
            for product in saved_products_list:
                while (product.name) == name_dish:
                    print("ERROR: El nombre introducido ya existe")
                    name_dish = product_name()

        while True: 
            try:
                type_dish = int(input("\n¿Qué clase de alimento es? \n1.De empaque \n2.De preparación \n>>> "))
                if type_dish not in range(1,3):
                    raise ValueError
                break 
            except ValueError:
                print("\nError: ¡Dato inválido!\n")
        
        dish_price = product_price()

        if type_dish==1:
            type_dish = 'de empaque'
        elif type_dish==2:
            type_dish = 'de preparación'
        
        product = Dish(name_dish, dish_price, type_dish)
        products_menu.append(product)
        print("\n¡Alimento registrado exitosamente!")

    elif type_food==2:

        name_drink = product_name()

        if file_existence("products_information.txt"):
            with open("products_information.txt", 'rb') as f:
                saved_products_list = pickle.load(f)
            for product in saved_products_list:
                while (product.name) == name_drink:
                    print("ERROR: El nombre introducido ya existe")
                    name_drink = product_name()

        while True:
            try: 
                size_drink = int(input("\n¿Cuál es el tamaño de la bebida? \n1.Pequeño \n2.Mediano \n3.Grande \n>>> "))
                if size_drink not in range(1,4):
                    raise ValueError
                break 
            except ValueError:
                print("\nError: ¡Dato inválido!\n")
        
        drink_price = product_price()

        if size_drink==1:
            drink_size = 'pequeño'
        elif size_drink==2:
            drink_size = 'mediano'
        elif size_drink==3:
            drink_size = 'grande'
        
        product = Drink(name_drink, drink_price, drink_size)
        products_menu.append(product)
        print("\n¡Bebida registrada exitosamente!")

    elif type_food==3:
        
        name_combo = input("Ingrese el nombre del combo: ")

        if file_existence("combos_information.txt"):
            with open("combos_information.txt", 'rb') as f:
                saved_combos_list = pickle.load(f)
            for combo in saved_combos_list:
                while (combo.name) == name_combo:
                    print("ERROR: El nombre introducido ya existe")
                    name_combo = input("Ingrese el nombre del combo: ")
        
        combo_products = []

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
            combo_products.append(combo_product)

        price_combo = product_price()

        combo = Combo(name_combo, price_combo, combo_products)
        combos_menu.append(combo)
        print("\n¡Combo registrado exitosamente!")

        if file_existence("combos_information.txt"):

            with open("combos_information.txt", 'rb') as f:
                saved_combos = pickle.load(f)
            for combo in combos_menu:
                saved_combos.append(combo)
            with open("combos_information.txt", 'wb') as file:
                pickle.dump(saved_combos, file)

        elif not file_existence("combos_information.txt"):
            with open("combos_information.txt", 'wb') as file:
                pickle.dump(combos_menu, file)

    if file_existence("products_information.txt"):

        with open("products_information.txt", 'rb') as f:
            saved_products = pickle.load(f)
        for product in products_menu:
            saved_products.append(product)
        with open("products_information.txt", 'wb') as file:
            pickle.dump(saved_products, file)
            
    elif not file_existence("products_information.txt"):
        with open("products_information.txt", 'wb') as file:
            pickle.dump(products_menu, file)

def binary_search_name(product_list, product):
    """[Verifica si un producto o combo se encuentra en la lista introducida]

    Args:
        product_list ([list]): [Lista del producto/combo]
        product ([str]): [Nombre del producto/combo]

    Returns:
        [None o impresión]
    """
    product_list.sort(key = lambda product: product.name) 

    first = 0 
    last = len(product_list)-1
    index = -1 
    while (first <= last) and (index == -1):
        mid = (first+last)//2 
        if (product_list[mid]).name == product:
            return (product_list[mid])
        else: 
            if product < (product_list[mid]).name:
                last = mid-1
            else: 
                first = mid+1
    return print('¡Resultado no encontrado!') 

def remove_product_combo(product_to_remove):
    """[Elimina el producto/combo introducido si se encuentra en el archivo de texto]

    Args:
        product_to_remove ([int]): [Producto/combo que se desea eliminar]
    """
    if product_to_remove==1:

        if file_existence("products_information.txt"):
            
            with open("products_information.txt", 'rb') as f:
                products_menu = pickle.load(f)

            if len(products_menu)>0:
                name_product = product_name()
                found_product = binary_search_name(products_menu, name_product)
                if found_product is not None:
                    products_menu.remove(found_product) 
                    print("\nProducto eliminado")
                
                with open("products_information.txt", 'wb') as file:
                    pickle.dump(products_menu, file)

            else:
                print("No hay productos registrados")
        
        else:
            print("No hay productos registrados")

    elif product_to_remove==2:

        if file_existence("combos_information.txt"):

            if len(combos_menu)>0:
                name_product = input("Ingrese el nombre del combo: ")
                found_combo = binary_search_name(combos_menu, name_product)
                if found_combo is not None:
                    combos_menu.remove(found_combo)
                    print("Combo eliminado")
                
                with open("combos_information.txt", 'wb') as file:
                    pickle.dump(combos_menu, file)

            else:
                print("No hay combos registrados")
        else:
                print("No hay combos registrados")
    
def change_product_combo(product_to_change):
    """[Cambia algún dato del producto/combo introducido]

    Args:
        product_to_change ([int]): [Producto/combo por cambiar]
    """

    if product_to_change==1:

        if file_existence("products_information.txt"):

            with open("products_information.txt", 'rb') as f:
                products_menu = pickle.load(f)
            
            name_product_change = product_name()
            product_found = binary_search_name(products_menu, name_product_change)
            if product_found is not None:
                product_found.setProduct()
            
            with open("products_information.txt", 'wb') as file:
                pickle.dump(products_menu, file)

        else:
            print("No hay productos registrados")

    elif product_to_change==2:

        if file_existence("combos_information.txt"):

            with open("combos_information.txt", 'rb') as f:
                combos_menu = pickle.load(f)

            name_product_change = input("Ingrese el nombre del combo que va a cambiar: ")
            combo_found = binary_search_name(combos_menu, name_product_change)
            if combo_found is not None:
                combo_found.setCombo()

            with open("combos_information.txt", 'wb') as file:
                pickle.dump(combos_menu, file)
        else:
            print("No hay combos registrados")

def search_product_combo(product_to_search):
    """[Busca el producto/combro introducido en función su nombre]

    Args:
        product_to_search ([int]): [Producto/combo por buscar]
    """

    if product_to_search==1:
        
        if file_existence("products_information.txt"):

            with open("products_information.txt", 'rb') as f:
                products_menu = pickle.load(f)

            name_product = product_name()
            product_found = binary_search_name(products_menu, name_product)
            if product_found is not None:
                product_found.showInformation()
        
        else:
            print("No hay productos registrados")
    
    elif product_to_search==2:

        if file_existence("combos_information.txt"):

            with open("combos_information.txt", 'rb') as f:
                combos_menu = pickle.load(f)

            name_combo = input("Ingrese el nombre del combo que va a buscar: ")
            for combo in combos_menu:
                if combo.name == name_combo:
                    combo.showInformation()

        else:
            print("No hay combos registrados")

def search_price_product_combo(product_to_change): 
    """[Busca producto/combo dentro de un rango específico dado por el usuaria]

    Args:
        product_to_change ([int]): [Product/combo por buscar]

    """
    while True:
        try: 
            mini = float(input("Ingrese el mínimo del intervalo: "))
            if mini<0:
                raise ValueError
            maxi = float(input("Ingrese el máximo del intervalo: "))
            if maxi<0:
                raise ValueError
            break
        except ValueError:
            print("¡Dato inválido!")

    if product_to_change == 1:

        if file_existence("products_information.txt"):

            with open("products_information.txt", 'rb') as f:
                products_menu = pickle.load(f)
            range_products = [product for product in products_menu if mini <= product.price <= maxi]

            if len(range_products)>0:
                for product in range_products:
                    product.showInformation()
            else:
                print("No se encontraron productos")
        else:
            print("No hay productos registrados")

    elif product_to_change==2:
        
        if file_existence("combos_information.txt"):

            with open("combos_information.txt", 'rb') as f:
                combos_menu = pickle.load(f)
            range_combos = [combo for combo in combos_menu if mini <= combo.price <= maxi]

            if len(range_combos)>0:
                for combo in range_combos:
                    combo.showInformation()
            else:
                print("No se encontraron combos")
        
        else:
            print("No hay combos registrados")

def restaurant():
    """[Se encarga de operar todas las funciones disponibles para el menú del crucero]
    """

    print("\n¡Bienvenido al Restaurante del Saman Caribbean!")

    while True: 

        while True:
            try:
                menu_choice = int(input("\n¿Qué función quiere realizar en el menú? \n1. Agregar plato/combo \n2. Eliminar producto/combo \n3. Modificar producto \n4. Buscar producto/combo \n5. Salir \n>>> "))
                if menu_choice not in range(1,6):
                    raise ValueError
                break 
            except ValueError:
                print("\nError: Dato ingresado no forma parte de las opciones dadas\n")

        if menu_choice==1: 

            add_product_combo()

        elif menu_choice==2:

            while True:
                try:
                    product_to_remove = int(input("\n¿Qué desea eliminar del menú? \n1. Producto \n2. Combo \n>>> "))
                    if product_to_remove not in range(1,3):
                        raise ValueError
                    break 
                except ValueError:
                    print("\nError: Dato ingresado no forma parte de las opciones dadas\n")

            remove_product_combo(product_to_remove)
    
        elif menu_choice==3:

            while True:
                try:
                    product_to_change = int(input("\n¿Qué desea cambiar del menú? \n1. Producto \n2. Combo \n>>> "))
                    if product_to_change not in range(1,3):
                        raise ValueError
                    break 
                except ValueError:
                    print("\nError: Dato ingresado no forma parte de las opciones dadas\n")
            
            change_product_combo(product_to_change)

        elif menu_choice==4:

            while True:
                try:
                    product_to_search = int(input("\n¿Qué desea buscar del menú? \n1. Producto \n2. Combo \n>>> "))
                    if product_to_search not in range(1,3):
                        raise ValueError
                    way_to_search = int(input("\n¿Cómo desea buscar el producto/combo del menú? \n1.Por nombre \n2.Por rango de precio \n>>> "))
                    if way_to_search not in range(1,3):
                        raise ValueError
                    break 
                except ValueError:
                    print("\nError: Dato ingresado no forma parte de las opciones dadas\n")

            if way_to_search==1:
                found_products_combos = search_product_combo(product_to_search)

            elif way_to_search==2:
                found_products_combos = search_price_product_combo(product_to_search)

        else:
            print("¡Hasta luego!")
            break 
