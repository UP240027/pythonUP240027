#Exercises: Level 3 DIA 9
 # Here we have a person dictionary. Feel free to modify it!
person={
    'first_name': 'Jessi',
    'last_name': 'Mejia',
    'age': 18,
    'country': 'Mexico',
    'is_marred': False,
    'skills': ['Proteus', 'Python', 'JavaScript', 'Autocad','Fusion 360','React'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

 # Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person:
    print(person['skills'][2])
 # Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills' in person:
    if 'Python' in person['skills']:
        print('Python esta en la lista de habilidades')
 # If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
if 'skills' in person:
    if 'JavaScript' in person['skills'] and 'React' in person['skills'] :
        print('He is a front end developer')
    elif 'Npde' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
        print('He is a backend developer')
    elif 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
        print('He is a fullstack developer')
    else:
        print('unknown title')
 # If the person is married and if he lives in Finland, print the information in the following format:
    person02={
    'first_name': 'Maria',
    'last_name': '02',
    'age': 18,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['Proteus', 'Python', 'JavaScript', 'Autocad','Fusion 360'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
if person02['is_marred'] == True and person02['country'] == 'Finland':
    print("Asabeneh Yetayeh lives in Finland and He is married")