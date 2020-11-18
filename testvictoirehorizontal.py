def testeVictoireHorizontale (tictactoe):
	for j in range (0,6):
		if (tictactoe[j]==tictactoe[j+1] and tictactoe[j]==tictactoe[j+2] and j%3==0 and tictactoe[j]!="vide"):
			if (tictactoe[j]=="croix"):
				print("Victoire pour les croix !")
				return True
			if (tictactoe[j]=="rond"):
				print("Victoire pour les ronds !")
				return True
	return False