#Exercises: Level 1
#Find the length of the set it_companies
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print("La longitud de la lista it companies es",len(it_companies))

#Add 'Twitter' to it_companies
it_companies.add('Twitter')
print("La lista con el nuevo elemento queda asi:", it_companies)

#Insert multiple IT companies at once to the set it_companies
it_companies.add("X")
it_companies.add("Instagram")
it_companies.add("Youtube")
print("La lista con los nuevos elementos agregados queda asi:", it_companies)

#Remove one of the companies from the set it_companies
it_companies.remove("Twitter")
print('La lista sin Twitter queda asi:', it_companies)

#What is the difference between remove and discard
#We can remove an item from a set using remove() method. 
# If the item is not found remove() method will raise errors, 
# so it is good to check if the item exist in the given set. However, discard() method doesn't raise any errors.
#EXAMPLE
it_companies.remove("X")
print("La lista sin X queda asi:", it_companies)

#Discard
it_companies.discard("Instagram")
print("La lista sin Instagram queda asi:", it_companies)

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
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = {22, 19, 24, 25, 26, 24, 25, 24}
print("Los componentes de la lista Age son:",len(age))
print("Los componentes de la lista A son:",len(A))
print("Los componentes de la lista B son:", len(B))
#comparar cual lista es la mayor
if (len(A) > len(B) and len(A) > len(age)):
    print("La lista mayor es A ")
if (len(B) > len(A) and len(B) > len(age)):
    print("La lista mayor es B")
if (len(age) > len(A) and len(age) > len(B)):
    print("La lista mayor es Age")

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