from cruises_functions import save_ship_information
from Room import Room 
from Client import Client 
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

def save_rooms(ships):
    """[Almacena la información de cada piso de cada crucero en una lista de listas, y también crea las habitaciones de cada crucero como objeto, posteriormente todo es almacenado en archivos de texto]

    Args:
        ships ([list]): [Lista de los cruceros]
    """
    ships_rooms = []
    ships_floors = []
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T','U', 'V', 'W','X', 'Y', 'Z']
    room_types = ['simple', 'premium', 'vip']
    room_types_letter = ['S', 'P', 'V']
    room_information = ['Tiene servicio a la habitación', 'Posee vista al mar', 'Albergar fiestas privadas']
    for ship in ships:
        ship_floors = []
        ship_rooms = []
        for i in range(len(room_types)):
            room_type = room_types[i]
            floor = {(alphabet[i]): [(x+1) for x in range (ship.rooms[room_type][1])] for i in range(ship.rooms[room_type][0])}
            capacity = ship.roomCapacity[room_type]
            price = ship.roomPrice[room_type]
            information = room_information[i]
            type_letter = room_types_letter[i]
            for key in floor.keys():
                letter = key 
                for v in floor[key]:
                    number = str(v)
                    name = type_letter+letter+number
                    room = Room(room_type, letter, number, name , "", capacity, price, information, False)
                    ship_rooms.append(room)

            ship_floors.append(floor)
        ships_rooms.append(ship_rooms)
        ships_floors.append(ship_floors)

    with open('floors_information.txt', 'wb') as file:
        pickle.dump(ships_floors, file)
    with open('rooms_information.txt', 'wb') as file: 
        pickle.dump(ships_rooms, file)

def show_rooms(cruise, room):
    """[Muestra de forma matricial las habitaciones que ha escogido el cliente]

    Args:
        cruise ([int]): [Posición del barco en la lista]
        room ([int]): [Posición del piso del barco en la lista]
    """
    with open('floors_information.txt', 'rb') as file:
        floors = pickle.load(file)

    print("\nLas habitaciones disponibles son las siguientes: \n")
    for letter, number in floors[cruise][room].items():
        for i in range(len(number)):
            print(f"{letter + str(number[i])}", end=" ")
        print()

def prime_number(identity):
    """[Verifica si un número es primo o no]

    Args:
        identity ([int]): [Documento de identidad del cliente]

    Returns:
        [bool]: [Depende de si es primo o no]
    """
    prime = 1 
    for i in range(2,identity):
        if identity % i == 0:
            prime = 0
            return False
            break
    if prime:
        return True

def abundant_number(identity):
    """[Verifica si el documento de identidad introducido es abundante o no]

    Args:
        identity ([int]): [Documento de identidad del cliente]

    Returns:
        [bool]: [Si el documento de identidad es abundante o no]
    """
    sum_divisors = 0
    for i in range(1,identity):
        if identity % i == 0:
            sum_divisors += i
    if sum_divisors > identity:
        return True
    else:
        return False 

