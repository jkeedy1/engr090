class lineup:

	def __init__(self, curLine):
		self.players = curLine
		self.time = 0.0
		self.pointsFor = 0
		self.pointsAgainst = 0
		self.possessions = 0
		self.defpossessions = 0
		self.assists = 0
		self.rebounds = 0
		self.FGA = 0
		self.FGM = 0
		self.turnovers = 0
		self.fouls = 0

	def getLine(self):
		return self.players
	def getLineTest(self):
		string  = ""
		for name in self.players:
			string += name
		return string
	def getTime(self):
		return self.time
	def getPossessions(self):
		return self.possessions
	def getDefPossessions(self):
		return self.defpossessions
	def OffRating(self):
		return (self.pointsFor)/(self.possessions)
	def DefRating(self):
		return (self.pointsAgainst)/(self.defpossessions)
	def getNetRating(self):
		return (self.OffRating) - (self.DefRating)
	def getPointsFor(self):
		return self.pointsFor
	def getPointsAgainst(self):
		return self.pointsAgainst
	def getStats(self):
		print "Points For:", self.pointsFor
		print "Points Against:", self.pointsAgainst
		print "Rebounds:", self.rebounds
		print "Turnovers:", self.turnovers
		print "Possessions:", self.possessions
		print "Defensive Possessions:", self.defpossessions
		if self.possessions != 0:
			print "OffRating:", 100*(float(self.pointsFor)/float(self.possessions))
		if self.defpossessions != 0:
			print "DefRating:", 100*(float(self.pointsAgainst)/float(self.defpossessions))
	def getAssistRate(self):
		return (self.assists)/(self.possessions)
	def getReboundRate(self):
		if self.possessions == 0:
			return 0
		return (self.rebounds)/(self.possessions)
	def getRebounds(self):
		return self.rebounds
	def getFGP(self):
		return (self.FGM)/(self.FGA)
	def getTurnovers(self):
		return self.turnovers
	def getTurnoverRate(self):
		return (self.turnovers)/(self.possessions)
	def getFoulRate(self):
		return (self.fouls)/(self.possessions)
	def getRebounds(self):
		return self.rebounds
	def addTime(self, time):
		self.time += time
	def addPointsFor(self, points):
		self.pointsFor += points
	def addPointsAgainst(self, points):
		self.pointsAgainst += points
	def addPossession(self):
		self.possessions += 1
	def addAssist(self):
		self.assists += 1
	def addRebound(self):
		self.rebounds += 1
	def addFGA(self):
		self.FGA += 1
	def addFGM(self):
		self.FGA += 1
		self.FGM += 1
	def addTurnover(self):
		self.turnovers += 1
	def addFoul(self):
		self.fouls += 1
	def addDefPossession(self):
		self.defpossessions += 1


