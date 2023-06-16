num_1 = input("Veuillez saisir le premier nombre : ")
num_2 = input ("Veuillez saisir le deuxième nombre : ")
operator = input("Veuillez choisir un opérateur : ")

if operator == "+" and num_1.isdigit and num_2.isdigit:
    print(f'Le résultat est {int(num_1) + int(num_2)}')
elif operator == "-" and num_1.isdigit and num_2.isdigit:
    print(f'Le résultat est {int(num_1) - int(num_2)}')
elif operator == "*" and num_1.isdigit and num_2.isdigit:
    print(f'Le résultat est {int(num_1) * int(num_2)}')
elif operator == "/" and num_1.isdigit and num_2.isdigit:
    print(f'Le résultat est {int(num_1) / int(num_2)}')
else:
    print("Veuillez entrer des valeurs correctes")
