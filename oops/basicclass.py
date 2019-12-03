class kettle(object):

    power_source = "electricity"

    def __init__(self,make,price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = kettle("kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

hamiton = kettle("hamilton", 14.55)

print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamiton.make, hamiton.price))

print("Models: {0.make} = {0.price} , {1.make} = {1.price}".format(kenwood, hamiton))

print(hamiton.on)
hamiton.switch_on() # calling by calue
print(hamiton.on)

kettle.switch_on(kenwood) # using class to call
print(kenwood.on)

print("*" * 80)

kenwood.power = 1.5 # assigning values dynamically using instance
print(kenwood.power)

print("switch to atomic power")
kettle.power_source = "atomic"
print(kettle.power_source)
print("switch to gas")
kenwood.power_source = "gas"
print(kettle.power_source)
print(kenwood.power_source)
print(hamiton.power_source)
print(kettle.__dict__)
print(kenwood.__dict__)
print(hamiton.__dict__)