def upgrade_room(cruise, room_letter, amount_people, hallway, old_room, old_number):
    """[Verifica si la habitación en que hospeda el cliente es simple, y en caso que lo sea y se desea cambiar la habitación, se actualizan los datos de la habitación premium por elegir]

    Args:
        cruise ([int]): [Posición del crucero en la lista]
        room_letter ([str]): [Letra del pasillo de la habitación anterior]
        amount_people ([int]): [Cantidad de personas ]
        hallway ([str]): [Letra del pasillo de la habitación simple]
        old_room ([str]): [Nombre de la habitación simple]
        old_number ([int]): [Número de la habitación simple]

    Returns:
        [str]: [Nombre de la habitación premium]
    """

    if room_letter == "S":

        confirm_upgrade = input("\n¿Desea cambiar la habitación a una premium con el precio de la habitación simple? Si (s) o no (n): ").lower()
        while (confirm_upgrade!='s' and confirm_upgrade!='n'):
            confirm_upgrade = input("Ingrese (s) o (n): ").lower()
        
        if confirm_upgrade == 's':
            print("\nIngrese los datos de la nueva habitación en que desea hospedar: ")
            show_rooms(cruise, 1)

            with open('floors_information.txt', 'rb') as file:
                floors = pickle.load(file)

            while True:
                try:
                    hallway = input("\nIngrese la letra de la habitación en que se desea hospedar: ").upper()
                    if hallway not in (floors[cruise][1]).keys():
                        raise Exception
                    break 
                except Exception:
                    print("\nERROR: Dato ingresado no forma parte de las opciones")
        
            while True:
                try:
                    number = int(input("Ingrese el número: "))
                    if number not in floors[cruise][1][hallway]:
                        raise ValueError
                    break
                except ValueError:
                    print("\nERROR: Dato ingresado no forma parte de las opciones") 
            
            newRoom = 'P' + hallway + str(number)

            (floors[cruise][1][hallway]).remove(number)

            with  open("rooms_information.txt", 'rb') as f:
                rooms = pickle.load(f)

            for room in rooms[cruise]:
                if room.name == newRoom: 
                    room.setAvailability() 
                    room.setReference()

                #Si es el único que iba a hospedar en la habitación simple, entonces esta última se desocupa
                if amount_people == 1:
                    
                    for room in rooms[cruise]:
                        if room.name == old_room:
                            room.setAvailability()
                            room.setReference() 
                    
                    floors[cruise][0][hallway].append(old_number)
                    floors[cruise][0][hallway] = sorted(floors[cruise][0][hallway])
                    
            with open("rooms_information.txt", 'wb') as file:
                pickle.dump(rooms, file)

            with open("floors_information.txt", 'wb') as file:
                pickle.dump(floors, file)

            return newRoom

def client_information(amount_people, cruise, room, clients, room_letter, ships):
    """[Registra la información de cada cliente y convierte cada cliente en un objeto; actuliza los datos de la disponibilidad de la habitación elegida]

    Args:
        amount_people ([int]): [Cantidad de personas que hospedarán en la habitación]
        cruise ([int]): [Posición del crucero en la lista]
        room ([int]): [Posición del tipo de habitación en la lista]
        clients ([list]): [Lista de los clientes]
        room_letter ([str]): [Inicial del tipo de habitación]
        ships ([list]): [Lista con toda la información de cada crucero]
    Returns:
        [list]: [Lista de clientes actualizada]
    """

    with open('floors_information.txt', 'rb') as file:
        floors = pickle.load(file)
    
    while True:
        try:
            hallway = input("\nIngrese la letra de la habitación en que se desea hospedar: ").upper()
            if hallway not in (floors[cruise][room]).keys():
                raise Exception
            break 
        except Exception:
            print("\nERROR: Dato ingresado no forma parte de las opciones")
        
    while True:
        try:
            number = int(input("Ingrese el número: "))
            if number not in floors[cruise][room][hallway]:
                raise ValueError
            break
        except ValueError:
            print("\nERROR: Dato ingresado no forma parte de las opciones")   
    
    chosenRoom = room_letter + hallway + str(number)

    (floors[cruise][room][hallway]).remove(number)

    with open('floors_information.txt', 'wb') as f:
        pickle.dump(floors, f)

    with open('rooms_information.txt', 'rb') as file:
        rooms = pickle.load(file)
    
    for room in rooms[cruise]:
        if room.name == chosenRoom: 
            room.setAvailability() 
            room.setReference()
            client_room = room

    print(f"\nA continuación ingresará los datos de las personas que hospedarán en la habitación {chosenRoom}")
    for i in range(amount_people):
        
        selected_room = chosenRoom

        identity_discount = 0
        disability_discount = 0

        first = input("\nIngrese el nombre: ").capitalize()
        while not first.isalpha():
            first = input("Ingre un nombre válido: ").capitalize()
            
        last = input("Ingrese el apellido: ").capitalize()
        while not last.isalpha():
            last = input("Ingrese un apellido válido: ").capitalize()
        
        name = first + ' ' + last

        if file_existence('clients_information.txt'):
            with open('clients_information.txt', 'rb') as f:
                old_clients = pickle.load(f) 
            while True:
                try:
                    identity = int(input("Ingrese el documento de identidad: "))
                    if not 5<(len(str(identity)))<12:
                        raise Exception
                    for old_client in old_clients:
                        if old_client.identity == identity:
                            raise Exception
                    if len(clients)>0:
                        for client in clients:
                            if client.identity == identity:
                                raise Exception
                    break 
                except Exception as Identifier:
                    print("Error: No ingreso una secuencia de números o el documento de identidad ya existe")
        else: 
            while True:
                try:
                    identity = int(input("Ingrese el documento de identidad: "))
                    if not 5<(len(str(identity)))<12:
                        raise ValueError
                    if len(clients)>0:
                        for client in clients:
                            if client.identity == identity:
                                raise Exception
                    break 
                except Exception as Identifier:
                    print("Error: No ingreso una secuencia de números o el documento de identidad ya existe")


        if prime_number(identity):
            identity_discount = 0.10
        elif abundant_number(identity):
            identity_discount = 0.15

        while True:
            try:
                age= int(input('Ingrese la edad: '))
                if age<0 or age>130:
                    raise ValueError
                break 
            except ValueError:
                print("Edad inválida")
        
        if age>=65:
            newRoom = upgrade_room(cruise, room_letter, amount_people, hallway, client_room, number)
            if newRoom is not None:
                selected_room = newRoom

        disability = input("¿Tiene alguna discapacidad? Si (s) o no (n): ").lower()
        while (disability!='s' and disability!='n'):
            disability = input("Ingrese (s) o (n): ").lower()

        if disability == 's':
            disability = True
            disability_discount = 0.3
        elif disability == 'n':
            disability = False 

        payment = (1 - disability_discount - identity_discount)*client_room.price 
        chosenCruise = ships[cruise].name

        client = Client(name, identity, age, disability, chosenCruise, selected_room, payment, False)
        clients.append(client)

        with open('rooms_information.txt', 'wb') as f:
            pickle.dump(rooms, f)
        
    return clients 
    
