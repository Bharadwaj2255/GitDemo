
#write a python program to reverse a string
name = "Bharadwaja"

print(name[8:2:-1])   #by using the slicing on the sting
print("=======================")
print(name[::-1])
print("=======================")
print(name[-1])     #access last character of the string
print("=======================")
Q = reversed(name)
print(Q)   #by using reversed object
print("=======================")
text = "Hey there i'm using watsapp"

textlenght = len(text)-1
while textlenght >= 0:                  #reverse a string by using while loop
    print(text[textlenght], end="")
    textlenght -= 1
print('\n')
#======================================
rev = text.split()
s = rev[::-1]
out = ' '.join(s)
print(out)
print("=======================")
#===========================================
print(text.find("i'm"))
print("=======================")
#===============================
if "i'm using" in text:
    print(True)
else:
    print(False)
print("=======================")
#====================================
