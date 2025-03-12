#EJERCISIOS DIA 7
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

