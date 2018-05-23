import itertools
import random


class Cards:
	def __init__(self):
		suits = ["C", "H", "S", "D"]
		ranks = ["A","2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]
		self._cards = []
		for item in itertools.product(ranks, suits):
			self._cards.append(str(item[0]+item[1]))
		# 洗牌
		random.shuffle(self._cards)

	def show(self):
		print (self._cards)

	def pop(self):
		return self._cards.pop()

	def append(self, item):
		self._cards.append(item)

	def remove(self, item):
		self._cards.remove(item)

	def add(self, cards):
		for i in range(0, len(cards)):
			self._cards.append(cards[i])

	def getAllCards(self):
		return self._cards

	def shuffle(self):
		random.shuffle(self._cards)		

