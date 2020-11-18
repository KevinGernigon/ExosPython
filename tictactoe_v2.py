tictactoe = ["vide","vide","vide","vide","vide","vide","vide","vide","vide"]
joueur = 0
victoire = False
tour = 0

def ajoutesymbole (tictactoe, i) :
	if (tictactoe[i]=="croix" or tictactoe[i]=="rond"):
		print("Cette case est déjà occupée, veuillez saisir une case vide.")
	if (tictactoe[i]=="vide" and joueur%2==0):
		tictactoe[i] = "croix"
	if (tictactoe[i]=="vide" and joueur%2!=0) :
		tictactoe[i] = "rond"
	return
		
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

def testeVictoireDiagonale (tictactoe):
	if (tictactoe[0]==tictactoe[4] and tictactoe[0]==tictactoe[8] and tictactoe[0]!="vide"):
		if (tictactoe[0]=="croix"):
			print("Victoire pour les croix !")
			return True
		if (tictactoe[0]=="rond"):
			print("Victoire pour les ronds !")
			return True
	if (tictactoe[2]==tictactoe[4] and tictactoe[2]==tictactoe[6] and tictactoe[2]!="vide"):
		if (tictactoe[2]=="croix"):
			print("Victoire pour les croix !")
			return True
		if (tictactoe[2]=="rond"):
			print("Victoire pour les ronds !")
			return True
	return False

def affichegrille (tictactoe):
	print(tictactoe)
	return

def croix1():
	print("* *     * *", end = "")
	return
	
def croix2():
	print("*  *   *  *", end = "")
	return

def croix3():
	print("*    *    *", end = "")
	return

def rond1():
	print("*   ***   *", end = "")
	return

def rond2():
	print("* *     * *", end = "")
	return

def vide():
	print("*         *", end = "")
	
def visuel(tableautest):
	print("*********************************")
	for j in range(0,3):
		if (tableautest[j]=="croix"):
			croix1()
		if (tableautest[j]=="rond"):
			rond1()
		if (tableautest[j]=="vide"):
			vide()
	print()
		
	for j in range (0,3):
		if (tableautest[j]=="croix"):
			croix2()
		if (tableautest[j]=="rond"):
			rond2()
		if (tableautest[j]=="vide"):
			vide()
	print()
		
	for j in range (0,3):
		if (tableautest[j]=="croix"):
			croix3()
		if (tableautest[j]=="rond"):
			rond2()
		if (tableautest[j]=="vide"):
			vide()
	print()
		
	for j in range (0,3):		
		if (tableautest[j]=="croix"):
			croix2()
		if (tableautest[j]=="rond"):
			rond2()
		if (tableautest[j]=="vide"):
			vide()
	print()
		
	for j in range (0,3):		
		if (tableautest[j]=="croix"):
			croix1()
		if (tableautest[j]=="rond"):
			rond1()
		if (tableautest[j]=="vide"):
			vide()
	print()
	print("*********************************")
		
	for j in range(3,6):
		if (tableautest[j]=="croix"):
			croix1()
		if (tableautest[j]=="rond"):
			rond1()
		if (tableautest[j]=="vide"):
			vide()
	print()
		
	for j in range (3,6):
		if (tableautest[j]=="croix"):
			croix2()
		if (tableautest[j]=="rond"):
			rond2()
		if (tableautest[j]=="vide"):
			vide()
	print()
		
	for j in range (3,6):
		if (tableautest[j]=="croix"):
			croix3()
		if (tableautest[j]=="rond"):
			rond2()
		if (tableautest[j]=="vide"):
			vide()
	print()
		
	for j in range (3,6):		
		if (tableautest[j]=="croix"):
			croix2()
		if (tableautest[j]=="rond"):
			rond2()
		if (tableautest[j]=="vide"):
			vide()
	print()
		
	for j in range (3,6):		
		if (tableautest[j]=="croix"):
			croix1()
		if (tableautest[j]=="rond"):
			rond1()
		if (tableautest[j]=="vide"):
			vide()
	print()
	print("*********************************")

	for j in range(6,9):
		if (tableautest[j]=="croix"):
			croix1()
		if (tableautest[j]=="rond"):
			rond1()
		if (tableautest[j]=="vide"):
			vide()
	print()
		
	for j in range (6,9):
		if (tableautest[j]=="croix"):
			croix2()
		if (tableautest[j]=="rond"):
			rond2()
		if (tableautest[j]=="vide"):
			vide()
	print()
		
	for j in range (6,9):
		if (tableautest[j]=="croix"):
			croix3()
		if (tableautest[j]=="rond"):
			rond2()
		if (tableautest[j]=="vide"):
			vide()
	print()
		
	for j in range (6,9):		
		if (tableautest[j]=="croix"):
			croix2()
		if (tableautest[j]=="rond"):
			rond2()
		if (tableautest[j]=="vide"):
			vide()
	print()
		
	for j in range (6,9):		
		if (tableautest[j]=="croix"):
			croix1()
		if (tableautest[j]=="rond"):
			rond1()
		if (tableautest[j]=="vide"):
			vide()
	print()
	print("*********************************")	

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
	