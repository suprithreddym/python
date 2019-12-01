import shelve
books = shelve.open("book")
books["recepies"] = {"bit": ["bacon", "lettuce", "tomato", "bread"],
                     "beans_on_toast":["beans", "bread"],
                     "scrambled eggs": ["eggs", "butter", "milk"],
                     "soup":["tin of soup"],
                     "pasta": ["pasta", "cheese"]}
books["maintainace"] = {"stuck":["oil"],
                        "loose": ["gaffer tape"]}

print(books["recepies"]["soup"])
print(books["recepies"]["scrambled eggs"])

print(books["maintainace"]["loose"])

books.close()