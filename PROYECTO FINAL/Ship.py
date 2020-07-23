class Ship:

    def __init__(self, name, route, departure, roomPrice, rooms, roomCapacity, sells):
       self.name = name
       self.route = route
       self.departure = departure
       self.roomPrice = roomPrice
       self.rooms = rooms
       self.roomCapacity = roomCapacity
       self.sells = sells 
    
    def showInformation(self):

        print("-----------------------------------------------------------------------------------------------------------------------------------")
        print('|{:^26}|{:^75}|{:^26}|'.format('Nombre','Ruta','Salida'))
        print("-----------------------------------------------------------------------------------------------------------------------------------")
        print('|{:^26}|{:^75}|{:^26}|'.format('', self.route, self.departure))
        print('|{:^26}|-------------------------------------------------------------------------------------------------------'.format(''))
        print('|{:^26}|{:^53}|{:^48}|'.format(self.name,'Precio por habitación','Capacidad por tipo de habitación'))
        print('|{:^26}|-------------------------------------------------------------------------------------------------------'.format(''))
        print('|{:^26}|{:^53}|{:^48}|'.format('', (f" Simple: {self.roomPrice['simple']}$  /  Premium: {self.roomPrice['premium']}$  /  VIP: {self.roomPrice['vip']}$ "), (f"Simple: {self.roomCapacity['simple']}  /  Premium: {self.roomCapacity['premium']}  /  VIP: {self.roomCapacity['vip']} ")))

       