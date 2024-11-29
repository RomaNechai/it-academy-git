countries = [
    'Russia Moscow Petersburg Novgorod Kaluga',
    'Ukraine Kiev Donetsk Odessa',
    'Belarus Minsk Brest Grodno'
]

cities = ['Grodno', 'Moscow', 'Kiev', 'Petersburg', 'Minsk']


def show_city(nations, towns):
    result_lst = []
    for city in towns:
        for country in nations:
            if city in country:
                country_lst = country.split()
                result_lst.append(country_lst[0])
    return result_lst


result = show_city(countries, cities)

for i in result:
    print(i)
