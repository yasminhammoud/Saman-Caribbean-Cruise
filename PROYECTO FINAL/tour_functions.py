from Tour import Tour
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

def tour_information():
    """[Imprime la información de cada tour a través de una tabla]
    """

    with open("tours_information.txt", 'rb') as f:
        tours = pickle.load(f)

    print("\nLos tours que se ofrecen son los siguientes:\n")
    print("-----------------------------------------------------------------------------------------------------------------------------------------")
    print('|{:^29}|{:^21}|{:^17}|{:^24}|{:^20}|{:^15}|'.format('Tipo',' Costo por persona ($) ',' Cupos por cliente ','Descuento (%)','Cupos disponibles','Hora de inicio'))
    print("-----------------------------------------------------------------------------------------------------------------------------------------")

    for tour in tours:
        print(tour.showInformation())
        print("-----------------------------------------------------------------------------------------------------------------------------------------")

def check_amount_people():
    """[Verifica si la cantidad de personas se encuentra en el límite de los cupos]

    Returns:
        [int]: [Cantidad de personas que compraran el tour]
    """
    while True:
        try:
            amount_people = int(input("Ingrese la cantidad de personas: "))
            if not 0<amount_people<5:
                raise ValueError
            break 
        except:
            print("Error: Debe ingresar un número entero entre el 1 y 4")
    return amount_people
            
def buy_tour(i):
    """[Verifica si hay cupos disponibles para vender un tour a los clientes]

    Args:
        i ([int]): [Posición del tour que se desea comprar]
    """
    with open("tours_information.txt", 'rb') as f:
        tours = pickle.load(f)

    amount_people = check_amount_people()

    if tours[i].spaceAvailable >= amount_people:

        total_bill = 0
        print("\nIngrese los documentos de identidad de las personas que comprarán el tour:")

        for person in range(1, amount_people + 1):

            with open("clients_information.txt", 'rb') as f:
                clients = pickle.load(f)

            clients_dni = []
            for client in clients:
                clients_dni.append(client.identity)

            while True:
                try:
                    dni = int(input("\nIngrese el documento de identidad: "))
                    if not 5<(len(str(dni)))<12:
                        raise Exception
                    if dni not in clients_dni:
                        raise Exception
                    break 
                except Exception as Identifier:
                    print("Error: No ingreso una secuencia de números o el documento no forma parte de la base de datos")
                
            client_bill = tours[i].purchase(person)
            total_bill += client_bill

            for client in clients:
                if client.identity == dni:
                    client.setBuyTour()
                    client.setMoneySpent(client_bill)
            
            with open("clients_information.txt", 'wb') as file:
                pickle.dump(clients, file)

        tours[i].showBill(total_bill)
        tours[i].updateAvailability(amount_people)  

        with open("tours_information.txt", 'wb') as file:
            pickle.dump(tours, file)

    elif tours[i].spaceAvailable == 0:
        print("\nNo hay cupos disponibles")

    else: 
        print("\nLa cantidad de personas es mayor que la cantidad de cupos disponibles")

def purchase_tour():
    """[La función se encarga de registrar los datos de compra del cliente, en caso que haya cupos disponibles]
    """

    with open("tours_information.txt", 'rb') as f:
            tours = pickle.load(f)
    
    print()
    for i,tour in enumerate(tours):
        print(f"{i+1}. {tour.typeTour}")

    while True: 
        try: 
            tour_to_sell = int(input("\nIntroduzca el número correspondiente al tour que se desea comprar: "))
            if tour_to_sell not in range(len(tours)+1):
                raise ValueError
            break 
        except:
            print("\nError: Dato ingresado no forma parte de las opciones")
    
    if tour_to_sell==1:
        buy_tour(0)

    elif tour_to_sell==2:
        buy_tour(1)

    elif tour_to_sell==3:

        while True:
            try: 
                amount_people= int(input("Ingrese la cantidad de personas: "))
                if not amount_people>0:
                    raise ValueError
                break 
            except ValueError:
                print("Error: Debe ingresar un número entero positivo")

        total_bill = 0
        print("\nIngrese los documentos de identidad de las personas que comprarán el tour:")

        for person in range(1, amount_people + 1):

            with open("clients_information.txt", 'rb') as f:
                clients = pickle.load(f)

            clients_dni = []
            for client in clients:
                clients_dni.append(client.identity)

            while True:
                try:
                    dni = int(input("\nIngrese el documento de identidad: "))
                    if not 5<(len(str(dni)))<12:
                        raise Exception
                    if dni not in clients_dni:
                        raise Exception
                    break 
                except Exception as Identifier:
                    print("Error: No ingreso una secuencia de números o el documento no forma parte de la base de datos")
            
            for client in clients:
                if client.identity == dni:
                    client.setBuyTour()
            
            with open("clients_information.txt", 'wb') as file:
                pickle.dump(clients, file)

        tours[2].showBill(total_bill)
    
    elif tour_to_sell==4:
        buy_tour(tours)

def tour():
    """[Se encagar de ejecutar cada una de las funcionalidades disponibles para los tours del crucero]

    """
    tour1 = Tour("Tour en el puerto", 30, '3ra y 4ta persona: 10', 4, 10, '7:00 A.M.', 10)
    tour2 = Tour("Degustación de comida local", 100, 0, 4, 100, '12:00 P.M.', 100)
    tour3 = Tour("Trotar por el pueblo/ciudad", 0, 0, 'No hay límite', 'No hay límite/', '6:00 A.M.', '')
    tour4 = Tour("Visita a lugares históricos", 40, '3ra y 4ta persona: 10', 4, 15, '10:00 A.M.', 15)
    tours = [tour1, tour2, tour3, tour4]

    if not file_existence("tours_information.txt"):
        with open("tours_information.txt", 'wb') as file:
            pickle.dump(tours, file)

    print("\n¡Bienvenido a Tours del Saman Caribbean!")

    while True: 

        while True:
            try:
                tour_choice = int(input("\n¿Qué función quiere realizar? \n1. Mostrar tours \n2. Vender tour \n3. Salir \n>>> "))
                if tour_choice not in range(1,4):
                    raise ValueError
                break 
            except ValueError:
                print("\nError: Dato ingresado no forma parte de las opciones dadas\n")

        if tour_choice==1:

            tour_information()
        
        elif tour_choice==2:

            if file_existence("clients_information.txt"):
                purchase_tour()
            else:
                print("No se pudo realizar la operación porque no hay clientes registrados")
        
        else: 
            print("¡Hasta luego!")
            break 
