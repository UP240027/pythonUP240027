#Exercises: Level 1 DIA 10
#para
#Iterate 0 to 10 using for loop, do the same using while loop.
conteo   = 0
while conteo < 10 :
    print(conteo)
    conteo = conteo + 1
    if conteo == 10:
        break

for loop in range(11):
    print(loop)

lista = [0, 1, 2, 3, 4, 5, 6, 7,8,9,10]
for numeros in lista: 
    print(numeros) 

#Write a loop that makes seven calls to print(), so we get on the output the following triangle:
#
##
###
####
#####
######
#######
for x in range(1, 8):
    print("#" * x)

#Use nested loops to create the following:

#Print the following pattern:
# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100
for numero in range(11):
    print(f"{numero} x {numero} = {numero * numero}")

#Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
lista_de_lenguajes = ['Python', 'Numpy','Pandas','Django', 'Flask']
for tipo_de_lenguaje in lista_de_lenguajes:
    print(tipo_de_lenguaje)

#Use for loop to iterate from 0 to 100 and print only even numbers
for x in range(101):
    if x % 2 == 0:
        print(x)

#Use for loop to iterate from 0 to 100 and print only odd numbers
for x in range(101):
    if x % 2 != 0:
        print(x)




