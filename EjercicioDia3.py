#Operaciones artimeticas en Python

print('Addition: ', 1 + 2)
print('Subtraction: ', 2 - 1)
print('Multiplication: ', 2 * 3)
print ('Division: ', 4 / 2)                         # Division in python gives floating number
print('Division: ', 6 / 2)
print('Division: ', 7 / 2)
print('Division without the remainder: ', 7 // 2)   # gives without the floating number or without the remaining
print('Modulus: ', 3 % 2)                           # Gives the remainder
print ('Division without the remainder: ', 7 // 3)
print('Exponential: ', 3 ** 2)                     # it means 3 * 3

# Numeros Flotantes
print('Floating Number,PI', 3.14)
print('Floating Number, gravity', 9.81)

# Numeros Complejos
print('Complex number: ', 1 + 1j)
print('Multiplying complex number: ',(1 + 1j) * (1-1j))

# Declaring the variable at the top first
a = 3 
b = 2 

# Asignar un resultado a una variable mediante operaciones aritmeticas

#suma
total = a + b
#resta
diff = a - b 
#multiplicacion
product = a * b 
#division
division = a / b
#numero restante de un problema de division
remainder = a % b

floor_division = a // b
#exponencial al cuadrado
exponential = a ** b


print(total) 
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)

# Declarar valores y organizarlos juntos
num_one = 3
num_two = 4

# Otra manera de hacer las operaciones aritmeticas a partir de los valores declarados
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_two
remainder = num_two % num_one

# Imprimir los valores con una un indicador de que operacion se realizo 
print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)

# Para calcular el area de un circulo se utiliza la formula pi*r^2
radius = 10                                 # dato= radio de un circulo
area_of_circle = 3.14 * radius ** 2        
print('Area of a circle:', area_of_circle) #imprimir el area del circulo calculado

# Calcular el area de un rectangulo
length = 10
width = 20
area_del_rectangulo = length * width
print('Area del Rectangulo:', area_del_rectangulo)

# Calcular el peso de un objeto
masa = 75
gravedad = 9.81
peso = masa * gravedad
print(peso, 'N')


# Comparaciones
print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False

#Comparaciones  Booleanas
print('True == True: ', True == True) 
print('True == False: ', True == False) 
print('False == False:', False == False) 
print('True and True: ', True and True) 
print('True or False:', True or False)

# Otra manera de comparar
print('1 is 1', 1 is 1)                   # True - because the data values are the same
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
print('B in Asabeneh', 'B' in 'Asabeneh') # False -there is no uppercase B
print('coding' in 'coding for all') # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statement is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False
