import random 
import itertools 

class BattleCards: 
	HP = 5
	wins = 0
	loses = 0
	tokens = 3
	roll = random.randint(1,6)
	damage = 1

	def __init__(self):
		self.HP = 5
		self.wins = 0
		self.loses = 0
		self.tokens = 3
		self.roll = random.randint(1,6)

	def rollDice(self):
		self.damage = 1
		self.roll = random.randint(1,6)

#Powers: Token: add 1 to your battle die
class Vanilla(BattleCards): 
	def __init__(self): 
		self.HP = 5
		self.tokens = 3
		self.name = "Vanilla"


	def usePower(self,otherPlayer):
		if (self.tokens>=1 and self.roll<otherPlayer.roll):
			self.roll += 1
			self.tokens -=1
			

#Powers: TOKEN: You win the round
class Ruler(BattleCards): 
	def __init__(self): 
		self.HP = 4
		self.tokens = 2
		self.name = "Ruler"

	def usePower(self,otherPlayer):
		if (self.tokens>=1 and self.roll<otherPlayer.roll):
			self.roll = 100
			self.tokens -=1

# Powers: EVERY ROUND: Gain 1 token for each HP of damage you recieve 
# 		TOKEN: add 2 to your roll 
class Banker(BattleCards): 
	def __init__(self): 
		self.HP = 4
		self.tokens = 0
		self.name = "Banker"

	def usePower(self,otherPlayer): 
		if(self.tokens>=1): 
			self.roll +=2
			self.tokens-=1

		if(self.roll<otherPlayer.roll): 
			self.tokens += 1

# POWERS: EVERY ROUND: Roll 2 battle dice. Score 1 HP damage for each die that beats opponent's roll
# EVERY ROUND: Double All damage you recieve
# If you roll a 1-3 it counts as a 4
class Barbarian(BattleCards):

	def __init__(self): 
		self.HP = 6
		self.tokens = 0
		self.secondRoll = 0
		self.name = "Barbarian"

	def usePower(self,otherPlayer):
		if (self.secondRoll>otherPlayer.roll and self.roll>otherPlayer.roll): 
			self.damage += 1
		else: 
			if (self.secondRoll>=self.roll): 
				self.Roll = self.secondRoll 

	def rollDice(self): 
		self.damage = 1
		self.roll = random.randint(1,6)

		if (self.roll <=3): 
			self.roll = 4

		self.secondRoll = random.randint(1,6)

		if (self.secondRoll <=3): 
			self.secondRoll = 4

# POWERS: EVERY ROUND: If you have less HP than your opponent, add 3 to your roll

class Wimp(BattleCards):
	def __init__(self): 
		self.HP = 3
		self.tokens = 0
		self.name = "Wimp"

	def usePower(self,otherPlayer):
		if (otherPlayer.HP>self.HP): 
			self.roll += 3

#POWERS: TOKEN: Double your roll 
# if you roll a 4 or a 5 it counts as a 6

class Assassin(BattleCards): 
	def __init__(self):
		self.HP = 3 
		self.tokens = 1
		self.name = "Assassin"

	def usePower(self,otherPlayer): 
		if(self.roll < otherPlayer.roll and self.tokens>0): 
			self.tokens -= 1
			self.roll *= 2

	def rollDice(self):
		self.damage = 1
		self.roll = random.randint(1,6)

		if (self.roll == 4 or self.roll == 5): 
			self.roll = 6

#POWER: EVERY ROUND: Roll 3 battle dice. Score 1 HP damage for each die that beats opponents roll
class Weenie(BattleCards): 
	def __init__(self):
		self.HP = 2
		self.tokens = 0 
		self.rollThree =0
		self.secondRoll = 0
		self.name = "Weenie"

	def usePower(self,otherPlayer): 
		if (self.roll>otherPlayer.roll and self.secondRoll>otherPlayer.roll):
			self.damage += 1
		if(self.rollThree > otherPlayer.roll): 
			self.damage += 1 

	def changeDice(self, roll):
		if (roll == 4): 
			roll = 3
		if (roll == 6):
			roll = 5 
		return roll 

	def rollDice(self):
		self.damage = 1
		self.roll = random.randint(1,6)
		self.roll = self.changeDice(self.roll)

		self.secondRoll = random.randint(1,6)
		self.secondRoll = self.changeDice(self.secondRoll)

		self.rollThree = random.randint(1,6)
		self.rollThree = self.changeDice(self.rollThree)

