menu = []
menu.append(["egg", "spam", "beacon"])
menu.append(["egg", "sausage", "beacon"])
menu.append(["egg", "spam"])
menu.append(["egg", "beacon", "spam"])
menu.append(["egg", "beacon", "sausage", "spam"])
menu.append(["spam", "beacon", "sausage", "spam"])
menu.append(["spam", "egg", "spam", "spam", "beacon", "spam"])
menu.append(["spam", "egg", "sausage", "spam"])

for meal in menu:
    if "spam" not in meal:
        print(meal)
        for item in meal:
            print(item)