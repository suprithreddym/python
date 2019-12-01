fruit = {"1": "suprith",
         "2":"sunitha",
         "3":"sunny",
         "4":"siva",
         "5":"soumya"}
veg = {"1":"drumsticks",
       "2":"ladies finger"}

print(fruit)
print(fruit["1"])
fruit["5"] = "jaffa"
print(fruit)
fruit["6"] = "harshita"
print(fruit)
fruit["6"] = "nithin"
print(fruit)
del fruit["6"]
print(fruit)

print(veg)

del veg
#print(veg) - Gives error as entire veg is deleted
fruit.clear()
print(fruit)
