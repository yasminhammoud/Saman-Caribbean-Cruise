from abc import ABC, abstractmethod 

class Restaurant:

    def __init__(self, name, price): 
        self.name = name 
        self.price = price
    
    @abstractmethod
    def showInformation(self):
        pass
