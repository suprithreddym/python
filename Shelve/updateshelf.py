import shelve
#
bit = ["becon", "lettuce", "tomato", "bread"]
# beans_on_toast = ["beans", "bread"]
# scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
# pasta = ["pasta", "cheese"]

with shelve.open('recipes', writeback=True) as recipes:
    # recipes["bit"] = bit
    # recipes["beans_on_toast"] = beans_on_toast
    # recipes["scrambled eggs"] = scrambled_eggs
    # recipes["soup"] = soup
    #
    # temp_list = recipes["bit"] # use this without writeback
    # temp_list.append("butter")
    # recipes["bit"] = temp_list
    #
    # recipes["bit"].append("butter") # append is used with write back
    # recipes["soup"].append("croutons")
    recipes["soup"] = soup
    recipes["bit"] = bit
    recipes.sync() # sync command deletes the cache
    soup.append("cream")

    for snack in recipes:
        print(snack, recipes[snack])


