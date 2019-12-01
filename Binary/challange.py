powers = []
for power in range(15, -1, -1):
    powers.append(2 ** power)

print(powers)

x = int(input("please enter the number"))

printing = False

for power in powers:
    bit = x // power
    if bit != 0:
        printing = True
    if printing:
        print(bit, end='')
    x %= power

