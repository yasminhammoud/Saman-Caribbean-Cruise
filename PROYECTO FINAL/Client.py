class Client:

    def __init__(self, name, identity, age, disability, chosenCruise, chosenRoom, moneySpent, boughtTour):
        self.name = name
        self.identity = identity
        self.age = age 
        self.disability = disability
        self.chosenCruise = chosenCruise
        self.chosenRoom = chosenRoom
        self.moneySpent = moneySpent
        self.boughtTour = boughtTour

    def showInformation(self):
        if self.disability ==True:
            client_disability = 'Si'
        else:
            client_disability = 'No'
        return (f"Nombre: {self.name} \nDocumento de identidad: {self.identity} \nEdad: {self.age} \nDescapacitado: {client_disability}\n")

    def setMoneySpent(self, amount):
        self.moneySpent += amount
    
    def setBuyTour(self):
        self.boughtTour = True
