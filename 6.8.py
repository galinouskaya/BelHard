countries = {
    'телемелитрямдия': ['нарния'],
    'россия': ['москва', 'питер'],
    'беларусь': ['минск', 'могилев', 'гомель']
}


def find_country(city):
    global countries
    for country, cities in countries.items():
        if city.lower() in cities:
            return country
    return 'страна не найдена'


print(find_country('могилев'))