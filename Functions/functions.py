def python_food():
    width = 80
    text = "spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin,text)


def centre_text(text): # passing single arg
    text = str(text)
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin,text)


def centre_args(*args): # passing multiple args
    text = ""
    for arg in args:
        text += str(arg) + " "
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin,text)


def centre_sep(*args, sep=' ', end='\n',file=None,flush=False): # passing multiple args with seperator
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin,text,end=end,file=file,flush=flush)


# call the function


python_food()
centre_text("spam and eggs")
centre_text("spam, spam and eggs")
centre_text(12)
centre_text("spam, spam, spam and spam")
centre_args("first","second",3,4,"spam")
centre_sep("first","second",3,4,"spam",sep=":")