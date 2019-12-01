#suprith = open("/Users/suprithmekala/Documents/python/IO/sample.txt",  'r')

# suprith = open("sample.txt", 'r')
# for line in suprith:
#     if "jabberwock" in line.lower():
#         print(line, end='')
#
# suprith.close()

# with open("sample.txt", 'r') as suprith: # with statement don't need to be closed
#     for line in suprith:
#         if "JAB" in line.upper():
#             print(line, end='')
#
# with open("sample.txt", 'r') as suprith:
#     lines = suprith.readlines()
#     print(lines) # convert to lists
#     for line in lines:
#         print(line, end='')

with open("sample.txt", 'r') as suprith:
    lines = suprith.readlines()
    print(lines) # convert to lists
    for line in lines[::-1]:
        print(line, end='')