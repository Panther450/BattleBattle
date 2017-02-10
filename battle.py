import random 

class BattleCards: 
	def __init__(self):
		self.roll = roll()

	def roll(self):
		roll = random.randint(1,6)
		return roll


class Vanilla(BattleCards): 
	def __init__(self): 
		self.HP = 5
		self.wins = 0
		self.loses = 0
		self.tokens = 3
		self.roll = random.randint(1,6)

	def usePower(self,otherRoll):
		if (self.tokens>1 and self.roll):
			#self.roll += 1
			self.tokens -=1


def round(player1, player2): 
	while(player1.HP>0 and player2.HP>0):

		player1.usePower(player2.roll)
		player2.usePower(player1.roll)

		if (player1.roll > player2.roll):
			player2.HP-=1
			player1.wins+=1
		elif (player2.roll > player1.roll):
			player1.HP-=1
			player2.wins+=1

	if (player1.HP>player2.HP): 
		print("player 1 Win")
	else: 
		print("player 2 Win")

if __name__ == "__main__":
	player1 = Vanilla()
	player2 = Vanilla()
	round(player1,player2)