# POWERS: TOKEN: roll an additional battle die.
# 		Each die that beats your oppponent's roll scores 1 damage
# 		EVERY ROUND: If any of your dice are doubles, you score no damage that round

class Wizard(BattleCards): 
	def __init__(self):
		self.HP = 2
		self.tokens = 5
		self.secondRoll = 0
		self.name = "Wizard"

	def usePower(self,otherPlayer): 
		if (self.roll == self.secondRoll): 
			self.damage = 0
		elif(self.tokens>0 and self.roll>otherPlayer.roll and self.secondRoll>otherPlayer.roll): 
			self.tokens -= 1
			self.damage += 1

	def rollDice(self):
		self.damage = 1
		self.roll = random.randint(1,6)
		self.secondRoll = random.randint(1,6)

# POWERS: TOKEN: Take no damage this round.
# 		  The next round damage is doubled	
#         On a 3 or a 4 roll again

class Gambler(BattleCards): 
	def __init__(self):
		self.HP = 5
		self.tokens = 3
		self.lastRoundToken = False
		self.name = "Gambler"

	def usePower(self,otherPlayer): 
		if(self.tokens>0 and self.roll<otherPlayer.roll): 
			self.tokens -= 1
			otherPlayer.damage = 0
			self.lastRoundToken = True 
		elif(self.lastRoundToken): 
			self.lastRoundToken = False 
			otherPlayer.damage= otherPlayer.damage*2

	def rollDice(self):
		self.damage = 1
		self.roll = random.randint(1,6)

		while(self.roll== 3 or self.roll == 4): 
			self.roll = random.randint(1,6)




#POWERS: EVERY ROUND: You can only recieve damage when your battle die is a 1 
# If you roll a 6 it equals a 1
class Zombie(BattleCards): 
	def __init__(self):
		self.HP = 2
		self.tokens = 0 
		self.name = "Zombie"

	def usePower(self,otherPlayer): 
		if (self.roll == 1): 
			otherPlayer.damage = 0

	def rollDice(self):
		self.damage = 1
		self.roll = random.randint(1,6)
		if (self.roll == 6): 
			self.roll = 1

#POWERS: EVERY ROUND: Wins Ties 
#        TOKEN: Reduce opponent's roll by one

class General(BattleCards): 
	def __init__(self):
		self.HP = 4
		self.tokens = 3 
		self.name = "General"

	def usePower(self,otherPlayer): 
		if(otherPlayer.roll == self.roll): 
			self.roll += 1
		elif(otherPlayer.roll == self.roll+1):
			otherPlayer.roll -= 1
			self.tokens -= 1

#POWERS: TOKEN: Keep your same battle die number for next round 
#               You cannot use a token 2 turns in a row 

class Bodybuilder(BattleCards): 
	def __init__(self):
		self.HP = 5
		self.tokens = 3 
		self.lastRoundToken = False
		self.lastRoll = 0
		self.name = "Bodybuilder"

	def usePower(self,otherPlayer): 
		if(self.lastRoundToken == False): 
			if(self.roll == 6 or self.roll == 5): 
				self.lastRoll = self.roll
				self.lastRoundToken = True
				self.tokens -= 1
			elif(self.lastRoundToken == True): 
				self.lastRoundToken == False

	def rollDice(self): 
		self.damage = 1
		self.roll = random.randint(1,6) 

		if(self.lastRoundToken == True): 
			self.roll = self.lastRoll


#POWERS: - EVERY ROUND: Each time you take damage, steal 1 token from your opponent
#        - EVERY ROUND: If your opponent has no tokens, when you take damage, add 2 to your next roll 

