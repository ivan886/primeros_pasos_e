persona = {
    'nombres':'Monica',
    'apellidos':'Reyes',
    'telefono':'31121654',
    'telefono2':'31121654',
    'telefono3':'31121654',

}

#OPERACIONES
persona.update({'nombres':'Rocio', 'telefono':'1111'})

print(persona.get("nombres"))
'''
print(persona['nombres'])
print(persona['apellidos'])

for llave in persona:
    print(f" {llave}: {persona[llave]}  " )

print(persona.keys())
print(persona.values())
'''