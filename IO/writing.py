cities = ["Tirupathi", "vijayawada", "Nellore", "Guntur", "Hyderabad"]
with open("cities.txt", 'w') as city_file:
    for city in cities:
        print(city, file=city_file)

cities1 = []
with open("cities.txt", 'r') as city_file:
    for city in city_file:
        cities1.append(city.strip('\n'))
print(cities1)
for city in cities1:
    print(city)