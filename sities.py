def city_contry (sity_name='Santiago', country_name='Chilie'):
    city=f"{sity_name}, {country_name}"
    return city.title()
city_choose=city_contry('Moscow','russia')
print(city_choose)
city_choose=city_contry()
print(city_choose)