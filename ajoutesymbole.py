def ajoutesymbole (tictactoe, i) :
	if (tictactoe[i]=="croix" or tictactoe[i]=="rond"):
		print("Cette case est déjà occupée, veuillez saisir une case vide.")
	if (tictactoe[i]=="vide" and joueur%2==0):
		tictactoe[i] = "croix"
	if (tictactoe[i]=="vide" and joueur%2!=0) :
		tictactoe[i] = "rond"
	return