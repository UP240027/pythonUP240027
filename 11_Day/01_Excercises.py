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
def areaDelCirculo ():
    radio = float(input('ingresa un radio: '))
    area = 3.1416 * radio **2
    print("El area de tu circulo es :", area)
areaDelCirculo() 

#Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.


#Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def celsius_a_fahrenheit ():
    #elementos
    celsius = float(input("Ingresa la temperatura en grados celsius que deseas convertir:"))
    conversion = (celsius * 9/5) + 32 #accion de la funcion
    print("La conversion de celsius a fahrenheit es:", conversion)
celsius_a_fahrenheit() 


# #Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def checar_estacion():
    mes = str(input('ingresa un mes: '))
    verano = 'junio, julio, agosto'
    otono = 'septiembre, octubre, noviembre'
    invierno = ' diciembre, enero, febrero'
    primavera = 'marzo, abril, mayo'
    if mes in verano:
        print('La estacion es verano')
    elif mes in otono:
        print ('La estacion es otono')
    elif mes in invierno:
        print ('La estacion es invierno')
    elif mes in primavera:
        print('La estacion es primavera')
checar_estacion()

#Write a function called calculate_slope which return the slope of a linear equation
def calcular_pendiente ():
    #elementos
    x1 = int(input('ingresa un valor entero para x1: '))
    x2 = int(input('ingresa un valor entero para x2: '))
    y1 = int(input('ingresa un valor entero para y1: '))
    y2 = int(input('ingresa un valor entero para y2: '))
    resultado_pendiente = (y2-y1)/(x2-x1) #accion de la funcion
    print("La pendiente de la ecuacion es :", resultado_pendiente)
    pendiente = '(y2-y1)/(x2-x1)'
    print("La ecuacion lineal es:", pendiente)
calcular_pendiente()

#Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def resolver_ecuacion_cuadratica ():
    a = float(input('ingresa un valor para a: '))
    b = float(input('ingresa un valor para b: '))
    c = float(input('ingresa un valor para c: '))
    x1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
    x2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)
    print("Las soluciones de la ecuacion cuadratica son:", x1, x2)
resolver_ecuacion_cuadratica()

#Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def imprimir_lista ():
    lista = ['perro', 'gato', 'pez', 'loro']
    print(lista)
imprimir_lista()

#Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def invertir_lista ():
    lista = ['perro', 'gato', 'pez', 'loro']
    lista.reverse()
    print(lista)
invertir_lista()

#Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalizar_lista ():
    lista = ['perro', 'gato', 'pez', 'loro']
    lista = [x.capitalize() for x in lista]
    print(lista)
capitalizar_lista()

#Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end
