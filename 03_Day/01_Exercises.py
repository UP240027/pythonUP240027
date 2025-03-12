#1-Declare your age as integer variable
edad =18
print(type(int(edad)),"El valor mi  edad es de:" ,edad)

#2-Declare your height as a float variable
altura =1.60
print(type(float(altura)),"Mi altura es de:" ,altura)

 
#3-Declare a variable that store a complex number
numero_complejo = 3+4j
print(type(complex(numero_complejo)),"El numero complejo es:" ,numero_complejo)

#4-script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = float(input("Ingrese la base del triangulo:"))
altura = float(input("Ingrese la altura del triangulo:"))
area_del_triangulo = base * altura / 2
print ("El area del triangulo es:", area_del_triangulo)

#5-Perimetro de un triangulo
#Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
lado_a = float(input('Ingrese el lado a : '))
lado_b = float(input('Ingrese el lado b : '))
lado_c = float(input('Ingrese el lado c : '))
perimetro_del_triangulo = lado_a + lado_b + lado_c
print ("El perimetro del triangulo es:", perimetro_del_triangulo)

#6-Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
largo = float(input('Ingresa el largo del rectangulo: '))
ancho = float(input('Ingresa el ancho del rectangulo: '))
area_del_rectangulo = largo * ancho
perimetro_del_rectangulo = 2 * (largo + ancho)
print ("El area del rectangulo es:", area_del_rectangulo)
print ("El perimetro del rectangulo es:", perimetro_del_rectangulo)

#7-Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radio = float(input('Ingresa el radio del circulo: '))
pi = 3.14
area_del_circulo = pi * radio ** 2
circunferencia_del_circulo = 2 * pi * radio
print ("El area del circulo es:", area_del_circulo)
print ("La circunferencia del circulo es:", circunferencia_del_circulo)

##8-Pendiente de interseccion con el eje x and y
##Para calcular los ejes de interseccion se debe despejar en la ecuacion la x, y 
x = 0
yc=2*x-2
print("El valor de y es: ", yc)
y = 0
xc = (y + 2)/2
print("El valor de x es: ", xc)
print('El valor de la pendiente es: (' + str(xc) +' , '+ str(yc)+')')

## Encontrar la pendiente y y la distancia euclidiana entre el punto (2, 2) y el punto (6, 10).
x1 = 2
y1 =2
x2 = 6
y2 = 10
m = (y2-y1)/(x2-x1)
print ('La pendiente es: ', m)
d = ((x2 - x1)*2 + (y2 - y1)*2)
res = d**0.5
print ('La distancia euclidiana es de: ',res)


#10-comparar pendientes. PENDIENTE

##11- Calcula el valor de y (y = x^2 + 6x + 9). 
x = 0
y = x**2 + 6*x + 9
print ('El valor de la variabale y es: ', y)
xuno = 3
yuno = xuno**2 + 6*xuno + 9
print ('El valor de la variabale y es: ', yuno)
xdos = 5
ydos = xdos**2 + 6*xdos + 9
print ('El valor de la variabale y es: ', ydos)

#12-Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print('El numero de letras que tiene dragon es: ', len('dragon'))
print('El numero de letras que tiene python es: ', len('python'))  
print(len('dragon') != len('python'))  # False

#13-Use and operator to check if 'on' is found in both 'python' and 'dragon'
palabra1 = 'python'
palabra2 = 'drangon'
if 'on' in palabra1 and 'on' in palabra2:
    print("'on' se encuentra en ambos 'python' y 'dragon'")
else:
    print("'on' no se encuentra en ambos 'python' y 'dragon'")

#14-Use in operator to check if jargon is in the sentence.
frase1 = 'Espero que este curso no esté lleno de jerga'
print('jerga in Espero que este curso no esté lleno de jerga', 'jerga' in 'Espero que este curso no esté lleno de jerga')

#15-There is no 'on' in both dragon and python
print('ON in dragon', 'ON' in 'dragon')
print('ON in python', 'ON' in 'python')

#16-Find the length of the text python and convert the value to float and convert it to string
palabras = 'python'
print('El numero de letras que tiene python es: ', len('python'))
print (type(float(len(palabras))))

#17-Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
numero1 = 4
numero2 = 6
numero3 = 7
numero4 = 25
frase1 = 'Divisible entre 2'
frase2 = 'No es divisible entre 2 y el resultado es 0 '
sum = numero1/2
print('El numero es: ', frase1, sum )
sum2 = numero2/2
print('El numero es: ', frase1, sum2 )
sum3 = numero3/2
print('El numero es: ', frase2, 0)
sum4 = numero4/2
print('El numero es: ', frase2, 0)

# #18-Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
num = 7
div = 3
division = num/div
print(type(int(division)))
print('El resultado de la division no es 2,7: ', not True)
print('El valor de la division es: ', int(division))

# prueba = (7//3== int(2.7))
# print(prueba) 

# #19-Check if type of '10' is equal to type of 10
# resultado = (type('10') == type(10))
# print(resultado) 
print('El tipo de 10 es igual al tipo de 10: ', type(10) == type(10))


#20-Check if int('9.8') is equal to 10
valor = '9.8'
print(type(float(valor)))
print('El valor del numero es: ', valor)
print('El valor de 9.8 es igual a 10: ', not True)


#22-Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
#calcular el salario de la persona?
horas = float(input('Ingrese las horas trabajadas: '))
tarifa = float(input('Ingrese la tarifa por hora: '))
salario = horas * tarifa
print('El salario de la persona es de: ', salario)


#23-Write a Python script that displays the following table
años = float(input('Ingrese la cantidad de años: '))
segundos = años * 365 * 24 * 60 * 60
print('La cantidad de segundos que puede vivir una persona es de: ',segundos)

#REVISADO
print("Revisado")