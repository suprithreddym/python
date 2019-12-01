shopping_list = ["eggs", "milk" , "pasta" , "spam" , "bread" , "rice"]
# for items in shopping_list:
#     if items == "spam":
#         continue
#
#     print("Buy " + items)

for items in shopping_list:
    if items == "spam":
        break

    print("Buy " + items)