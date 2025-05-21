#teht1
# def my_sum():
#     a = float(input("Write the first number: "))
#     b = float(input("Write the second number: "))
#     tulos = a + b
#     print(tulos)
    
# my_sum()


#teht2
# def alkio():
#     start_num = float(input("Write the start number: "))
#     end_num = float(input("Write the end number: "))
#     while True:
#         if start_num > end_num:
#             start_num = start_num - 1
#             print (start_num)
#             if start_num == end_num:
#                 return
#         if end_num > start_num:
#             start_num = start_num + 1
#             print(start_num)
#             if start_num == end_num:7
#                 return
              
# alkio()

# #teht3
# def etsi():
#     num_list = [7 , 2, 6, 22, 9, 77, 3, 44]
#     user_inp = int(input("Write the number: "))
    
    
#     if user_inp in num_list:
#         index = num_list.index(user_inp)
#         print(f"Indeks of number that you have searched is: {index}")

# etsi()


#teht4
# def pal():
#     inp1 = input("Write first number: ")
#     inp2 = input("Write second number: ")
#     sum1 = inp1 + inp2
#     print(sum1)

# pal()


#teht5
# def summa(*args):
#     return sum(args)

# print(summa(1, 2, 3))        
# print(summa(10, 20, 30, 40)) 
# print(summa())   


#teht6
# print("Write the first number: ")
# num1 = float(input())
# print("Write the second number: ")
# num2 = float(input())
# blank = []

# oper = input()
# def s1():
#  if oper == "+":
#     sum1 = num1 + num2
#     blank.append(sum1)
#     print(sum1)
# def s2():
#  if oper == "-":
#     sum2 = num1 - num2
#     blank.append(sum2)
#     print(sum2)
# def s3():
#  if oper == "*":
#     sum3 = num1 * num2
#     blank.append(sum3)
#     print(sum3)
# def s4():
#  if oper == "/":
#     sum4 = num1 / num2
#     blank.append(sum4)
#     print(sum4)

# s1()
# s2()
# s3()
# s4()


#teht7
# def funk1 ():
#     listik = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
#     print(listik[::-1])

# funk1()

#teht8
# listik = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
# def funk1 ():
    # a =  int(input("write the number from what you want to start: "))
    
    # b = int(input("Write how many numbers you want to see after the first number: "))

    # if a in listik:
    #    index = listik.index(a)
    #    b1 = listik.index(b)
    #    index1 = listik.index(a + b)
    #    while index <=index1:
    #        index = index +1
    #        print(index)
    #V2
    # etsittava = 30
 
 
    # lista = [10,20,30,40]
 
    # laskuri = 0
 
    # while laskuri < len(lista):
    #     if lista[laskuri] == etsittava:
    #       print("LOYTYY! PAIKASTA",laskuri)
    #     laskuri += 1

# funk1()

#teht9

# listik = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
# x = 6
# y = 4
# for num in listik:
#     if y > num:
#         print(num)
#     if x < num:
#         print(num)

#teht10
# e = 2
# listik = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9,]

# laskuri = 0
# while laskuri < len(listik):
    
#     if listik[laskuri] == e:
#         print(f"first index {laskuri}")
#         if laskuri + 1 < len(listik) and listik[laskuri + 1] == e:  
#             print(laskuri + 1)
#             break  
#     laskuri += 1 


