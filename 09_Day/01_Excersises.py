#EJERCISIOS DIA 9
#Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
edad_del_usuario = int(input('Ingresa tu edad: '))
if edad_del_usuario == 18:
    print ('Eres lo suficiente mayor para  poder manejar')
if edad_del_usuario > 18:
    print('Eres lo suficiente mayor para  poder manejar')
if edad_del_usuario < 18:
    print ("Espera mas anios para poder manejar")

#Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
mi_edad = 18
edad_del_usuario = int(input('Ingresa tu edad: '))


if edad_del_usuario > mi_edad :
    print("Tu eres mayor que yo")
else:
    print("Tu eres menor que yo")


#Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
numero_01 = float(input('Ingresa un numero: '))
numero_02 = float(input('Ingresa otro numero: '))

if numero_01 > numero_01 :
    print("El primer numero ingresado es mayor al segundo")

if numero_02 > numero_01 :
    print("El segundo numero ingresado es mayor al segundo")

if numero_01 == numero_02 :
    print ("Los numeros ingresados son los mismos")
