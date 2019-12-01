# number = "9,223,245,298,300"
# for i in range(0, len(number)):
#     if number[i] in "0123456789":
#         print(number[i])

number = "9,223,245,298,300"
cleanednumber = ''
for i in range(0, len(number)):
     if number[i] in "0123456789":
         cleanednumber = cleanednumber + number [i]
newnumber = int(cleanednumber)
print("the number is {}".format(newnumber))