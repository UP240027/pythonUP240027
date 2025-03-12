#Exercises: Level 2
#The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24] #lista desordenada

#Sort the list and find the min and max age 
ages.sort()
print("La lista ordenada es:", ages)
print("La edad minima de la lista  es:", min(ages))
print("La edad maxima de la lista  es:", max(ages))

#Add the min age and the max age again to the list
edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
nueva_lista2 = edades.copy()
nueva_lista2.insert(11, '19') #insertar elemento en la quinta posicion
nueva_lista2 .insert(12, '26') #insertar elemento en ls sexta posicion
print("La lista con la minima  maxima edad incluidos de nuevo es:", nueva_lista2)

#Find the median age (one middle item or two middle items divided by two)
edades = [19, 19, 20, 22, 24, 24, 24, 25, 25, 26]
suma = 24 + 24
print ('La edad media es:', suma/2)

#Find the average age (sum of all items divided by their number )
edades = [19, 19, 20, 22, 24, 24, 24, 25, 25, 26]
sumaedades = 19 + 19 + 20 + 22 + 24 + 24 + 24 + 25 + 25 + 26
promedio = sumaedades/10
print ('la edad promedio es :', promedio)

#Find the range of the ages (max minus min)
edades = [19, 19, 20, 22, 24, 24, 24, 25, 25, 26]
edades.sort()
rango = edades[-1] - edades[0]
print('El rango de edades es:', rango)

#Compare the value of (min - average) and (max - average), use abs() method
edades = [19, 19, 20, 22, 24, 24, 24, 25, 25, 26]
edades.sort()
promedio = 23 #El promdeio que marac en realidad es de 22.8 pero por este motivo lo dejare en 23 porque se acerca mas a este valor por los decimales
min_promedio = abs(edades[0] - promedio)
max_promedio = abs(edades[-1] - promedio)
print('El valor de (min - promedio) es:', min_promedio)
print('El valor de (max - promedio) es:', max_promedio)

#Find the middle country(ies) in the countries list
import paises as p
countries = p.countries
countries.sort()
print(countries)
print('El pais intermedio es:', countries[96])
      
#Divide the countries list into two equal lists if it is even if not one more country for the first half.
import paises as p
p
all_countries = countries[0:193]
mitad_de_paises = countries[0:96]
print('La primera itad de paises es:', mitad_de_paises)
segunda_mitad_de_paises = countries[97:193]
print('La segunda mitad de paises es:', segunda_mitad_de_paises)

#['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
countries2 = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
ultimos_tres_paises = countries2[3:7]
print ('Los ultimos tres paises son:', ultimos_tres_paises)













