class Room:

    def __init__(self, roomType, letter, number, name, reference, capacity, price, information, availability):
        self.roomType = roomType 
        self.letter = letter         
        self.number = number
        self.name = name        
        self.capacity = capacity
        self.reference = reference
        self.price = price    
        self.information = information 
        self.availability = availability    

    def showInformation(self):
        if self.availability ==True:
            availability = 'Si'
        else:
            availability = 'No'
        return (f"\nTipo: {(self.roomType).capitalize()} \nNombre: {self.letter + self.number} \nCapacidad: {self.capacity} \nReferencia: {self.reference} \nPrecio: {self.price} \nInformación: {self.information} \nOcupada: {availability}")
    
    def setAvailability(self):
        if self.availability == False:
            self.availability = True
        else:
            self.availability = False
        return self.availability

    def setReference(self):
        if self.availability == True:
            self.reference = input("Ingrese la referencia de las personas que se hospedan en esta habitación (Si es un error, presione enter): ")
        else:
            self.reference = ''
                            