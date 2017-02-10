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
		self.roll = random.randint(1,6)

		if (self.roll <=3): 
			self.roll = 4

		self.secondRoll = random.randint(1,6)

		if (self.secondRoll <=3): 
			self.secondRoll = 4

class Wimp(BattleCards):
	def __init__(self): 
		self.HP = 3
		self.tokens = 0

	def usePower(self,otherPlayer):
		if (otherPlayer.HP>self.HP): 
			self.roll += 3
			print("Use Wimp Power")

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
		self.roll = random.randint(1,6)

		if (self.roll == 4 or self.roll == 5): 
			self.roll = 6

def round(player1, player2): 
	count = 0
	while(player1.HP>=0 and player2.HP>=0):
		count += 1
		print(count)
		player1.rollDice()
		player2.rollDice()

		player1.usePower(player2)
		player2.usePower(player1)

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
	player1 = Wimp()
	player2 = Assassin()
	round(player1,player2)