class Thief(BattleCards):
	def __init__(self):
		self.HP = 4
		self.tokens = 0
		self.lastRoundPower = False 
		self.name = "Thief"

	def usePower(self,otherPlayer): 
		if(self.roll < otherPlayer.roll and otherPlayer.tokens>0):
			otherPlayer.tokens -=1 

		elif(self.roll < otherPlayer.roll and otherPlayer.tokens<=0):
			self.lastRoundPower = True

	def rollDice(self):
		self.damage = 1
		self.roll = random.randint(1,6) 

		if(self.lastRoundPower == True): 
			self.roll = self.roll+2
			self.lastRoundPower = False



#POWERS: TOKEN: double your damage. The next round, subtract 3 from your roll. 

class Boxer(BattleCards):
	def __init__(self):
		self.HP = 5
		self.tokens = 3
		self.lastRoundPower = False 
		self.name = "Boxer"	

	def usePower(self,otherPlayer): 
		if(self.roll>otherPlayer.roll): 
			self.damage += 3 
			self.tokens -= 1
			self.lastRoundPower = True 

	def rollDice(self): 
		self.damage = 1
		self.roll = random.randint(1,6) 

		if(self.lastRoundPower == True): 
			self.roll = self.roll-3
			self.lastRoundPower = False


#POWERS: TOKEN: roll again 
# If you roll a 1,2,3 then +1 token
# IF THEY ROLL AGAIN DO THEY GET A TOKEN ON A 1-3 ROLL?
class Trickster(BattleCards):
	def __init__(self):
		self.HP = 4
		self.tokens = 0
		self.name = "Trickster"

	def usePower(self,otherPlayer):
		if(self.roll<otherPlayer.roll):
			self.rollDice()
			self.tokens-=1

	def rollDice(self): 
		self. damage = 1
		self.roll = random.randint(1,6) 

		if(self.roll<=3): 
			self.tokens+=1

#POWERS TOKEN: permanently swap your HP die and your battle die roll 
class Survivalist(BattleCards):
	def __init__(self):
		self.HP = 5
		self.tokens = 1
		self.name = "Survivalist"

	def usePower(self,otherPlayer):
		if(self.HP == 1 and self.tokens >0): 
			self.tokens -=1
			roll = self.roll 
			self.roll = self.HP 
			self.HP = roll 


def round(player1, player2): 
	count = 0
	while(player1.HP>=0 and player2.HP>=0):
		count += 1

		player1.rollDice()
		player2.rollDice()

		if (player1.HP>=player2.HP):
			player1.usePower(player2)
			player2.usePower(player1)
		else:
			player2.usePower(player1)
			player1.usePower(player2)

		if (player1.roll > player2.roll):
			player2.HP-=player1.damage

		elif (player2.roll > player1.roll):
			player1.HP-=player2.damage

	if (player1.HP>player2.HP): 
		player1.wins += 1

	else: 
		player2.wins += 1


#Sets up the list of characters so we can go through them
def setUp(): 
	characterList = []

	barbarian = Barbarian()
	characterList.append(barbarian)

	ruler = Ruler()
	characterList.append(ruler)

	banker = Banker()
	characterList.append(banker)

	vanilla = Vanilla()
	characterList.append(vanilla)

	zombie = Zombie()
	characterList.append(zombie)

	wimp = Wimp()
	characterList.append(wimp)

	assassin = Assassin()
	characterList.append(assassin)

	weenie = Weenie()
	characterList.append(weenie)

	gambler = Gambler() 
	characterList.append(gambler)

	wizard = Wizard()
	characterList.append(wizard)

	general = General()
	characterList.append(general)

	bodybuilder = Bodybuilder()
	characterList.append(bodybuilder)

	thief  = Thief()
	characterList.append(thief)

	boxer = Boxer()
	characterList.append(boxer)

	trickster = Trickster()
	characterList.append(trickster)

	survivalist = Survivalist()
	characterList.append(survivalist)

	return characterList

def RunSimulation():
	characterList = setUp()
	print(characterList)
	characterList2 = setUp()


	for character1 in characterList:
		player1 = character1 
		for character2 in characterList2: 
			player2 = character2 

			print(player1.name + " vs "+ player2.name)
			for x in range (1,10):
				round(player1, player2)

if __name__ == "__main__":

	 player1 = Barbarian()
	 player2 = Barbarian()
	 round(player1,player2)