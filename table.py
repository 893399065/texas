from card import Cards
import copy

class Table:
	def __init__(self, people_number):
		self._all_cards = None
		self._copy_cards = None
		self._public_cards = []
		self.newRound()

	# 新的一局
	def newRound(self):
		self._all_cards = Cards()

	# 发手牌
	def Deal(self):
		hands = []
		for i in range(0, 2):
			hands.append(self._all_cards.pop())
		return hands

	# 发特定手牌
	def specialDeal(self, hands):
		self._all_cards.remove(hands[0])
		self._all_cards.remove(hands[1])
		return hands

	# 从牌堆里随机抽出一张牌
	def popCard(self):
		card = self._all_cards.pop()
		return card

	# 同步桌子上的公共牌
	def syncPublicCards(self, cards_list):
		self._public_cards = cards_list
		all_cards = self._all_cards.getAllCards()
		for i in range(0, len(cards_list)):
			if cards_list[i] in all_cards:
				self._all_cards.remove(cards_list[i])

	# 返回桌子上的公共牌
	def getPublicCards(self):
		return self._public_cards

	# 回收牌
	def recoverCards(self, cards):
		self._all_cards.add(cards)

	# 显示牌堆
	def showAllCards(self):
		print (self._all_cards.show())

	# 复制牌堆
	def copyCards(self):
		self._copy_cards = copy.deepcopy(self._all_cards)

	# 恢复牌堆
	def recoverPreCards(self):
		self._all_cards = copy.deepcopy(self._copy_cards)

	# 洗牌
	def shuffle(self):
		self._all_cards.shuffle()
