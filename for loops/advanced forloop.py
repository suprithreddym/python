number = "9,234,678,190,700"
cleanednumber = ''
for char in number:
    if char in "0123456789":
        cleanednumber = cleanednumber + char

newnumber = int(cleanednumber)
print("the number is {}".format(newnumber))

for state in ["this","parrot","is","green"]:
    print("this parrot is {}".format(state))
    #print("this parrot is" + state)

for i in range(0,100,5):
    print("i value {}".format(i))

for i in range(101)[::7]:
    print(i)

for i in range(1,5):
    for j in range(1,5):
        print("{} times {} is {}".format(i,j,i*j))
    print("===============")

for i in range(1,5):
    for j in range(1,5):
        print("{} times {} is {}".format(i,j,i*j),end='\t')

quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""
for char in quote:
    if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print(char, end = '')





