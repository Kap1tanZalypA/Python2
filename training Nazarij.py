a = 12
# b = 23
# sana = "kissa"
# tulos = a + b
# print("tulos :",  tulos)
# 
# taulu = [12, 23, 34, 45, "kissa"]
# 
# 
# 
# def summa (a,b):   #argumentit a ja b korvautuvat annetuilla arvoilla kutsuttaessa
# 
#      return (a + b)    #return palauttaa funktiosta jotain
# 
# tulos = summa(10,10)    #returnilla palautettu arvo kannattaa ottaa talteen muuttujaan
# 
# print(tulos)
# 
# 
# laskuri = 0           #laitetaan laskuri TAAS nollaksi, muuten se olisi tassa jo 10
# 
# while laskuri < 10:  #niin pitkaan kuin laskuri on pienempi kuin 10
# 
#     print(laskuri)
# 
#     laskuri = laskuri + 1
#     if laskuri == 5:
# 
#              print("Laskuri on nyt viisi.")


# suurpedot = ["zalypa", "pipa", "zhopa", "chlen"]
# if "zalypa" in suurpedot:
#     print("Zalypa in suurpedot list")
# if "zalypa" not in suurpedot:
#     print("zalypa not in suurpeto list")

# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# combined_list = list1 + list2
# print(combined_list)

# def summa (kissanprinti):
#     print ("Miisu")
# summa()







# def pienet(lukulista, raja):
#     tulos = []
#     laskuri = 0
#     while laskuri < len(lukulista):
#         kokeilu = lukulista[laskuri]
#         if kokeilu > raja:
#             tulos.append(kokeilu)
#         laskuri = laskuri +1
#     return tulos
# 
# 
# 
# def yla_ala(lukulista, alaraja, ylaraja):
#     ala = []
#     laskuri = 0
#     while laskuri < len(lukulista):
#         kokeilu = lukulista[laskuri]
#         if kokeilu > raja:
#             tulos.append(kokeilu)
#         laskuri = laskuri +1
#     return ala,

# def autoprog (autoList):
#     cars_price = []
#     index = 0
#     while index < len(autoList):
#         if type(autoList[index]) == str or type(autoList[index - 1]) == str:
#             cars_price.append(autoList[index - 1])
#         index = index + 1
#     return cars_price
# 
# cars_price = autoprog(["audi", 200, 300, "Mercedes", 500, 700])
# print (cars_price)


# def tuplaa(luku):
#     luku = luku * 2
#     print(luku)
#     tuplaa(luku)
# tuplaa(1)


# def tp():
#     if glip == 0:
#         print("tilanne vakaa, Nolla")
#     if glip == 1:
#         print("huutera 1")
# 
# glip =0
# tp()
# glip = 1
# tp()

# def cat_color(catList, colorList):
#     cats_colors = []
#     
#     index = 0
#     while index < len(catList):
#         cats_colors.append(catList[index])
#         cats_colors.append(colorList[index%len(colorList)])
#         index = index +1
#     return cats_colors
# 
# 
# cats_colors = cat_color(["dasdasd", "ahmed", "abdula", "rahmed"],["vihrea", "punainen"])
# 
# print(cats_colors)
        
# import random
# setNumLista= []
# 
# #listan taytto
# index = 0
# while index < 1000:
#     setNum1 = random.randint(1, 100)
#     setNumLista.append(setNum1)
#     index = index + 1
#     
# #listaan keskiarvolaskenta
# index = 0
# summa = 0
# while index < 1000:
#     #lisaa summaan listasta kohdasta index
#     summa += setNumLista[index]
#     index = index + 1
# tulos = summa / 1000



   
# print(tulos)
# print(setNumLista)
# print(summa)