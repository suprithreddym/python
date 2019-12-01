number = "9, 133, 200 ,144, 300"
cleanednumber = ''
for i in range(0, len(number)):
    if number[i] in "0123456789":
        cleanednumber += number[i] # argument assignment

newnumber = int(cleanednumber)
print(newnumber)

x = 23
x += -1
print(x)

x -= 4
print(x)

x *= 2
print(x)

x //= 4
print(x)

x %= 6
print(x)

greeting = "good"
greeting += "morning "
print(greeting)

greeting *= 5
print(greeting)
