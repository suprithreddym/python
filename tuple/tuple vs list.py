#tuples

welcome = "welcome to my nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", "Bad Company"
budgie = "Nightflight", "Budge", 1981
imelda = "More Mayhem", "emelda may", 2011
metallica = "Ride the lightening", "metallica", 1984

print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])

#metallica[0] = "master of puppets" this gives error
imelda = imelda[0], "imelda may", imelda[2]
print(imelda)

# unpacking tuple
title, artist, year = imelda
print(title)
print(artist)
print(year)

#list

metallica2 = ["ride the lightening", "Metallica", 1984]
metallica2.append("test")
print(metallica2)
metallica2[0] = "master of puppets"
print(metallica2)