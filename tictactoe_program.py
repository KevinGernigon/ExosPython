while (tour >= 0 and tour <=8):
	visuel(tictactoe)
	choixcase = int(input("Veuillez saisir une case de 1 à 9 \n"))
	choixcase = choixcase-1
	ajoutesymbole(tictactoe,choixcase)
	if (testeVictoireVerticale(tictactoe)==True or testeVictoireHorizontale(tictactoe)==True or testeVictoireDiagonale(tictactoe)==True):
		visuel(tictactoe)
		break
	joueur = joueur+1
	tour = tour+1
	if (tour==9 and testeVictoireVerticale(tictactoe)==False and testeVictoireHorizontale(tictactoe)==False and testeVictoireDiagonale(tictactoe)==False ):
		print("Match Nul !")
		visuel(tictactoe)
input()