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