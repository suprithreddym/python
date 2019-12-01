with open("sample.txt", 'r') as suprith:
    line = suprith.readline()
    while line:
        print(line, end='')
        line = suprith.readline()
