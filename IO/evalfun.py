# imelda = "More Mayhem", "imelda may", "2011", (
#     (1, "pulling the rug"), (2, "psycho"), (3, "mayhem"), (4, "Kentish Town Waltz"))
#
# with open("imelda.txt", 'w') as imelda_file:
#     print(imelda, file=imelda_file)

with open("imelda.txt", "r") as imelda_file:
    contents = imelda_file.readline()

imelda = eval(contents)

print(imelda)
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)