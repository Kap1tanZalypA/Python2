# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         i = 0
#         while sum()
#         if target == nums[i] + nums[i+1]:
#             print(nums[i], nums[i + 1])
#         else:
            
# class Solution:
#     def mergeTwoLists(self, list1 = [1,2,4], list2 = [1,3,4], ):
#         i = 0
#         list3 = []
#         while i < len(list1):
#             if list1[i]== list2[i]:
#                 list3.append(list1[i])
#                 list3.append(list2[i])
#             if list1[i] != list2[i]:
#                 list3.append(list1[i])
#             if list1[i] != list2[i]:
#                 list3.append(list2[i])
#             i+=1
#         return print(list3)

# sol = Solution()
# sol.mergeTwoLists()


# nums = [ 1,1, 2,3,4,4]
# nums2 = []
# for i in range(len(nums)):
#     for q in range(i + 1 , len(nums)):
#         if nums[i] == nums[q]:
#             nums2.append(nums[q])
#         if nums[i] < nums[q]:
#              nums2.append(nums[i])
# print(nums2)


# from typing import List
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
      
#         seen = set()
#         i = 0
#         while i < len(nums):
#             if nums[i] in seen:
#                 del nums[i]
#             else:
#                 seen.add(nums[i])
#                 i += 1
#         return len(nums)
# print('a', 'b', 'c', sep='*')
# print('d', 'e', 'f', sep='**', end='')
# print('g', 'h', 'i', sep='+', end='%')
# print('j', 'k', 'l', sep='-', end='\n')
# print('m', 'n', 'o', sep='/', end='!')
# print('p', 'q', 'r', sep='1', end='%')
# print('s', 't', 'u', sep='&', end='\n')
# print('v', 'w', 'x', sep='%')
# print('y', 'z', sep='/', end='!')

# a = int(input())
# b = a + 1
# c = a - 1 
# print('Следующее за числом', a, 'число:', b)

# print('Для числа', a, 'предыдущее число:', c)


# a = 15 // (16 % 7)
# b = 34 % a * 5 - 29 % 5 * 2
# print(a + b)

# import math
# result = 0
# popul = int(input())

# if popul % 2 == 1:
#     popul = popul / 2
#     result = math.ceil(popul)
#     print(result)
# else:
#     print(popul / 2)

# print(1132 % 2)

# a = int(input())
# print((a-1) // 4 + 1)


# num = int(input())
# a = num % 10
# b = (num % 100) // 10
# c = num // 100

# sum1 = a + b + c
# sum2 = a * b * c
# print("Сумма цифр =", sum1)
# print("Произведение цифр =", sum2)

# inp1 = int(input())

# num1  = inp1 // 100
# num2 = (inp1 % 100) // 10
# num3 = inp1 % 100

# sum1 = num1 + num2 + num3
# sum2 = num1 * num2 * num3

# print("Сумма цифр =", sum1)
# print("Произведение цифр =", sum2)


a, b, c = map(str, input())
print(a + b + c)
print(a + c + b)
print(b + a + c)
print(b + c + a)
print(c + a + b)
print(c + b + a)


