#! /usr/bin/python3
# -*- coding:utf-8 -*-

"""
趋势科技德州扑克AI游戏
coder: Dentist
start date: 4/25/2018
"""

import json
import hashlib
import sys
from websocket import create_connection
from people import People
from table import Table


class Gamer:
	count_number = 800
	game_round = 1
	right_forecast = 0
	win_list = []
	fold_list = []
	warning = 0
	def __init__(self, ticket, port):
		self._phone_number = "13060067437"
		self._password = "7602093"
		self._ticket = ticket
		self._port = port
		self._player_name = "Dentist"
		self._people_number = None
		self._people_survive = None
		self._people = []
		self._pre_cards = []
		self._action = None
		self._table = None
		self._could_start = False
		self._could_caculate = False
		self._my_hands_exsist = None
		self._win_rate = None
		self._odds_rate = None
		self._call_rate = None
		self._threshold = 0.65
		self._ws = create_connection("ws://ai.cad-stg.trendmicro.com:"+self._port)



	# 服务端监听
	def doListen(self):
		# print ("start the game")
		hasn_md5 = hashlib.md5()
		hasn_md5.update(self._password.encode("utf8"))
		password = hasn_md5.hexdigest()
		msg = {
			"eventName": "__join",
			"data": {
				"playerName": self._player_name,
				"phoneNumber": self._phone_number, 
				"password": password,
				"ticket": self._ticket,
				"port": self._port,
				"gameName": "texas_holdem"
				}
		}
		""" 请求加入游戏 """
		self.sendMessage(msg)
		while True:
			result = self._ws.recv()
			if(result.strip() != ""):
				result = json.loads(result)
				event_name = result["eventName"]
				data = result["data"]
				#print (json.dumps(result, sort_keys=True, indent=2))
				#print ("---------------------------------------------------------------")
				self.takeAction(event_name, data)
			else:
				# print ("there is some error")
				sys.exit(0)



	# 离开游戏
	def leaveGame(self):
		self._ws.close();



	# 信息发送
	def sendMessage(self, msg):
		self._ws.send(json.dumps(msg))



	# 采取措施
	def takeAction(self, event_name, data):
		""" 新一轮开始 """
		if(event_name == "__new_round"):
			me_survive = False
			self._my_hands_exsist = False
			count = 0
			self._people_number = len(data["players"])
			for i in range(0, self._people_number):
				if(data["players"][i]["isSurvive"] == True):
					count += 1
					if(data["players"][i]["playerName"] == self._player_name):
						me_survive = True
			self._people_survive = count

			""" 构建桌子 """
			self._table = Table(self._people_survive)

			""" 构建玩家 """
			for x in range(0, self._people_survive):
				self._people.append(People())
			self._could_start = True
			self._action = "call"
			if(me_survive == False):
				self._could_start = False


		if(self._could_start == True):
			""" 索取筹码 """
			if(event_name == "__start_reload"):
				msg = {
					"eventName": "__reload"
				}
				self.sendMessage(msg)

			""" 美女荷官发牌 """
			if(event_name == "__deal"):
				public_cards = data["table"]["board"]
				game_round_name = data["table"]["roundName"]
				if(self._my_hands_exsist == False):
					""" 同步自己手牌 """
					for i in range(0, self._people_number):
						if("cards" in data["players"][i].keys()):
							if (len(data["players"][i]["cards"]) == 2):
								hands = data["players"][i]["cards"]
								self._people[0].drawHands(self._table.specialDeal(hands))
								self._my_hands_exsist = True
								break

				""" 给其他玩家发假想牌计算胜率 """
				self._table.copyCards()
				count = 0
				cards = None
				for i in range(0, Gamer.count_number):
					self._table.shuffle()
					if(game_round_name == "Flop"):
						cards = self._table.Deal()
						cards = public_cards.copy() + cards

					elif(game_round_name == "Turn"):
						cards = public_cards.copy()
						cards.append(self._table.popCard())

					elif(game_round_name == "River"):
						cards = public_cards.copy()
					
					self._table.syncPublicCards(cards)
					rank_list = []
					for j in range(1, self._people_survive):
						self._people[j].drawHands(self._table.Deal())
					for j in range(0, self._people_survive):
						self._people[j].maxRank(self._table.getPublicCards())
						rank_list.append(self._people[j].getMaxRank())
					win = True
					for j in range(1, self._people_survive):
						if((rank_list[0]+1) < rank_list[j]):
							win = False
					if(win == True):
						count += 1
					self._table.recoverPreCards()			
				self._win_rate = count/Gamer.count_number

				self._action = "call"
				if(game_round_name == "Flop"):
					if(self._win_rate <= 0.03):
						self._action = "fold"
					elif(self._win_rate < 0.1 and Gamer.warning != 0):
						self._action = "fold"
					if(self._win_rate > 0.5):
						self._action = "raise"
					

				if(game_round_name == "Turn"):
					if(self._win_rate < 0.05):
						self._action = "fold"
					elif(self._win_rate < 0.15 and Gamer.warning != 0):
						self._action = "fold"
					if(self._win_rate > 0.6):
						self._action = "raise"

				if(game_round_name == "River"):
					if(self._win_rate < 0.4):
						self._action = "fold"
					if(self._win_rate > 0.7):
						self._action = "raise"
					if((self._win_rate > 0.2) and (self._odds_rate < 0.18) and (Gamer.warning == 0)):
						self._action = "call"
				print ("win rate", self._win_rate)
				print ("action", self._action)
				print ("call rate", self._call_rate, end="\n\n")

			# 采取行动
			if(event_name == "__action"):			
				msg = {
					"eventName": "__action",
					"data": {
						"action": self._action
					}
				}
				if(self._action == "call"):
					msg = {
					"eventName" : "__action",
					"data" : {
						"action" : "bet",
						"amount" : data["self"]["chips"]/15
					}
				}
				if(self._action == "raise"):
					msg = {
						"eventName" : "__action",
						"data" : {
							"action" : "bet",
							"amount" : data["self"]["chips"]/10
						}
					}
				self.sendMessage(msg)


			# 需要下注
			if(event_name == "__bet"):
				# 存在bug
				if(self._action == "fold"):
					msg = {
					"eventName": "__action",
					"data": {
						"action": self._action
						}
					}
				elif(self._action == "call"):
					msg ={
					    "eventName" : "__action",
					    "data" : {
					        "action" : "bet", 
					        "amount" : 10
					    }
					}

				elif(self._action == "raise"):
					
					msg = {
						"eventName" : "__action",
						"data" : {
							"action" : "bet",
							"amount" : data["self"]["chips"]/10
						}
					}
				self.sendMessage(msg)


			# 更新桌面状态
			if(event_name == "__show_action"):
				maxbet = 0
				mybet = 0
				if(data["action"]["action"] == "raise"):
					if(data["action"]["playerName"] != self._player_name):
						Gamer.warning += 1

				for i in range(0, self._people_number):
					if("roundBet" in data["players"][i].keys()):
						if(data["players"][i]["roundBet"] > maxbet):
							maxbet += data["players"][i]["roundBet"]
						if(data["players"][i]["playerName"] == self._player_name):
							mybet += data["players"][i]["roundBet"]
				total_bet = data["table"]["totalBet"]
				self._odds_rate = maxbet / (total_bet + maxbet - mybet)
				count = 0
				for i in range(0, self._people_number):
					if(data["players"][i]["folded"] == True):
						count += 1
				self._call_rate = (self._people_survive - count)/self._people_survive





			# 结束一轮
			if(event_name == "__round_end"):
				rank_list = []
				fold_choice = None
				self._could_caculate = False
				Gamer.warning = 0
				self._people.clear()
				print ("-----------------------------")


			# 游戏结束
			if(event_name == "__game_over"):
				print (data["winners"])
		else:
			print ("wait the this round over")

if __name__ == '__main__':
	ticket = "9y3gf1u6k6vje2zbt8myy8g00rc9ag"
	port = "9021"
	my = Gamer(ticket, port) 
	my.doListen()

