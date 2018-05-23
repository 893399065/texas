from rank import rankHandInt

class People:
	def __init__(self):
		self._allIn = None
		self._bet = None
		self._hands = []
		self._folded = None
		self._isSurvice = None
		self._playerName = None
		self._reloadCount = None
		self._roundBet = None
		self._maxRank = 0

	# 摸手牌
	def drawHands(self, hands):
		self._hands = hands


	# 检查手牌是否与公共牌重复
	def checkHands(self, card):
		if (card in self._hands):
			self._hands.remove(card)
			return True
		else:
			return False

	# 增加一张手牌
	def addCard(self, card):
		self._hands.append(card)

	def getHands(self):
		return self._hands

	def getMaxRank(self):
		return self._maxRank

	# 计算最大牌力
	def maxRank(self, public_cards):
		cards = self._hands + public_cards
		max_rank = 0
		for x in range(0, 6):
			for y in range(x+1, 7):
				cards_copy = cards.copy()
				temp1 = cards_copy[x]
				temp2 = cards_copy[y]
				cards_copy.remove(temp1)
				cards_copy.remove(temp2)
				hands = cards_copy
				result = rankHandInt(hands)
				rank = result["rank"]
				if (rank > max_rank):
					max_rank = rank
		self._maxRank = max_rank





