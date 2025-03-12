#EJERCISIOS DIA 7
#Exercises: Level 2
#Join A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
C = A.union(B)
print("La lista al unir A y B queda asi:", C)

#Find A intersection B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
A.intersection(B)
print("La lista de la interseccion de A y B queda asi:", A.intersection(B))

#Is A subset of B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
subset = A.issubset(B)
print("Es A un subconjunto de B?", subset)

#Are A and B disjoint sets
disjoint = A.isdisjoint(B)

#Join A with B and B with A
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
A_with_B = A.union(B)
print ("La lista al unir A y B queda asi:", A_with_B)
B_with_A = B.union(A)
print("La lista al unir B con A queda asi:", B_with_A)

#What is the symmetric difference between A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
A.symmetric_difference(B)
print("La lista de la diferencia simetrica de A y B queda asi:", A.symmetric_difference(B))

#Delete the sets completely
del A
del B

#Exercises: Level 3
#Convert the ages to a set and compare the length of the list and the set, which one is bigger?
#longitud de las listas
age = [22, 19, 24, 25, 26, 24, 25, 24]
setAge = set(age)
print("Los componentes de la lista Age son:",len(age))
print("Los componentes de la lista SetAge son:",len(setAge))
#comparar cual lista es la mayor
if (len(age) > len(setAge)):
    print ("La lista mayor es: ", age)
if (len(age) < len(setAge)):
    print ("La lista mayor es: ", setAge)

#Explain the difference between the following data types: string, list, tuple and set
string = "Hola :)"
print(string)
list = ["Platano","Sandia","Uva"]
print(list)
tuple = ("Platano","Sandia","Uva")
print(tuple)
set = {'item1', 'item2', 'item3', 'item4'}
print(set)

#I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
oracion = "I am a teacher and I love to inspire and teach people"
conteo_palabras_unicas = oracion.split()
print("Las palabras unicas en la oracion son:", len(conteo_palabras_unicas))
print ("Las palabras unicos en la oracion son:", conteo_palabras_unicas)