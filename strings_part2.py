import random

text = "Hey there i'm using watsapp!"
Name = "Bharadwaja"
Act = "202015"

Low_text = text.upper()
# print(text.upper())
print(Low_text)
print(Low_text.lower())
print(Low_text.title())

print("=======================")
print(Name.isalpha())   #isalpha returns True value only if string contains pure characters without any numbers, speacial chars, or white spaces
print(Act.isdigit())    #isdigit returns True value only if string contains pure numbers without any alphabets, speacial chars, or white spaces
print(Name.isspace())
print(Name.count('a'))
print(text.find("watsapp"))
# text.replace("watspp", "facebook")
updated_text = text.replace(text[20:27], "Instagram")
print(updated_text)

My_list = [1, 2, 3, 4]
My_list.extend([5, 6, "bharadwaj"])
print(My_list)

nested_list = [[1, 2], [3, 4], [5, 6]]
flat_list = [item for sublist in nested_list for item in sublist]
print(flat_list)

print(random.choice(My_list))

result = []
for i in range(0, len(text), 3):
    result.append(text[i:i+3])

print(result)

