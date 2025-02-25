#1-Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
sentence0 =  '30 dias de python'
print (sentence0)

#2-Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'
sentence1 = 'Codificacion para todos' 
print (sentence1)

#3-Declare a variable named company and assign it to an initial value "Coding For All".
company = 'codificacion para todos'

#4-Print the variable company using print().
print (company)

#5-Print the length of the company string using len() method and print().
print("La longitud de company es:",len(company))

#6-ange all the characters to uppercase letters using upper() method.
company = 'codificacion para todos'
print(company.upper()) 

#7-Change all the characters to lowercase letters using lower() method.company = 'codificacion para todos'
company = 'CODIFICACION PARA TODOS'
print(company.lower()) 

#8-Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
company = 'codificacion para todos'
print(company.capitalize()) 

company = 'codificacion para todos'
print(company.title())

companye = 'codificacion para todos'
print(company.swapcase())   
company = 'Codificacion Para Todos'
print(company.swapcase())  

#9-Cut(slice) out the first word of Coding For All string.
company = 'codificacion para todos'
last_three = company[12:24]
print(last_three)

#10-Check if Coding For All string contains a word Coding using the method index, find or other methods.