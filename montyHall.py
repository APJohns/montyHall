from random import randint


# Monty
# @param choice(int), switch(bool)
# Takes in a choice [1, 3] and a boolean (True is switch, False is don't switch), and runs the Monty Hall scenario
def monty(choice, switch):
	#Declares variables and assigns a car position
	doors = [False, False, False]
	doors[randint(0, len(doors) - 1)] = True

	#Reveals a goat
	revealed = False
	for i in range(3):
		if i != choice - 1 and doors[i] != True and revealed == False:
			revealedGoat = i
			revealed = True
	
	#Selects switch position
	for i in range(3):
		if i != choice - 1 and i != revealedGoat:
			switchSpot = i

	#Determines outcome
	if switch == False:
		if doors[choice - 1] == True:
			return True
		else:
			return False
	if switch == True:
		if doors[switchSpot] == True:
			return True
		else:
			return False


# testHall
# @params testSize(int)
# Runs the monty hall scenario a given amount of times for both switch cases and no switch cases
def testHall(testSize):
	swtichWinTotal = 0
	noSwtichWinTotal = 0
	for i in range(testSize):
		if(monty(randint(1, 3), True)):
			swtichWinTotal += 1

	for i in range(testSize):
		if(monty(randint(1, 3), False)):
			noSwtichWinTotal += 1

	print('Switch wins: ' + str(swtichWinTotal) + '/' + str(testSize))
	print('No switch wins: ' + str(noSwtichWinTotal) + '/' + str(testSize))
	return [swtichWinTotal, noSwtichWinTotal]

keepGoing = True
TestAmnt = int(input('How many times do you want to run the test? '))
while keepGoing:
	testHall(TestAmnt)
	userInput = input('Again? (y/n) ')
	if userInput == 'n':
		keepGoing = False
	