def sell_rooms(ships):
    """[Dispone de todas las funcionalidades para vender una habitación o varias habitaciones dependiendo de la cantidad de clientes]

    Args:
        ships ([list]): [Lista con todos los cruceros]
    """

    while True:
        try:
            choose_ticket = int(input("\nSeleccione la opción que más se ajuste a su criterio. \nEn base a qué se desea comprar el boleto: \n1. Barco\n2. Destino\n>>> "))
            if choose_ticket not in range(1,3):
                raise ValueError
            break 
        except ValueError:
            print("\nError: Dato ingresado no forma parte de las opciones\n")

    if choose_ticket==1:
        print()
        for i, ship in (enumerate(ships)):
            print(f"{i+1}. {ship.name}")

    elif choose_ticket==2:
        print()
        for i, ship in (enumerate(ships)):
            print(f"{i+1}. {ship.route}")

    while True:
        try: 
            choose_cruise = int(input("Ingrese el número del barco que más ajuste a su criterio: "))
            if choose_cruise not in range(1,5):
                raise ValueError
            break 
        except:
            print("\nError: Dato ingresado no forma parte de las opciones\n")
    
    while True:
        try:
            type_room = int(input("\nElija el tipo de habitación en qué se desea hospedar: \n1. Sencilla\n2. Premium\n3. VIP\n>>> "))
            if type_room not in range(1,4):
                raise ValueError
            break 
        except ValueError:
            print("\nError: Dato ingresado no forma parte de las opciones\n")

    if type_room==1:
        name_room = 'simple'
        room_letter = 'S'
    elif type_room == 2:
        name_room = 'premium'
        room_letter = 'P'
    elif type_room == 3:
        name_room = 'vip'
        room_letter = 'V'
    
    while True:
        try:
            amount_people = int(input("Ingrese la cantidad de personas que van a hospedar: "))
            if amount_people<1:
                raise ValueError
            break 
        except ValueError:
            print("\nError: Debe ingresar un número entero positivo\n")
    
    with open('floors_information.txt', 'rb') as file:
        floors = pickle.load(file)

    chosen_ship = ships[choose_cruise-1]
    client_room_capacity = chosen_ship.roomCapacity[name_room]
    cruise = choose_cruise-1
    room = type_room-1

    rooms_availables = []
    for value in floors[cruise][room].values():
        for i in value:
            rooms_availables.append(1)
    space_available = sum(rooms_availables)*client_room_capacity

    while True: 

        if space_available<amount_people:
            print("No hay habitaciones suficientes")
            break 
        else:

            clients = []

            if amount_people>client_room_capacity:
                print("\nTendrán que comprar más de una habitación")
                people = amount_people
                while people>client_room_capacity:
                    show_rooms(cruise, room)
                    client_information(client_room_capacity, cruise, room, clients, room_letter, ships)
                    people -= client_room_capacity
                show_rooms(cruise, room)
                client_information(people, cruise, room, clients, room_letter, ships)
            else:
                show_rooms(cruise, room)
                client_information(amount_people, cruise, room, clients, room_letter, ships)

            ocupied_rooms = []
            total_payment = []

            print()
            print("-----------------------------------------")
            print('|{:^40}|'.format('Resumen de compra'))
            print("-----------------------------------------")
            print("Clientes:")
            for client in clients:
                print(client.showInformation())
                ocupied_rooms.append(client.chosenRoom)
                total_payment.append(client.moneySpent)
            monto_total = sum(total_payment)
            print("-----------------------------------------")
            list_ocupied_rooms = set(ocupied_rooms)
            info_ocupied_rooms = ', '.join(list_ocupied_rooms)
            print(f'Habitacion(es) seleccionada(s): {info_ocupied_rooms}')
            rooms_price = (chosen_ship.roomPrice[name_room])*len(clients)
            impuestos = rooms_price*0.16
            print(f'Monto total: {rooms_price}$')
            print(f"Monto con descuentos: {monto_total}$")
            print(f'Impuestos: {impuestos}$')
            print("-----------------------------------------")
            print(f"Total: {monto_total+impuestos}$")

        if not file_existence('clients_information.txt'):
            with open('clients_information.txt', 'wb') as file:
                pickle.dump(clients, file)
        else: 
            with open('clients_information.txt', 'rb') as f:
                new_clients = pickle.load(f)

                for client in clients:
                    new_clients.append(client)

            with open('clients_information.txt', 'wb') as file:
                pickle.dump(new_clients, file)
        break 

