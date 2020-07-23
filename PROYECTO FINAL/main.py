#REVIEW 
from cruises_functions import *
from tour_functions import * 
from restaurant_functions import * 
from rooms_functions import *
from statistics_functions import *

def main():
    
    print("\n¡Bienvenido al Saman Caribbean!")

    while True: 

        while True:
            try:
                user_choice = int(input("\n¿Qué parte del sistema desea visitar/revisar? \n1. Información de los cruceros \n2. Venta y búsqueda de habitaciones \n3. Restaurante \n4. Tours \n5. Estadísticas del funcionamiento del crucero \n6. Salir \n>>>  "))
                if user_choice not in range(7):
                    raise ValueError
                break
            except ValueError:
                print("\nERROR: Dato ingresado no forma parte de las opciones")
        if user_choice==1:
            print_ship_information()

        elif user_choice==2:
            room_process()

        elif user_choice==3:
            restaurant()

        elif user_choice==4:
            tour()

        elif user_choice==5:
            statistics()

        elif user_choice==6:
            print("¡Adiós!")
            break 

if __name__ == "__main__":
    main()