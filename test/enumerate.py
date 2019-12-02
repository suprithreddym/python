grocery = ['bread','milk','butter']
enumerategrocery = enumerate(grocery)
print(type(enumerategrocery))

print(list(enumerategrocery))

enumerategrocery = enumerate(grocery, 10)
print(list(enumerategrocery))