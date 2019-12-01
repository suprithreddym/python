age = 24
print("my age is " + str(age))
print("my age is {0} years".format(age))
print("there are {0} days in {1}, {2}, {3}".format(31, "jan" , "mar", "may"))
print("""january: {2}
feb: {0}
mar: {2}
apr: {1}
may: {2}
""".format(28,30,32))
print("my age is %d years" % age)
print("my age is %d %s, %d %s" % (age, "years", 6, "months"))
for i in range(1, 12):
    print("no. %2d is squared %4d is cubed %4d" %(i, i ** 2, i ** 3))

print("pi is approximately %.50f" %(22/7))

for i in range(1, 12):
    print("no. {0:2} is squared {1:4} is cubed {2:4}".format(i, i ** 2, i ** 3))
for i in range(1,13):
    print("no. {0:2} squared is {1:<4} is cubed {2:<4}".format(i, i ** 2, i **3))

print("pi is appriximately {0:.50}".format(22/7))

