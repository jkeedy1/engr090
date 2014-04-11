'''
engr090
Joe Keedy & Noah Sterngold

'''

from bs4 import BeautifulSoup
from e90classes import *
import urllib
import copy



def isSub(string):
  '''
determines whether or not a given pbpRow string is a substitution,
returning one if it is or zero otherwise
'''
  if len(string) > 0:
    if "enters the game" in string:
      return 1
    else:
      return 0
  return 0

def whichTeam(string, players1):
  '''
given a string and the players from a single team, determines to
which team the action in the string applies
'''
  for player in players1:
    if player in string:
      return "team1"
  return "team2"

def getPlayerIn(string, players1, players2):
  stringSection = len(string) - 1
  for player in players1:
    if player in string[:stringSection]:
      return player
  for player in players2:
    if player in string[:stringSection]:
      return player
  print string
  print players1
  print players2

def getPlayerOut(string, players1, players2):
  stringSection = 1
  for player in players1:
    if player in string[stringSection:]:
      return player
  for player in players2:
    if player in string[stringSection:]:
      return player

def getNameInBoxScore(string):
  for i in range(len(string)):
    if string[i] == ",":
      return string[:i]
  return 0

def getSoup(url):
  file_pointer = urllib.urlopen(url)
  return BeautifulSoup(file_pointer)

def isTime(section):
  if ":" in section:
    return 1
  return 0

def stringToSeconds(timeString):
  for i in range(len(timeString)):
    if timeString[i] == ":":
      split = i
  minutes = int(timeString[:split])
  seconds = int(timeString[(split+1):])
  timeSeconds = seconds + (minutes*60)
  return timeSeconds

def secondsToTimeString(seconds):
  m, s = divmod(seconds, 60)
  if len(str(m)) == 1 and len(str(s)) == 1:
    timeString = "0" + str(m) + ":" + "0" + str(s)
  elif len(str(m)) == 1 and len(str(s)) == 2:
    timeString = "0" + str(m) + ":" + str(s)
  elif len(str(m)) == 2 and len(str(s)) == 1:
    timeString = str(m) + ":" + "0" + str(s)
  else:
    timeString = str(m) + ":" + str(s)
  return timeString

def addLineTime(masterLines, curLine1, curLine2, team1, team2, timeSegment):
  for i in range(len(masterLines[team1])):
    if curLine1 == masterLines[team1][i].getLine():
      masterLines[team1][i].addTime(timeSegment)
  for i in range(len(masterLines[team2])):
    if curLine2 == masterLines[team2][i].getLine():
      masterLines[team2][i].addTime(timeSegment)

def printLinesInfo(masterLines, masterKeys, team1, team2):
  print
  print masterKeys[team1] + " lineups:"
  for i in range(len(masterLines[team1])):
    print
    print masterLines[team1][i].getLine()
    lineTime = masterLines[team1][i].getTime()
    print secondsToTimeString(lineTime)
    masterLines[team1][i].getStats()

  print
  print masterKeys[team2] + " lineups:"
  for i in range(len(masterLines[team2])):
    print
    print masterLines[team2][i].getLine()
    lineTime = masterLines[team2][i].getTime()
    print secondsToTimeString(lineTime)
    masterLines[team2][i].getStats()

def printTeamTotals(masterLines, masterKeys, team1, team2):
  away = 0
  home = 0
  Aposs = 0
  Hposs = 0
  arebs = 0
  hrebs = 0
  aptsagainst = 0
  hptsagainst = 0
  aturns = 0
  hturns = 0
  adefposs = 0
  hdefposs = 0


  for i in range(len(masterLines[team1])):
    away += masterLines[team1][i].getPointsFor()
    Aposs+= masterLines[team1][i].getPossessions()
    arebs += masterLines[team1][i].getRebounds()
    aptsagainst += masterLines[team1][i].getPointsAgainst()
    aturns += masterLines[team1][i].getTurnovers()
    adefposs += masterLines[team1][i].getDefPossessions()

  aOffrat = 100*(float(away)/float(Aposs))
  aDefrat = 100*(float(aptsagainst)/float(adefposs))
  aNet = aOffrat - aDefrat
  
  print
  print masterKeys[team1], "Totals:"
  print "Points For:", away
  print "Points Against:", aptsagainst
  print "Possessions:", Aposs
  print "Defensive Possessions", adefposs
  print "Rebounds:", arebs
  print "Turnovers:", aturns
  print "Off Rating:", aOffrat
  print "Def Rating:", aDefrat
  print "Net Rating:", aNet
  

  for i in range(len(masterLines[team2])):
    home += masterLines[team2][i].getPointsFor()
    Hposs+= masterLines[team2][i].getPossessions()
    hrebs += masterLines[team2][i].getRebounds()
    hptsagainst += masterLines[team2][i].getPointsAgainst()
    hturns += masterLines[team2][i].getTurnovers()
    hdefposs += masterLines[team2][i].getDefPossessions()


  hOffrat = 100*(float(home)/float(Hposs))
  hDefrat = 100*(float(hptsagainst)/float(hdefposs))
  hNet = hOffrat - hDefrat


  print
  print masterKeys[team2], "Totals:"
  print "Points For:", home
  print "Points Against:", hptsagainst
  print "Possessions:", Hposs
  print "Defensive Possessions", hdefposs
  print "Rebounds:", hrebs
  print "Turnovers:", hturns
  print "Off Rating:", hOffrat
  print "Def Rating:", hDefrat
  print "Net Rating:", hNet

def isStat(string, buzz):
  if buzz in string:
    return 1
  else:
    return 0

def getTeam(team, player):
  for i in team:
    if i in player:
      return 1
  return 0

def isTurnover(string):
  if "bad pass" in string or "turnover" in string or "traveling" in string:
    return 1
  else:
    return 0

