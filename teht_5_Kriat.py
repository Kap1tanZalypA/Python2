#TEHT 1
# monkeys = ["James", "Zigmond", "Zhidyara", "Cigan Eblivii"]
# srok = [5, 23, 52, 1475]
# def tyrma (monkeys, srok):
    
#     ottrahat = monkeys + srok
#     print (ottrahat)
    
# tyrma(monkeys, srok)    

#TEHT2 = ?


#TEHT3

# list1 = [1, 2, 34, 5, 8]
# sum = 0
# for nums in list1:
#     sum += nums
# kesk = sum / len(list1)
# print(kesk)

#teht4 
# numbers = [1, 2, 2, 34, 5, 5, 8]
# for i in range(len(numbers) - 1):
#     current_num = numbers[i]
#     next_num = numbers[i + 1]
#     if current_num == next_num:
#         continue
#     print(current_num)
    

#teht5
# numbers = [1, 2, 2, 34, 5, 5, 8]
# numbers.reverse()
# print(numbers)


# numbers = [1, 2, 2, 34, 5, 5, 8]
# print(numbers[7:1:-1])


# #teht6
# numbers = [1, 2, 2, 34, 5, 5, 8]
# for nums in numbers:
#     if nums % 2 == 0:
#         print(nums) 

#teht7
# numbers = [1, 2, 2, 34, 5, 5, 8]

# sorted_numbers = sorted(numbers)

# min_number = sorted_numbers[0]
# max_number = sorted_numbers[-1]

# print(f"The minimum number is {min_number}")
# print(f"The maximum number is {max_number}")


#teht8
# numbers = [1, 2, 2, 34, 5, 5, 8]
# half1_list = len(numbers) // 2
# new_list = numbers[:half1_list]
# new_list2 = numbers[half1_list:]
# print (new_list )
# print(new_list2)'

#teht9
# numbers = [1, 2, 2, -1, -10, 34, 5, 5, 8]
# pos_Nums = []
# for nums in numbers:
#     if nums > 0 :
#         pos_Nums = [nums]
#         print (pos_Nums)

# numbers = [1, 2, 2, -1, -10, 34, 5, 5, 8]

# for nums in numbers[:]:
#     if nums < 0 :
#         numbers.remove(nums)

# print (numbers)

#teht 10


# numbers = [1, 2, 2, -1, -10, 34, 5, 5, 8, 2]

# counts = Counter(numbers)

# print(counts)

#teht11
# numbers = [10, 20, 30, 40, 50]


# item = numbers.pop(2)  
# numbers.insert(4, item)  

# print(numbers)  
# #teht 12
# numbers = [1, 2, 2, 34, 5, 5, 8]

# sorted_numbers = sorted(numbers)


# max_number = sorted_numbers[-2]


# print(f"The maximum number is {max_number}")
#teht 13
numbers = [1, 2, 2, 2, 3, 4, 4, 4, 5, 6]


for i in range(len(numbers) - 2):  
    if numbers[i] == numbers[i+1] == numbers[i+2]:  
        print(f" {numbers[i]}  {i}")
       


#teht14

# autot = ["Mersu", 100, 200 "Lada", 200, "Toyota", 300, "Jeep", 342]


# alilista = [[autot[i], autot[i+1]] for i in range(0, len(autot), 2)]

# print(alilista)

#teht15

# autot = ["Mersu", 100, 3, 4, "Lada", 200, 200, "Toyota", 300, "Jeep", 560, 654, 342]


# puhdas_lista = [item for item in autot if isinstance(item, (str, int))]


# puhdas_lista = [item for item in puhdas_lista if not (isinstance(item, int) and item > 300)]

# print(puhdas_lista)