def room_to_free(ships):
    """[Actuliza la disponibilidad de la habitación elegida - Desocupar habitación]

    Args:
        ships ([list]): [lista con toda la información de cada crucero]

    Returns:
        [bool]: [Depende de si la habitación fue conseguida o no]
    """
    print()
    for i, ship in (enumerate(ships)):
            print(f"{i+1}. {ship.name}")
    
    while True:
        try: 
            user_cruise = int(input("Ingrese el número del barco donde se encuentra la habitación: "))
            if user_cruise not in range(1,5):
                raise ValueError
            break 
        except:
            print("\nError: Dato ingresado no forma parte de las opciones\n")
    
    letter_room_type = input("\nIngrese el tipo de habitación que desea eliminar: \nSencilla (S) \nPremium (P) \nVIP (V) \n>>> ").upper()
    while (letter_room_type!='S' and letter_room_type!='P' and letter_room_type!='V'):
        letter_room_type = input("Ingrese (S) (P) o (V): ").upper()

    if letter_room_type == 'S':
        room_type = 0
    elif letter_room_type == 'P':
        room_type = 1
    elif letter_room_type == 'V':
        room_type = 2
    
    letter_room = input("Ingrese la letra del pasillo de la habitación: ").upper()
    while (not letter_room.isalpha()) or (len(letter_room)>1):
        letter_room = input("Ingrese una letra: ").upper()

    while True:
        try:
            room_number = int(input("Ingrese el número de la habitación: "))
            if room_number<0:
                raise ValueError
            break
        except ValueError:
            print("\nERROR: Debe ingresar un número entero positivo")   

    room_name = letter_room_type + letter_room + str(room_number)

    with open('rooms_information.txt', 'rb') as file:
        rooms_to_update = pickle.load(file)

    ocupied = True 

    for room in rooms_to_update[user_cruise-1]:
        if room.name == room_name:
            check_room_reference = input("Introduzco la referencia de las personas que hospedaban en la habitación: ")
            if room.reference == check_room_reference:
                ocupied = room.setAvailability()
                room.setReference()
    
    with open("rooms_information.txt" , 'wb') as f:
        pickle.dump(rooms_to_update, f)

    if not ocupied:
        with open("floors_information.txt", 'rb') as f:
            floors = pickle.load(f)
        
        floors[user_cruise-1][room_type][letter_room].append(room_number)

        floors[user_cruise-1][room_type][letter_room] = sorted(floors[user_cruise][room_type][letter_room])

        with open("floors_information.txt", 'wb') as file:
            pickle.dump(floors, file)

    return ocupied

