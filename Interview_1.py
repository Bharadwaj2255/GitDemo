import re


a = [111222333444555]

num_str = str(a[0])
print(num_str)
print("--------------------------->>")
# output = ''.join([num_str[i:i+3] + 'A' for i in range(0, len(num_str), 3)])

for i in range(0, len(num_str), 3):
    output = ''.join(num_str[i:i+3] + "A")
    print(output)
# output = output.rstrip("A")
print("--------------------------->>")

list = []
for i in range(1, 11):
    list.append(i)

print(list)
print("--------------------------->>")
list.insert(2, 15)
print(list)
print("--------------------------->>")

def function():
    print(list[0], list[-1])


function()
print("--------------------------->>")

# the below string extract the email id using regular expressions.

str1 = "Here is the email information - bharadwajmadaka2255@gmail.com, click on email link to navigate to the email page."
email_ptrn = r'[a-zA-Z0-9._%+-]+@[a-zA-Z]+.[a-zA-Z]{2,}'
match = re.search(email_ptrn, str1)
if match:
    print("Email found: ", match.group())
else:
    print("Email not found")
print("--------------------------->>")








