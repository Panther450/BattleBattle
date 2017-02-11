import random 

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


	def usePower(self,otherPlayer):
		if (self.tokens>=1 and self.roll<otherPlayer.roll):
			self.roll += 1
			self.tokens -=1
			print("use Vanilla token")
			

#Powers: TOKEN: You win the round
class Ruler(BattleCards): 
	def __init__(self): 
		self.HP = 4
		self.tokens = 2

	def usePower(self,otherPlayer):
		if (self.tokens>=1 and self.roll<otherPlayer.roll):
			self.roll = 100
			self.tokens -=1
			print("use Ruler token")


# Powers: EVERY ROUND: Gain 1 token for each HP of damage you recieve 
# 		TOKEN: add 2 to your roll 
class Banker(BattleCards): 
	def __init__(self): 
		self.HP = 4
		self.tokens = 0

	def usePower(self,otherPlayer): 
		if(self.tokens>=1): 
			self.roll +=2
			self.tokens-=1
			print("banker adds to rolls")

		if(self.roll<otherPlayer.roll): 
			self.tokens += 1
			print("Tokens: " +str(self.tokens))

# POWERS: EVERY ROUND: Roll 2 battle dice. Score 1 HP damage for each die that beats opponent's roll
# EVERY ROUND: Double All damage you recieve
# If you roll a 1-3 it counts as a 4
class Barbarian(BattleCards):

	def __init__(self): 
		self.HP = 6
		self.tokens = 0
		self.secondRoll = 0

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

	def usePower(self,otherPlayer):
		if (otherPlayer.HP>self.HP): 
			self.roll += 3
			print("Use Wimp Power")


#POWERS: TOKEN: Double your roll 
# if you roll a 4 or a 5 it counts as a 6

class Assassin(BattleCards): 
	def __init__(self):
		self.HP = 3 
		self.tokens = 1

	def usePower(self,otherPlayer): 
		if(self.roll < otherPlayer.roll and self.tokens>0): 
			self.tokens -= 1
			self.roll *= 2

			print("Use Assasin Power")

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

	def usePower(self,otherPlayer): 
		if (self.roll>otherPlayer.roll and self.secondRoll>otherPlayer.roll):
			self.damage += 1
		if(self.rollThree > otherPlayer.roll): 
			self.damage += 1 

		print("Weenie Damage: "+ str(self.damage))

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

	def usePower(self,otherPlayer): 
		if (self.roll == self.secondRoll): 
			self.damage = 0
		elif(self.tokens>0 and self.roll>otherPlayer.roll and self.secondRoll>otherPlayer.roll): 
			print("Wizard Token Used")
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

	def usePower(self,otherPlayer): 
		if(self.tokens>0 and self.roll<otherPlayer.roll): 
			print("Gambler Token Used")
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

	def usePower(self,otherPlayer): 
		if(otherPlayer.roll == self.roll): 
			self.roll += 1
			print("Tie")
		elif(otherPlayer.roll == self.roll+1):
			otherPlayer.roll -= 1
			self.tokens -= 1
			print("General Token used")

#POWERS: TOKEN: Keep your same battle die number for next round 
#               You cannot use a token 2 turns in a row 

class Bodybuilder(BattleCards): 
	def __init__(self):
		self.HP = 5
		self.tokens = 3 
		self.lastRoundToken = False
		self.lastRoll = 0

	def usePower(self,otherPlayer): 
		if(self.lastRoundToken == False): 
			if(self.roll == 6 or self.roll == 5): 
				self.lastRoll = self.roll
				self.lastRoundToken = True
				self.tokens -= 1
				print("Bodybuilder token used")
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

	def usePower(self,otherPlayer): 
		if(self.roll < otherPlayer.roll and otherPlayer.tokens>0):
			otherPlayer.token -=1 

		elif(self.roll < otherPlayer.roll and otherPlayer.tokens<=0):
			self.lastRoundPower = True

	def rollDice(self):
		self.damage = 1
		self.roll = random.randint(1,6) 

		if(self.lastRoundPower == True): 
			self.roll = self.roll+2





def round(player1, player2): 
	count = 0
	while(player1.HP>=0 and player2.HP>=0):
		count += 1
		print(count)

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
			player1.wins+=1

		elif (player2.roll > player1.roll):
			player1.HP-=player2.damage
			player2.wins+=1

	if (player1.HP>player2.HP): 
		print("player 1 Win")

	else: 
		print("player 2 Win")

if __name__ == "__main__":
	player1 = Bodybuilder()
	player2 = Thief()
	round(player1,player2)