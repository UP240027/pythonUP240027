#1-Declare an empty list
lista_vacia = []
print(len(lista_vacia)) #comrpueba la lista vacia

#2-Declare a list with more than 5 items/ lista con 5 componentes
colores = ['azul', 'verde', 'rosa', 'amarillo', 'rojo','morado']
print ("Los colores de la lista son:", colores)

#3-Find the length of your list/ cuantos componentes tiene la lista
print("La longitud/componentes de la lista de colores es:", len(colores))

#4-Get the first item, the middle item and the last item of the list/ contando desde 0 los elementos de la lista
primer_color_de_la_litsta = colores[0]
print("El primer color de la lista es", primer_color_de_la_litsta)
color_de_en_medio_de_la_lista = colores[2]
print("El color de en medio de la lista es:", color_de_en_medio_de_la_lista)
ultimo_color_de_la_lista = colores[5]
print("El ultimo color de la lista es:", ultimo_color_de_la_lista)

#5-Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Jessica', 18, 1.60, False, 'Aguascalientes']
print("Los datos de la lista son:", mixed_data_types)   


#6-Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
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

#14-Join the it_companies with a string '#; '
it_companies = 'Facebook / Google / Instagram / Linkedin / APPLE / IBM / Oracle / Amazon / Twitter'

