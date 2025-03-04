#Excercises level 1
#1-Create an empty tuple
tupla_vacia = ()
tupla_vacia = tuple ()


#2- Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
tpl1 = ('Jacquline', 'Christopher')

#3-Join brothers and sisters tuples and assign it to siblings
tpl1 = ('Jacquline', 'Christopher','Hola')
tpl2 = ('Britny','Dariana','LOlita')
tpl3 = tpl1 + tpl2
print(tpl3)


#4-How many siblings do you have?
len (tpl2)
print ("El numero de primos son:", len(tpl2))

#5-Modify the siblings tuple and add the name of your father and mother and assign it to family_member
tpl2 = ('Britny','Dariana','LOlita','Vero','Daniel')
miembros_de_la_familia= tpl1 + tpl2
print("Los miembros de la familia son:", miembros_de_la_familia)

# Exercises: Level 2
# Unpack siblings and parents from family_members

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
frutas =('manzana','pera','platano')
vegetales = ('zanahoria','lechuga','espinaca')
productos_animales = ('pollo','res','pescado')
food_stuff_tp = frutas + vegetales + productos_animales 
print("Las tuplas unidas se ven asi:", food_stuff_tp)

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_tp = frutas + vegetales + productos_animales 
lista = list(food_stuff_tp)
print("La lista de las tuplas unidas se ven asi:", lista)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
food_stuff_tp = frutas + vegetales + productos_animales 
todos_los_elementos = food_stuff_tp[0:9] #declarar cuantos elementos tiene la lista
todos_los_elementos = food_stuff_tp[0:] #declarar desde donde se va a cortar
lista_sin_elemento_medio = food_stuff_tp[0:4] + food_stuff_tp[5:9]
print("La lista sin el elemento del medio queda asi:", lista_sin_elemento_medio)

# Slice out the first three items and the last three items from food_staff_lt list
food_stuff_tp = frutas + vegetales + productos_animales 
todos_los_elementos = food_stuff_tp[0:9] #declarar cuantos elementos tiene la lista
lista_sin_los_tres_primeros = food_stuff_tp[ 0:3]
lista_sin_los_tres_ultimos = food_stuff_tp[6:9]
print("La lista de los tres primeros elementos queda asi:", lista_sin_los_tres_primeros)
print("La lista de los tres ultimos elementos queda asi:", lista_sin_los_tres_ultimos)

# Delete the food_staff_tp tuple completely
food_stuff_tp = frutas + vegetales + productos_animales 
del food_stuff_tp
print("La tupla se eliminO")

# Check if an item exists in tuple:
food_stuff_tp= ('manzana', 'pera', 'platano', 'zanahoria', 'lechuga', 'espinaca', 'pollo', 'res', 'pescado')
print('naranja' in food_stuff_tp)   # False


# Check if 'Estonia' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries) # False
# Check if 'Iceland' is a nordic country
print('Iceland' in nordic_countries) # True
