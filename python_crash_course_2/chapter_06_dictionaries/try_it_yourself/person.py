#!/usr/bin/python3

anjas_infos = {'first_name': 'anja', 'lastname': 'boettcher', 'age': 36, 'high': 170, 
	'home': 'berlin', 'work': 'web design'
}

print(f"[*] Name: {anjas_infos['first_name'].title()}")
print(f"[*] Lastname: {anjas_infos['lastname'].title()}")
print(f"[*] Home: {anjas_infos['home'].title()}")
print(f"[*] Age: {anjas_infos['age']}")
print(f"[*] Work: {anjas_infos['work'].title()}")


print(f"[*] Name: {anjas_infos.get('first_name', 'No key with that value').title()}")
