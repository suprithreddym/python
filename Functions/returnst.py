def centre_args(*args, sep=' '): # passing multiple args
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    return " " * left_margin + text


with open("menu","w") as menu:
    s1=centre_args("spam and eggs")
    print(s1, file=menu)
    s2=centre_args("spam, spam and eggs")
    print(s2, file=menu)
    print(centre_args(12),file=menu)

