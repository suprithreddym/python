#tuple

imelda = "more mayhem", "imelda may", 2011, ((1, "pulling the rug"), (2, "psycho"), (3, "mayhem"), (4, "kentish town waltz") )

print(imelda)

title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
for song in tracks:
    track, title = song
    print("\tTrack number {}, Title: {}".format(track, title))

# mix of tuple and list

imelda = "more mayhem", "imelda may", 2011, [(1, "pulling the rug"), (2, "psycho"), (3, "mayhem"), (4, "kentish town waltz") ]

print(imelda)

imelda[3].append((5, "all is you"))
title, artist, year, tracks = imelda
tracks.append((6,"end of list"))
print(title)
print(artist)
print(year)
for song in tracks:
    track, title = song
    print("\tTrack number {}, Title: {}".format(track, title))