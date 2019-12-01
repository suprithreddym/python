import shelve

with shelve.open("bike") as bike:
    bike["name"] = "Honda"
    bike["model"] = "250 dream"
    bike["color"] = "blue"
    bike["engine_size"] = 250

    #del bike["engine sizw"] # shelve stores everything if we by mistake give names
    #del bike["engine size"]
    for key in bike:
        print(key)

    print("=" * 40)

    print(bike["engine_size"])
    print(bike["color"])