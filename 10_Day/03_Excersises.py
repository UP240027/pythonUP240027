#Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
import paises02 as p
paises02 = p.countries
for pais in paises02:
    if 'land' in pais:
        print("Paises que llevan 'land' en su nombre :", pais)

#his is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
lista = ['banana', 'orange', 'mango', 'lemon']
for fruta in reversed(lista):
    print("La lista de frutas al reves queda asi:", fruta)

#Go to the data folder and use the countries_data.py file.Loop through the countries and extract all the countries containing the word land.
import countries_data as cd
paises = cd.countries
for pais in paises:
    if 'land' in pais:
        print("Paises que llevan 'land' en su nombre :", pais) 

#What are the total number of languages in the data
import countries_data as cd
paises = cd.countries
total = 0
