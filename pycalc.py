def calculator():
	valeur1 = int(input("Entrez la première valeur : \n"))
	valeur2 = int(input("Entrez la deuxième valeur : \n"))
	modeOp = input("Entrez le mode d'opération : \n s(Somme) \n diff(différance \n m(multiplication) \n d(division \n choix:")

	if modeOp == "s":
		print("résultat :", valeur1 + valeur2)
	elif modeOp == "diff":
		print("résultat :", valeur1 - valeur2)
	elif modeOp == "m":
		print("résultat :", valeur1 * valeur2)
	elif modeOp == "d":
		print("résultat :", valeur1 / valeur2)
	