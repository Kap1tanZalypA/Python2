# class Peli:
#     laatikon_maatetriaali = "PAHVI"
#     def __init__(self):
#         self.rahat = 1000
#     def siirto(self):
#         print("Heotetaan noppa")
#         
#         
#         
# monopoli = Peli()
# print(monopoli.rahat)
# monopoli.siirto()
# 
#     def __init__(self):
#             self.kuivuus = 1    
#     
#




                                        #TEHT2







# class Telinne:
#     def __init__(self):
#         self.paperit = []
#         for p in range(10
#                        ):
#             paperi = Paperi()
#             self.paperit.append(paperi)
#     def anna_paperi(self):
#         if len(self.paperit) > 5:
#             annettava_paperi = self.paperit.pop()
#         else:
#             annettava_paperi = "Ei ole"
#             print("PiP")
#             
#         return annettava_paperi
#         
# luokantelinne = Telinne()
# 
# 
# for n in range(10):
#     ykspaperi = luokantelinne.anna_paperi()
#     print(ykspaperi)



                                    #Teht3



# class Pisyn:
#     def __init__(self):
#         self.zhizhka = 10
#         
# class Podhodik:
#     def __init__(self):
#         self.num1 = 2
#         
#     def Output(self, podhodik, pisyn):
#             sum1 = podhodik.num1 * pisyn.zhizhka
#             return sum1
#         
# pisyn = Pisyn()
# podhodik = Podhodik()
# 
# 
# 
# result = podhodik.Output(podhodik, pisyn )
# print(result)



                                #Teht4 (Obizyanka i kakashki)



# import random
# 
# 
# 
# class Obizyanka:
#     def __init__(self):
#         self.kakashke = 1
#         
#         
# class Rebenocheg:
#     def __init__(self):
#         self.popadanie = random.randint(1,10)
#     def Output(self, obizyanka, rebenocheg):
#         while obizyanka.kakashke <= self.popadanie:
#             obizyanka.kakashke += 1
#             print("Pryam v desyatochky")
#         return obizyanka
#             
#             
#         
# 
# 
# obizyanka = Obizyanka()
# rebenocheg = Rebenocheg()
# 
# result = rebenocheg.Output( obizyanka, rebenocheg  )
# print(result)


        
        
        
        

# self.kurssin_oppilat_srt = sorted(self.kurssin_oppilat, key=lamda oppilas: oppilas.arvosana, reverse= True)


# class Koira:
#     def __init__(self):
#         self.nimi = "ei nimi"
#         self.nalka = 1000
#         
#     def ruokinta(self, ruoka):
#         
#         self.nalka -=ruoka
#         
# munkoira = Koira()
# munkoira.ruokinta()
# print(munkoira.nalka)



# class Talo:
#     def __init__(self):
#         self.kissat = []
#         
# class Kissa:
#     def __init__(self):
#         self.nimi = "eioleviela"
#         self.pennut = []
#     def aantely(self):
#         print("Miau!")
#         
# munkissa = Kissa()
# pentu = Kissa()
# munkissa.pennut.append(pentu)
# koti = Talo()
# koti.kissat.append(munkissa)




# list1 = [20, 8 ,3, 33]
# p0 = list1[0]
# p1 = list1[1]
# for nums in list1:
#     if p0 > p1:
#         list1[0] = p1
#         list1[1] = p0
#     else:
#         list1[0] = p0
#         list1[1] = p1
#     print(nums)
        

# list2 = ["a", "b"]
# temp = list2[0]
# 
# p1 = list2[1]
# 
# p0 = list2[0]
# 
# print("p0:",p0,"p1:",p1)
# list2[0] = p1
# list2[1] = p0
# print(list2)


def bubble_sort(arr):
    n= len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = [20, 8, 3, 33]
print(bubble_sort(arr))
    
    




