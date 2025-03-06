#1-Declara una lista vacia
lista_vacia = []
print(len(lista_vacia)) #comrpueba la lista vacia

#2Declara una lista con 5 elementos/ lista con 5 componentes
colores = ['azul', 'verde', 'rosa', 'amarillo', 'rojo','morado']
print ("Los colores de la lista son:", colores)

#3-Encuentra la longitud de la lisa/ cuantos componentes tiene la lista
print("La longitud/componentes de la lista de colores es:", len(colores))

#4-Obten el primer elemento, el del medio y el ultimo de lista/ contando desde 0 los elementos de la lista
primer_color_de_la_litsta = colores[0]
print("El primer color de la lista es", primer_color_de_la_litsta)
color_de_en_medio_de_la_lista = colores[2]
print("El color de en medio de la lista es:", color_de_en_medio_de_la_lista)
ultimo_color_de_la_lista = colores[5]
print("El ultimo color de la lista es:", ultimo_color_de_la_lista)

#5-Declara una lista llamada mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Jessica', 18, 1.60, False, 'Aguascalientes']
print("Los datos de la lista son:", mixed_data_types)   


#6-Declara una lista llamada  it_companies y agrega estos componentes a ella: values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print("Las empresas de la lista son:", it_companies)

#7-Print the list using print()
print(it_companies)

#8-Print the number of companies in the list
print("El numero de empresas que hay en la lista es:", len(it_companies))

#9-Print the first, middle and last company
primer_empresa =it_companies[0]
print("La primera empresa de la lista es:", primer_empresa)
empresa_del_medio = it_companies[3]
print("La empresa del medio de la lista es", empresa_del_medio)
ultima_empresa = it_companies[6]
print("La ultima empresa de la lista es:", ultima_empresa)

#10-Print the list after modifying one of the companies
it_companies[2] = 'Instagram'
print("La lista de empresas despues de modificar una de ellas es:", it_companies)

companies = 'Facebok / Google / Microsoft / Apple / IBM / Oracle / Amazon'
print(companies.replace(' Microsoft', 'Instagram'))
print("La lista de empresas despues de modificar una de ellas es:", it_companies)

#11-Add an IT company to it_companies
it_companies.append('Twitter') #AGREGAR ELEMENTO AL FINAL DE LA LISTA 
print("La lista de empresas despues de agregar una de ellas es:", it_companies)

#12-Insert an IT company in the middle of the companies list
it_companies.insert(3, 'Linkedin') #AGREGAR ELEMENTO EN EL MEDIO DE LA LISTA
print("La lista de empresas despues de agregar una de ellas es:", it_companies)

#13-Change one of the it_companies names to uppercase (IBM)
it_companies = 'Facebook / Google / Instagram / Linkedin / APPLE / IBM / Oracle / Amazon / Twitter'
print("La lista de empresas en mayusculas es:", it_companies.upper())

#14-Join the it_companies with a string '#; '#PENDIENTE
it_companies = 'Facebook / Google / Instagram / Linkedin / APPLE / IBM / Oracle / Amazon / Twitter'

#15-Check if a certain company exists in the it_companies list.
it_companies = ['Facebook', 'Google', 'Instagram', 'Linkeding', 'Apple', 'IBM', 'Oracle', 'Amazon', 'Twitter']
does_exist = 'Facebook' in it_companies
print("La palabra (Facebook) existe en la lista?", does_exist) 
does_exist = 'X' in it_companies
print("La palabra (x) existe en la lista?", does_exist)

#16-Sort the list using sort() method
it_companies = ['Facebook', 'Google', 'Instagram', 'Linkeding', 'Apple', 'IBM', 'Oracle', 'Amazon', 'Twitter']
it_companies.sort()
print("La lista ordenada es:", it_companies)

#17-Reverse the list in descending order using reverse() method
it_companies = ['Facebook', 'Google', 'Instagram', 'Linkeding', 'Apple', 'IBM', 'Oracle', 'Amazon', 'Twitter']
it_companies.sort(reverse=True)
print("La lista con orden en reversa es:", it_companies)

#18-Slice out the first 3 companies from the list
it_companies = ['Facebook', 'Google', 'Instagram', 'Linkeding', 'Apple', 'IBM', 'Oracle', 'Amazon', 'Twitter']
cortar_primeras_tres_empresas = it_companies[3:9]
print("La lista sin las tres primeras empresas queda asi:", cortar_primeras_tres_empresas)

#19-Slice out the last 3 companies from the list
it_companies = ['Facebook', 'Google', 'Instagram', 'Linkeding', 'Apple', 'IBM', 'Oracle', 'Amazon', 'Twitter']
cortar_ultimas_tres_empresas = it_companies[:6]
print("La lista sin las tres ultimas empresas queda asi:", cortar_ultimas_tres_empresas)

#20-Slice out the middle IT company or companies from the list
it_companies = ['Facebook', 'Google', 'Instagram', 'Linkeding', 'Apple', 'IBM', 'Oracle', 'Amazon', 'Twitter']
cortar_empresa_del_medio = it_companies[4:5]
print("La lista sin la empresa del medio queda asi:", cortar_empresa_del_medio)

#21-Remove the first IT company from the list
it_companies = ['Facebook', 'Google', 'Instagram', 'Linkeding', 'Apple', 'IBM', 'Oracle', 'Amazon', 'Twitter']
it_companies.remove('Facebook') #remover elemento directo
print("La lista sin la primera empresa queda asi:", it_companies)

#22-Remove the middle IT company or companies from the list
it_companies = ['Facebook', 'Google', 'Instagram', 'Linkeding', 'Apple', 'IBM', 'Oracle', 'Amazon', 'Twitter']
it_companies.remove('Apple') #remover elemento directo
print("La lista sin la empresa del medio queda asi:", it_companies)

#23-Remove the last IT company from the list
it_companies = ['Facebook', 'Google', 'Instagram', 'Linkeding', 'Apple', 'IBM', 'Oracle', 'Amazon', 'Twitter']
it_companies.remove('Twitter') #remover elemento directo
print("La lista sin la ultima empresa queda asi:", it_companies)

#24-Remove all IT companies from the list
it_companies = ['Facebook', 'Google', 'Instagram', 'Linkeding', 'Apple', 'IBM', 'Oracle', 'Amazon', 'Twitter']
it_companies.clear() #remover todos los elementos de la lista
print("La lista sin las empresas queda asi:", it_companies)

#25-Delate the IT companies list
it_companies = ['Facebook', 'Google', 'Instagram', 'Linkeding', 'Apple', 'IBM', 'Oracle', 'Amazon', 'Twitter']
del it_companies #borrar la lista

#26-Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
Unir_listas = front_end + back_end
print("Las listas unidas es:", Unir_listas)

#27-After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
Unir_listas = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']
nueva_lista = Unir_listas.copy()
nueva_lista.insert(5, 'Python') #insertar elemento en la quinta posicion
nueva_lista.insert(6, 'SQL') #insertar elemento en ls sexta posicion
print("La lista con Python y SQL incluidos es:", nueva_lista)

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













