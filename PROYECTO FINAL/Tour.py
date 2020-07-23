class Tour:

    def __init__(self, typeTour, price, discount, maxPerClient, totalCapacity, time, spaceAvailable):
        self.typeTour = typeTour
        self.price = price
        self.discount = discount
        self.maxPerClient = maxPerClient
        self.totalCapacity = totalCapacity
        self.time = time
        self.spaceAvailable = spaceAvailable

    def showInformation(self):
        return ('|{:^29}|{:^23}|{:^19}|{:^24}|{:^20}|{:^15}|'.format(self.typeTour, self.price,self.maxPerClient, self.discount, f"{self.spaceAvailable}/{self.totalCapacity}", self.time))
    
    def purchase(self, amountPeople):
        
        if self.discount == '3ra y 4ta persona: 10':

            if amountPeople==3 or amountPeople==4:
                bill = self.price*0.9
        else: 
            bill = self.price
        
        if amountPeople==1 or amountPeople==2:
            bill = self.price
            
        return bill

    def showBill(self, bill):

        print()
        print("-----------------------------")
        print('|{:^27}|'.format('Resumen de compra'))
        print("-----------------------------")
        print('|{:^13}|{:^13}|'.format('Hora', self.time))
        print("-----------------------------")
        print('|{:^13}|{:^13}|'.format('Monto total', (f'{bill}$')))
        print("-----------------------------")

    def updateAvailability(self, amountPeople):
        self.spaceAvailable -= amountPeople

        

    




  