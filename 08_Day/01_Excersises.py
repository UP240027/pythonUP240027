#Create an empty dictionary called dog
dog = {}
#Add name, color, breed, legs, age to the dog dictionary
dog =  {'white':'beagle', '4 legs':'3 years'}
print ("La descripcion de el diccionario perro queda asi:",dog)
#Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
estudiante = {
    'first_name':'Jessica',
    'last_name':'Mejia',
    'age':18,
    'country':'Mexico',
    'is_marred':False,
    'skills':{'elemento1': 'elemento2'},
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print("La descripcion del estudiante queda asi:", estudiante)

#Get the length of the student dictionary
print("La cantidad de datos del estudiante son:", len(estudiante))

#Get the value of skills and check the data type, it should be a list
skills = {'elemento1','elemento2', 'elemnto3','elemento4',}
print (len (skills))
#checar que tipo de datos son (lista) pendiente


#Modify the skills values by adding one or two skills
estudiante = {
    'first_name':'Jessica',
    'last_name':'Mejia',
    'age':18,
    'country':'Mexico',
    'is_marred':False,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],   
      'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }

#Get the dictionary keys as a list
estudiante = {
    'first_name':'Jessica',
    'last_name':'Mejia',
    'age':18,
    'country':'Mexico',
    'is_marred':False,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],   
      'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
keys = estudiante.keys()
print(keys)

#Change the dictionary to a list of tuples using items() 
estudiante = {
    'first_name':'Jessica',
    'last_name':'Mejia',
    'age':18,
    'country':'Mexico',
    'is_marred':False,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],   
      'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }

print(estudiante.items())

#Delete one of the items in the dictionary
estudiante = {
    'first_name':'Jessica',
    'last_name':'Mejia',
    'age':18,
    'country':'Mexico',
    'is_marred':False,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],   
      'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
del estudiante['last_name']

#Delete one of the dictionaries
estudiante = {
    'first_name':'Jessica',
    'last_name':'Mejia',
    'age':18,
    'country':'Mexico',
    'is_marred':False,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],   
      'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
del estudiante


