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
company = 'codificacion para todos'
print(company.find('codificacion'))  
print(company.find('hola')) # 0 #aparece error

company = 'codificacion para todos'
sub_string = 'codificacion'
print(company.index(sub_string))  

#11-Replace the word coding in the string 'Coding For All' to Python.
company = 'codificacion para todos'
print("Ahora la frase remplazando queda asi: ",company.replace('codificacion', 'python')) # 'thirty days of coding'

#12-Change Python for Everyone to Python for All using the replace method or other methods.
texto00 = 'Python for everyone'
print(texto00.replace('everyone', 'all')) 

#13-Split the string 'Coding For All' using space as the separator (split())
company = 'codificacion para todos'
print("Ahora la frase remplazando queda asi: ", company.split())

#14-"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
text01 = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print("Separando la oracion:", text01.split(','))

#15-What is the character at index 0 in the string Coding For All.
company = 'codificacion para todos'
print("La primera letra de la frase es:",company[0])

#16-What is the last index of the string Coding For All.'
company = 'codificacion para todos'
print("La ultima letra de la frase es :", company[-1])

#17-What character is at index 10 in "Coding For All" string.
company = 'codificacion para todos'
print("La decima letra de la frase es :", company[10])

#18-Create an acronym or an abbreviation for the name 'Python For Everyone'.
texto01 = 'Python For Everyone'
acronymo00 = ''.join(word[0] for word in texto01.split())
print("La abreviacion de (Python for Everyone) es:",acronymo00)

#19-Create an acronym or an abbreviation for the name 'Coding For All'.
texto02 = 'Coding For All'
acronymo01 = ''.join(word[0] for word in texto02.split())
print("La abreviacion de (Coding for All) es:", acronymo01)

#20-Use index to determine the position of the first occurrence of C in Coding For All/codicion para todos.
company = 'codificacion para todos'
print("La posicion de la primera letra c en la frase es:", company.index('c'))

#21-Use index to determine the position of the first occurrence of F in Coding For All/codicion para todos.
company = 'codificacion para todos'
print("La posicion de la primera letra f en la frase es:", company.index('f'))

#22-Use rfind to determine the position of the last occurrence of a in Coding For All People./coficacion para todos.
company = 'codificacion para todos'
print("La posicion de la ulima letra a en la frase es:", company.rfind('a'))

#23-Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
texto03=  'No puedes terminar una oración con porque, porque (porque)  es una conjunción'
print("La posicion de la primera palara (porque) en la frase es:", texto03.index('porque')) #primer porque

#24-Use rfind to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
texto03 = 'No puedes terminar una oración con porque, porque (porque)  es una conjunción'
print("La posicion de la ultima palara (porque) en la frase es:", texto03.rfind('porque')) #ultimo porque

#25-Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
texto03=  'No puedes terminar una oración con porque, porque (porque)  es una conjunción'
print(texto03.replace('No puedes terminar una oración con porque, porque (porque)  es una conjunción', 'No puedes terminar una oración con es una conjunción')) # 'thirty days of coding'

#26-Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
texto03 = 'No puedes terminar una oración con porque, porque (porque)  es una conjunción'
print("La posicion de la primera palara (porque) en la frase es:", texto03.index('porque')) #primer porque
print("La posicion de la primera palara (porque) en la frase es:", texto03.find('porque')) #primer porque


#27-Find the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'#correjir
texto03 = 'No puedes terminar una oración con porque, porque (porque)  es una conjunción'
print("La posicion de la primera palara (porque) en la frase es:", texto03.index('porque')) #primer porque
print("La posicion de la primera palara (porque) en la frase es:", texto03.find('porque')) #primer porque

#28-Does ''Coding For All' start with a substring Coding? VERDAD O FALSO si inicio con la palabra codificacion
company = 'codificacion para todos'
print("La frase empieza con la palabra 'codificacion' ?:", company.startswith('codificacion'))

#29-Does 'Coding For All' end with a substring coding? VERDAD O FALSO si termina con la palabra codificacion
company = 'codificacion para todos'
print("La frase termina con la palabra 'codificacion' ?:", company.endswith('codificacion'))

#30-'   Coding For All      '  , remove the left and right trailing spaces in the given string.
company = 'codificacion para todos'
print("La frase sin espacios es:", company.strip())

#31-Which one of the following variables return True when we use the method isidentifier(): 30DaysOfPython, thirty_days_of_python, 'thirty_days_of_python', '30_days_of_python'
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())
print('thirty_days_of_python'.isidentifier())
print('30_days_of_python'.isidentifier())

#32-The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
text04 = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("La lista de unas librerias de python es:", ' , '.join(text04))

#33-Use the new line escape sequence to separate the following sentences. 'I am enjoying this challenge. I just wonder what is next.'