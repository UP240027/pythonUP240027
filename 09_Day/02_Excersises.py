#Excersises level 2 DIA 9
#Write a code which gives grade to students according to theirs scores:
calificacion_del_alumno = int(input("Ingresa tu calificacion:"))
if calificacion_del_alumno > 80 and calificacion_del_alumno == 100 :
    print("Tu nota es (A)")
if calificacion_del_alumno >= 70 and calificacion_del_alumno <= 89 :
    print("Tu nota es (B)")
if calificacion_del_alumno >= 60 and calificacion_del_alumno <= 69:
    print("Tu nota es (C)")
if calificacion_del_alumno >= 50 and calificacion_del_alumno <= 59:
    print ("Tu nota es (D)")
if calificacion_del_alumno >= 0 and calificacion_del_alumno <= 49:
    print ("Tu nota es (F)")

 #Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
mes = str(input('Ingresa el mes en el que estas: '))
verano = 'Junio, julio, agosto'
otono = 'septiembre, octubre, noviembre'
invierno = ' Diciembre, enero, febrero'
primavera = 'Marzo, abril, mayo'
if mes in verano:
    print('La estacion en la que estas es: verano')
elif mes in otono:
    print ('La estacion en la que estas es: es otono')
elif mes in invierno:
    print ('La estacion en la que estas es: invierno')
elif mes in primavera:
    print('La estacion en la que estas es: primavera')

 #The following list contains some fruits:
 #If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'naranja', 'mango', 'limon']
ingresa_fruta = str(input("Ingresa una fruta que creas que este en la lista : "))
if ingresa_fruta in fruits:
    print("La fruta ya existe en la lista")
else :
    print ("La fruta no existe en la lista")



