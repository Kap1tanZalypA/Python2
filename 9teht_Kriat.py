#                                                     #teht1
# class Jaatelokioski:
#     def __init__(self):
#         self.jaatelo = 1000
#         self.kassa = 0
        
#     def myynti(self, ihminen):
#         self.kassa = ihminen.raha
#         ihminen.raha -= 100
#         ihminen.omajaatelo += 100
#         self.jaatelo -= 100


# class Ihminen:
#     def __init__(self):
#         self.raha = 100
#         self.omajaatelo = 0
    

# kioski = Jaatelokioski()
# bobby = Ihminen()
# kioski.myynti(bobby)


#teht2

class Paikka:
    def __init__(self):
        self.field = [3, 1, 0, 2, 0, 1, 1, 0, 1, 0, 1, 0]
        self.mosquito = 1
        self.kasvi = 2
        self.none = 0
        self.ihminen = 3
        self.energy = 100

class Teht:
    def __init__(self):
        self.position = 0

    


    def move_forward(self):
        self.position += 1
        self.check_position(p)


    def move_backward(self):
        self.position -= 1
        self.check_position(p)

    def check_position(self,p):
        if self.position > 11:
            self.position = 0
        elif self.position < 0:
            self.position = 11


        if self.position == 3:
            print("You win!")

        if p.field[self.position] == p.mosquito:
            p.energy -=10
            print("You los 10 energy from mosquito")
            print(f"Remeining energy: {p.energy}")

        
        if p.field[self.position] == p.kasvi:
            print("You found a plant!")
        elif p.field[self.position] == p.ihminen:
            print("You encountered a human!")
            


         

p = Paikka()    
t = Teht() 

print("Starting game!")
print(f"Initial position: {t.position}, Energy: {p.energy}")

t.move_forward()

t.move_forward()

t.move_forward()
