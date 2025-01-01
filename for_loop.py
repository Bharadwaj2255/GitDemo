
# val = 2
# for i in range (1, 11):
#     mul = i * val
#     print(f"{i} x {val} = {mul}")


# for i in range(5, 0, -1):
#     for j in range(i):
#         print("* ", end="")
#     print()

# for i in range (50):
#     if i%2 == 1:
#         print(i)


C = [11002235680020054020000300]
text = str(C)
print(text.count("00"))

count = 0
for i in range(len(text) - 1):
    if text[i:i+2] == "00":
        count += 1
print(count)









