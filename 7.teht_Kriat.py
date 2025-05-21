
def  p():
 import random
 file = open("Luvut.luv", "w")
 list1 = []
 i = 0
 while len(list1) < 10:
      i = i +1
      number =random.randint(100, 200) 
      list1.append(number)
      if number % 2 == 0:
           
           file.write(f"{i}:{number} parillinen \n" )
      else:
          
          file.write(f"{i}:{number} pariton \n")
 file.close
p()


#teht2
pari_l= []
pariton = [] 
# while True:
#     with open('Luvut.luv') as f:
#         if 'parillinen' in f.read():





def print_lines_with_word(file_path, word, word2):
        with open(file_path, 'r', encoding='utf-8
60 
61 
62 
63 
64 
') as file:
            for line in file:
                if word in line:
                    # print(line.strip())
                    pari_l.append((line.strip()))
                    print(pari_l)
                elif word2 in line:
                    pariton.append((line.strip()))
                    print(pariton)
    
file_path = 'Luvut.luv'
word = 'parillinen'

# print_lines_with_word(file_path, word)

# def print_lines_with_word(file_path, word):
#         with open(file_path, 'r', encoding='utf-8') as file:
#             for line in file:
#                 if word in line:
#                     # print(line.strip())
#                     pariton.append((line.strip()))
#                     print(pariton)
    



word2 = 'pariton'

print_lines_with_word(file_path, word, word2)


with open('Parillinen.luv', 'w') as file:
    for name in pari_l:  
        file.write(f"{name}\n")



with open('Pariton.luv', 'w') as file:
    for name2 in pariton:  
        file.write(f"{name2}\n")



        



    
   