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