def search_room(search_choice, ships):
    """[Busca las habitaciones en función del filtro elegido por el usuario]

    Args:
        search_choice ([int]): [Filtro de búsqueda elegido]
        ships ([list]): [Lista con la información de cada crucero]
    """

    with open("rooms_information.txt", 'rb') as f:
        rooms_list = pickle.load(f)

    print()
    for i, ship in (enumerate(ships)):
            print(f"{i+1}. {ship.name}")
    
    while True:
        try: 
            user_cruise = int(input("Ingrese el número del barco donde se encuentra la habitación: "))
            if user_cruise not in range(1,5):
                raise ValueError
            break 
        except:
            print("\nError: Dato ingresado no forma parte de las opciones\n")
    
    
    rooms_ship = rooms_list[user_cruise-1]

    if search_choice==1:
        letter_room_type = input("\nIngrese el tipo de habitación que desea eliminar: \nSencilla (S) \nPremium (P) \nVIP (V) \n>>> ").upper()
        while (letter_room_type!='S' and letter_room_type!='P' and letter_room_type!='V'):
            letter_room_type = input("Ingrese (S) (P) o (V): ").upper()
        
        for room in rooms_list[user_cruise-1]:
            if letter_room_type in room.name:
                print(room.showInformation())

    elif search_choice==2:

        while True:
            try: 
                mini = int(input("Ingrese el mínimo del rango de la capacidad de la habitación que desea buscar: "))
                if mini<0:
                    raise ValueError
                maxi = int(input("Ingrese el máximo del rango: "))
                if maxi<0:
                    raise ValueError
                break
            except ValueError:
                print("¡Dato inválido!")

        range_rooms = [room for room in rooms_ship if mini <= room.capacity <= maxi]

        if len(range_rooms)>0:
            for room in range_rooms:
                print(room.showInformation())
        else:
            print("No se encontraron habitaciones en ese rango")

    elif search_choice==3:

        letter_room_type = input("\nIngrese el tipo de habitación que desea eliminar: \nSencilla (S) \nPremium (P) \nVIP (V) \n>>> ").upper()
        while (letter_room_type!='S' and letter_room_type!='P' and letter_room_type!='V'):
            letter_room_type = input("Ingrese (S) (P) o (V): ").upper()
        
        letter_room = input("Ingrese la letra del pasillo de la habitación: ").upper()
        while (not letter_room.isalpha()) or (len(letter_room)>1):
            letter_room = input("Ingrese una letra: ").upper()

        while True:
            try:
                room_number = int(input("Ingrese el número de la habitación: "))
                if room_number<0:
                    raise ValueError
                break
            except ValueError:
                print("\nERROR: Debe ingresar un número entero positivo")   

        room_name = letter_room_type + letter_room + str(room_number)

        for room in rooms_ship:
            if room.name == room_name:
                print(room.showInformation())

def room_process():
    """[Ejecuta todas las funciones posibles que se pueden hacer en la venta y búsqueda de habitaciones, todo en función a la elección del usuario]

    """
    ships = save_ship_information()
    
    if not file_existence('floors_information.txt') and not file_existence("rooms_fuctions.txt"):
        save_rooms(ships)

    print("\n¡Bienvenido a los procesos de venta y búsqueda de habitaciones del Saman Caribbean!")

    while True: 
        
        while True:
            try:
                sell_choice = int(input("\n¿Qué función quiere realizar? \n1. Vender habitación \n2. Desocupar habitación \n3. Buscar habitación \n4. Salir \n>>> "))
                if sell_choice not in range(1,5):
                    raise ValueError
                break 
            except ValueError:
                print("\nError: Dato ingresado no forma parte de las opciones dadas\n")
        
        if sell_choice==1:
            sell_rooms(ships)

        elif sell_choice==2:

            ocupied_room = room_to_free(ships)
            if not ocupied_room:
                print("Habitación desocupada")
            else:
                print("No se encontro la habitación o ya estaba desocupada")

        elif sell_choice==3:

            while True:
                try:
                    search_choice = int(input("¿Qué filtro desea usar para buscar la habitación? \n1. Tipo\n2. Capacidad\n3. Tipo + Pasillo + Número\n>>> "))
                    if search_choice not in range(1,4):
                        raise ValueError
                    break 
                except ValueError as Identifier :
                    print("\nError: Dato ingresado no forma parte de las opciones\n")

            search_room(search_choice, ships)

        else:
            break 
