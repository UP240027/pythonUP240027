#Use for loop to iterate from 0 to 100 and print the sum of all numbers.
suma = 0
for x in range(101):
    suma += x
    print(suma)

#Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
suma_nums_pares =0
suma_nums_impares = 0
for x in range(101):
    if x % 2 == 0:
        suma_nums_pares += x
    else:
        suma_nums_impares += x
    print("Suma de numeros pares:", suma_nums_pares)
    print("Suma de numeros impares:", suma_nums_impares)



