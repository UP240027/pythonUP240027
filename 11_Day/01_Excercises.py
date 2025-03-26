#EJERCICIOS DIA 11 N.1
#Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def suma_de_dos_numeros ():
    #elementos 
    num_uno = 2
    num_dos = 3
    total = num_uno + num_dos #accion de la funcion
    print(total)
suma_de_dos_numeros() #mandar a llamar la funcion


#Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
 def area_del_circulo ():
   π = 3.1416
   radio = float(input('Ingresa radio del circulo: ')) 
    area = π * radio * radio
    print("El area de tu circulo es:", area)
 area_del_circulo() #mandar a llamar la funcion 

def areaDelCirculo ():
    radio = 4 
    area = 3.1416 * radio **2
    print(area)
areaDelCirculo()

#Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.


#Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convertir_celsius_a_fahrenheit ():
    #elementos
    celsius = float(input("Ingresa la temperatura en grados celsius que deseas convertir:"))
    conversion = (celsius * 9/5) + 32 #accion de la funcion
    print("La conversion de celsius a fahrenheit es:", conversion)
    convertir_celsius_a_fahrenheit() 


# #Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
# def checar_estacion ():
#     invierno =  {'Enero':'Febrero', 'Marzo' : '.'}
#     primavera = {'Abril':'Mayo', 'Junio':'.'}
#     verano = {'Julio':'Agosto', 'Septiembre':'.'}
#     otoño = {'Octubre':'Noviembre', 'Diciembre':'.'}

#     mes = input("Ingresa el mes que quieres saber la estacion:")
#     if mes in invierno:
#         print("La estacion es Invierno")
#     elif mes in primavera:
#         print("La estacion es Primavera")
#     elif mes in verano:
#         print("La estacion es Verano")
#     elif mes in otoño:
#         print("La estacion es Otoño")
#     else:
#         print("Mes no encontrado")
#     checar_estacion()
    

    # elif mes == "Abril" or mes == "Mayo" or mes == "Junio"
    #     print("La estacion es Primavera")
    # elif mes == "Julio" or mes == "Agosto" or mes == "Septiembre"
    #     print("La estacion es Verano")
    # elif mes == "Octubre" or mes == "Noviembre" or mes == "Diciembre"
    #     print("La estacion es Otoño")
    # else 
    #     print("Mes no valido")
