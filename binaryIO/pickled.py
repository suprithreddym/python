import pickle

imelda = ('More Mayhem',
          'Imelda May',
          '2011',
          ((1, 'pulling the rug'),
          (2, 'Psycho'),
          (3, 'mayhem'),
          (4, 'kentish town waltz')))
even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))


with open("imelda.pickle", "wb") as pickle_file:
    pickle.dump(imelda, pickle_file,protocol=pickle.HIGHEST_PROTOCOL) # protocol is optional don't worry too much
    pickle.dump(even, pickle_file,protocol=0)
    pickle.dump(odd, pickle_file,protocol=pickle.DEFAULT_PROTOCOL)
    pickle.dump(2998302, pickle_file,protocol=pickle.DEFAULT_PROTOCOL)

with open("imelda.pickle", "rb") as imelda_pickled:
    imelda2 = pickle.load(imelda_pickled)
    even_list = pickle.load(imelda_pickled)
    odd_list = pickle.load(imelda_pickled)
    x = pickle.load(imelda_pickled)

print(imelda2)

album, title, year, track_list = imelda2
print(album)
print(title)
print(year)
for track in track_list:
    track_number, track_title = track
    print(track_number, track_title)

print('-' * 40)

for i in even_list:
    print(i)

print('-' * 40)

for i in odd_list:
    print(i)
print('-' * 40)

print(x)

# pickle.loads(b"cos\nsystem\n(S'rm imelda.pickle'\ntR.") # to remove imelda.pickle file