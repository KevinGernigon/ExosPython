def testeVictoireVerticale (tictactoe):
	for j in range (0,3):
		if (tictactoe[j]==tictactoe[j+3] and tictactoe[j]==tictactoe[j+6] and tictactoe[j]!="vide"):
			if (tictactoe[j]=="croix"):
				print("Victoire pour les croix !")
				return True
			if (tictactoe[j]=="rond"):
				print("Victoire pour les ronds !")
				return True
	return False