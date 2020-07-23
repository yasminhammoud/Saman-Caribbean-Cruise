import requests 
from Ship import Ship

def save_ship_information():
    """[Guarda la información ofrecida por el API y es almacenada en un objeto crusero]

    Returns:
        [list]: [Lista de los cruceros como objetos]
    """
    response = requests.get('https://saman-caribbean.vercel.app/api/cruise-ships')
    saman_caribbean_api = response.json()

    ships = []

    for cruise in saman_caribbean_api:
        name =  cruise['name']
        route = ' - '.join(cruise['route'])
        departure = cruise['departure']
        roomPrice = cruise['cost']
        rooms = cruise['rooms']
        roomCapacity = cruise['capacity']
        sells = cruise['sells']
        ship = Ship(name, route, departure, roomPrice, rooms, roomCapacity, sells)
        ships.append(ship)
        
    return ships

saman_caribbean_api = [
    {'name': 'El Dios de los Mares', 
'route': ['Fort Lauderdale', 'Bahamas', 'St. Thomas', 'Islas Vírgenes', 'Fort Lauderdale'], 
'departure': '2020-12-20T00:00:00.000Z', 
'cost': {'simple': 69.99, 'premium': 89.99, 'vip': 129.99}, 
'rooms': {'simple': [4, 10], 'premium': [3, 9], 'vip': [1, 6]}, 
'capacity': {'simple': 2, 'premium': 4, 'vip': 8}, 
'sells': [
    {'name': 'Coca Cola', 'price': 3.99, 'amount': 500}, 
    {'name': 'Pizza', 'price': 11.99, 'amount': 230}, 
    {'name': 'Hamburguesa', 'price': 25.99, 'amount': 250}, 
    {'name': 'Hamburguesa & Refresco', 'price': 19.99, 'amount': 250}, 
    {'name': 'Ron', 'price': 6.99, 'amount': 300}]}, 
{'name': 'La Reina Isabel', 
'route': ['Barbados', 'Bahamas', 'Aruba', 'Curaçao', 'Santa Lucia', 'Barbados'], 
'departure': '2020-12-21T00:00:00.000Z', 
'cost': {'simple': 59.99, 'premium': 99.99, 'vip': 119.99}, 
'rooms': {'simple': [6, 10], 'premium': [4, 8], 'vip': [2, 4]}, 
'capacity': {'simple': 2, 'premium': 4, 'vip': 8}, 
'sells': [
    {'name': 'Coca Cola', 'price': 5.99, 'amount': 100}, 
    {'name': 'Pasta', 'price': 12.99, 'amount': 150}, 
    {'name': 'Hamburguesa', 'price': 13.99, 'amount': 230}, 
    {'name': 'Donas', 'price': 2.99, 'amount': 110}, 
    {'name': 'Ron', 'price': 11.99, 'amount': 250}]}, 
{'name': 'El Libertador del Océano', 
'route': ['Miami', 'Bahamas', 'Puerto Rico', 'Haití', 'República Dominicana', 'Miami'], 
'departure': '2020-12-17T00:00:00.000Z', 
'cost': {'simple': 49.99, 'premium': 89.99, 'vip': 139.99}, 
'rooms': {'simple': [6, 8], 'premium': [4, 6], 'vip': [4, 2]}, 
'capacity': {'simple': 3, 'premium': 5, 'vip': 12}, 
'sells': [
    {'name': 'Coca Cola', 'price': 2.99, 'amount': 150}, 
    {'name': 'Pizza', 'price': 11.99, 'amount': 230}, 
    {'name': 'Hamburguesa', 'price': 16.99, 'amount': 200}, 
    {'name': 'Cerveza', 'price': 3.99, 'amount': 180}, 
    {'name': 'Cofuta & Refresco', 'price': 11.99, 'amount': 150}]}, 
{'name': 'Sabas Nieves', 
'route': ['Galveston', 'Cozumel', 'Haití', 'Jamaica', 'Panamá', 'Galveston'], 
'departure': '2020-12-19T00:00:00.000Z', 
'cost': {'simple': 59.99, 'premium': 99.99, 'vip': 119.99}, 
'rooms': {'simple': [4, 12], 'premium': [3, 7], 'vip': [2, 4]}, 
'capacity': {'simple': 3, 'premium': 5, 'vip': 10}, 
'sells': [
    {'name': 'Coca Cola', 'price': 5.99, 'amount': 100}, 
    {'name': 'Pizza', 'price': 12.99, 'amount': 130}, 
    {'name': 'Hamburguesa', 'price': 15.99, 'amount': 260}, 
    {'name': 'Cofuta', 'price': 6.99, 'amount': 150}, 
    {'name': 'Cofuta & Refresco', 'price': 12.99, 'amount': 350}]}
]

def save_ship_information():

    ships = []

    for cruise in saman_caribbean_api:
        name =  cruise['name']
        route = ' - '.join(cruise['route'])
        departure = cruise['departure']
        roomPrice = cruise['cost']
        rooms = cruise['rooms']
        roomCapacity = cruise['capacity']
        sells = cruise['sells']
        ship = Ship(name, route, departure, roomPrice, rooms, roomCapacity, sells)
        ships.append(ship)
        
    return ships

def print_ship_information():
    """[Imprime la información de cada barco del crucero]
    """
    saman_caribbean_ships = save_ship_information()

    print("\nLos barcos disponibles son los siguientes:\n")

    for ship in saman_caribbean_ships:
        ship.showInformation()
        print("-----------------------------------------------------------------------------------------------------------------------------------")
        print()
