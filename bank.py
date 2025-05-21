class Bank:
    def __init__(self):
        self.deposit = 0
        self.percent = 0.03
        self.years = 5


    def newMoney(self, user, bank):
        bank.deposit += user.pament

 
    def newDep(self, bank):
        bank.deposit += (bank.deposit * bank.percent) * bank.years + bank.deposit

        return bank.deposit
        


class User:
    def newPament (self):
        self.pament = 0


bank = Bank()
user = User()
user.newPament(1000)
bank.newDep()
                                                             #   bank account

list1 = []

class Bank:
    def __init__(self):
        self.deposit = 0
        self.percent = 0.03
        self.years = 5
    
   
    def newMoney(self, user, bank):  
        list1.append(user.pament)
        bank.deposit += sum(list1)
        user.pament = 0 
    
    def newDep(self, bank):  
        bank.deposit += (bank.deposit * bank.percent) * bank.years
        return bank.deposit
    
    

class User:
    def newPament(self):
        for nums in list1: 
            self.pament = int(input("Kirjoita summa: "))



bank = Bank()
user = User()

bank.newMoney(user, bank) 
bank.newDep(bank)  
print(bank.deposit) 
print(user.pament)


