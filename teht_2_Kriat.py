#Tehtava 1

# string = "i love python programming in python"
# string1 = string.replace("python", "Python")
# print(string1)

#tehtava 2

# string ="Hello Worold"
# x = string.swapcase()
# print(x)

#tehtava 3
# string ="Hello World"
# sliced_string = string[5:11]
# print(sliced_string)



#tehtava 4
# string = "    Python is awesome!  "
# striped_string = string.strip()
# print(striped_string)


#tehtava 5
# text = "Python"
# centered_text = text.center(20, "*")
# print(centered_text)


#tehtava 6
# text = "python is a great language"
# text_title = text.title()
# print(text_title)


#tehtava7
# text =  "banana sandwich"
# text_count = text.count("a")
# print(text_count)

#teht8
# tr1 = ""
  

# str2 = ""
  

# str3 = "eauiyo"
  
 
# trg = "beautiful python"
  

# table = trg.maketrans(tr1, str2, str3) 
  

# print ("The string before translating is : ", end ="") 
# print (trg) 
  

# print ("The string after translating is : ", end ="") 
# print (trg.translate(table)) 

#teht9

# txt = " Python Programming"[::-1]
# print(txt) 

#teht10
import re
string = "I have a cat and a dog"
repl1 = ["cat", "dog"]
new_repl = "animal"


pattern = r'\b(' + '|'.join(repl1) + r')\b'
new_text = re.sub(pattern, new_repl, string)

print(new_text)

