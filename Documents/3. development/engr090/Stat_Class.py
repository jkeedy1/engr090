#engr090
#Joe Keedy & Noah Sterngold
#2/13/14

from bs4 import BeautifulSoup
import urllib
import copy
from e90classes import *

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

def getScore(string, home, away, team1, team2, masterLines):
  getPoints(string, home, away, team1, team2, masterLines)
  if "assists" in string:
    sa = string.find("(")
    ea = string.find("assists")
    passer = string[sa+1:ea-1]
    checkHome = getTeam(home, passer)
    # if checkHome:
    #   stats2[10] += 1
    # else:
    #   stats1[10] += 1
    # stats[2] += 1
  return

def getPoints(string, home, away, team1, team2, masterLines):
  endname = string.find("makes")
  shooter = string[:endname]
  checkHome = getTeam(home, shooter)
  checkAway = getTeam(away, shooter)
  if "free throw" in string:
    points = 1
    last = checkLastFT(string)
    if checkHome:
      for i in range(len(masterLines[team1])-1):
        line = masterLines[team1][i+1].getLine()
        if line == home:
          masterLines[team1][i+1].addPointsFor(points)
      if last:
        masterLines[team1][i+1].addPossession()
    elif checkAway:
      for i in range(len(masterLines[team2])-1):
        line = masterLines[team2][i+1].getLine()
        if line == away:
          masterLines[team2][i+1].addPointsFor(points)
      if last:
        masterLines[team2][i+1].addPossession()
    else:
      print "Couldn't Find shooter in lineup", string
      print shooter, home, away
  elif "three" in string:
    points = 3
    if checkHome:
      for i in range(len(masterLines[team1])-1):
        line = masterLines[team1][i+1].getLine()
        if line == home:
          masterLines[team1][i+1].addPointsFor(points)
          masterLines[team1][i+1].addPossession()
    elif checkAway:
      for i in range(len(masterLines[team2])-1):
        line = masterLines[team2][i+1].getLine()
        if line == away:
          masterLines[team2][i+1].addPointsFor(points)
          masterLines[team2][i+1].addPossession()
    else:
      print "Couldn't Find shooter in lineup", string
      print shooter, home, away
  else:
    points = 2
    if checkHome:
      for i in range(len(masterLines[team1])-1):
        line = masterLines[team1][i+1].getLine()
        if line == home:
          masterLines[team1][i+1].addPointsFor(points)
          masterLines[team1][i+1].addPossession()
    elif checkAway:
      for i in range(len(masterLines[team2])-1):
        line = masterLines[team2][i+1].getLine()
        if line == away:
          masterLines[team2][i+1].addPointsFor(points)
          masterLines[team2][i+1].addPossession()
    else:
      print "Couldn't Find shooter in lineup", string
      print shooter, home, away

  return

def checkLastFT(string):
  #Look to see if the FT make was the last one to get a possession change
  ends = ["2 of 2", "3 of 3" , "1 of 1"]
  for i in ends:
    if i in string:
      return 1

  return 0

def getLineupDigit(masterLines, team, current):
  count = 0
  for i in range(len(masterLines[team])-1):
    line = masterLines[team][i+1]

def getRebound(string, home, away, team1, team2, masterLines):
  if "team" in string:
    if "defensive" in string:
      end = string.find("defensive")
      team = string[:end-1]
      if masterLines[team1][0] in nameCheck[team]:
        for i in range(len(masterLines[team2])-1):
          line = masterLines[team2][i+1].getLine()
          if line == away:
            masterLines[team2][i+1].addPossession()
      elif masterLines[team2][0] in nameCheck[team]:
        for i in range(len(masterLines[team1])-1):
          line = masterLines[team1][i+1].getLine()
          if line == home:
            masterLines[team1][i+1].addPossession()
      else:
        print "No Match"
    return 0
  else:
    if "defensive" in string:
      end = string.find("defensive")
      boarder = string[:end]
      checkHome = getTeam(home, boarder)
      if checkHome:
        for i in range(len(masterLines[team1])-1):
          line = masterLines[team1][i+1].getLine()
          if line == home:
            masterLines[team1][i+1].addRebound()
            masterLines[team1][i+1].addPossession()
            return
      else:
        for i in range(len(masterLines[team2])-1):
          line = masterLines[team2][i+1].getLine()
          if line == away:
            masterLines[team2][i+1].addRebound()
            masterLines[team2][i+1].addPossession()
            return
      #     if boarder == name:
      #       masterLines[team1][i+1].addRebound()
      #       return
      # if checkHome:
      #   stats2[8] += 1
      #   stats2[9] += 1
      #   stats1[14] += 1
      # else:
      #   stats1[8] += 1
      #   stats1[9] += 1
      #   stats2[14] += 1
      # stats[7] += 1
      # stats[8] += 1
    else:
      end = string.find("offensive")
      boarder = string[:end]
      checkHome = getTeam(home, boarder)
    #   if checkHome:
    #     stats2[7] += 1
    #     stats2[9] += 1
    #   else:
    #     stats1[7] += 1
    #     stats1[9] += 1
    # stats[9] += 1
    # stats[1] += 1
    return 1

def isSub(string):
  if len(string) > 0:
    if "enters the game" in string:
      return 1
    else:
      return 0
  return 0

def getPlayerIn(string, players1, players2):
  lookHere = ((len(string))/2) + 5
  for player in players1:
    if player in string[:lookHere]:
      return player
  for player in players2:
    if player in string[:lookHere]:
      return player
  print string
  print players1
  print players2

def getPlayerOut(string, players1, players2):
  lookHere = ((len(string))/2) - 5
  for player in players1:
    if player in string[lookHere:]:
      return player
  for player in players2:
    if player in string[lookHere:]:
      return player

def getNameInBoxScore(string):
  for i in range(len(string)):
    if string[i] == ",":
      return string[:i]
  return 0

def getSoup(url):
  file_pointer = urllib.urlopen(url)
  return BeautifulSoup(file_pointer)

def getPlayersAndStarters(soup, players1, players2,
                          starters1, starters2, masterLines):
  rowIndex = 0
  start = 0
  bench = 0
  teamCount = 0
  firstTeamCount = 0
  for row in soup.find_all("tr"):
    for i in range(len(masterLines)):
      if masterLines[i][0] in row.text:
        firstTeamCount += 1
        if firstTeamCount == 1:
          team1 = i
        elif firstTeamCount == 2:
          team2 = i
          break
    rowIndex += 1
    if "STARTERS" in row.text:
      teamCount += 1
      start = rowIndex + 1
    if "BENCH" in row.text:
      bench = rowIndex + 1
    if rowIndex >= start and rowIndex < (start + 5):
      col = 0
      for section in row.find_all("td"):
        if col == 0:
          player = getNameInBoxScore(section.text)
          if player:
            if teamCount == 1:
              starters1.append(player)
            else:
              starters2.append(player)
        col += 1
    elif rowIndex >= bench and "TOTALS" not in row.text:
      col = 0
      for section in row.find_all("td"):
        if col == 0:
          player = getNameInBoxScore(section.text)
          if player:
            if teamCount == 1:
              players1.append(player)
            else:
              players2.append(player)
        col += 1

  for player in starters1:
    players1.insert(0, player)
  for player in starters2:
    players2.insert(0, player)

  return players1, players2, starters1, starters2, team1, team2

def getSubs(row, players1, players2, curLine1, curLine2):
  rowIndex = 0
  
  # print "in: " + getPlayerIn(row, players1, players2)
  # print "out: " + getPlayerOut(row, players1, players2)

  if getPlayerOut(row, players1, players2) in curLine1:
    curLine1.append(getPlayerIn(row, players1, players2))
    curLine1.remove(getPlayerOut(row, players1, players2))

  elif getPlayerOut(row, players1, players2) in curLine2:
    curLine2.append(getPlayerIn(row, players1, players2))
    curLine2.remove(getPlayerOut(row, players1, players2))

  else:
    print "ERROR in getSubs"

  return curLine1, curLine2

def isTime(section):
  if ":" in section:
    return 1
  return 0

def pbpStructure(soup):
  q2, q3, q4 = 0, 0, 0
  quarter = 0
  rowIndex = 0
  pbpRows = []
  time = []
  for row in soup.find_all("tr"):
    for section in row.find_all("td"):
      if len(section.text) > 1:
        if section.text[0].isdigit():
          if isTime(section.text):
            time.append(section.text)
        else:
          pbpRows.append(section.text)
    rowIndex += 1

  vsIndex = 0
  for i in range(len(pbpRows)):
    if "vs." in pbpRows[i]:
      vsIndex = i
      break

  for i in range(vsIndex):
    pbpRows.pop(0)

  for i in range(len(pbpRows)):
    if "Quarter" in pbpRows[i]:
      quarter += 1
      if quarter == 1:
        q2 = i + 1
      if quarter == 2:
        q3 = i + 1
      if quarter == 3:
        q4 = i + 1

  return q2, q3, q4, pbpRows, time

# once we know who starts each quarter, this will track all changes
def getLineChanges(pbpRows, start, end, players1,
                   players2, curLine1, curLine2,
                   team1, team2, masterLines):

  for i in range(start, end):
    play = pbpRows[i]
    if isSub(pbpRows[i]):

      curLine1, curLine2 = getSubs(pbpRows[i], players1,
                                   players2, curLine1, curLine2)

      appendLine(masterLines, curLine1, curLine2, team1, team2)

    elif isStat(play, "rebound"):
      rebs = getRebound(play, curLine1, curLine2, team1, team2, masterLines)

    elif isStat(play, "makes"):
      getScore(play, curLine1, curLine2, team1, team2, masterLines)


def appendLine(masterLines, line1, line2, team1, team2):
  line1.sort()
  line2.sort()
  temp1 = copy.deepcopy(line1)
  temp2 = copy.deepcopy(line2)

  change1 = 1
  change2 = 1

  for i in range(len(masterLines[team1]) - 1):
    if temp1 == masterLines[team1][i + 1].getLine():
      change1 = 0
  if change1 == 1:
    masterLines[team1].append(lineup(temp1))

  for i in range(len(masterLines[team2]) - 1):
    if temp2 == masterLines[team2][i + 1].getLine():
      change2 = 0
  if change2 == 1:
    masterLines[team2].append(lineup(temp2))

def getQuarterStarters(pbpRows, start, end, players1, players2):

  # a list of players who could not have been in the quarter first
  notInFirst, qStarters1, qStarters2 = ([] for i in range(3))

  for i in range(start, end):

    # if there is a sub in the quarter, need to keep track of some things
    if isSub(pbpRows[i]):
      playerOut = getPlayerOut(pbpRows[i], players1, players2)
      playerIn = getPlayerIn(pbpRows[i], players1, players2)

      if playerOut in players1:
        notInFirst.append(playerIn)
        if playerOut not in notInFirst and playerOut not in qStarters1:
          qStarters1.append(playerOut)

      elif playerOut in players2:
        notInFirst.append(playerIn)
        if playerOut not in notInFirst and playerOut not in qStarters2:
          qStarters2.append(playerOut)

    # by looking at who's in the action, build out who started the quater
    else:
      for player in players1:
        if player in pbpRows[i] and player not in notInFirst:
          if player not in qStarters1:
            qStarters1.append(player)

      for player in players2:
        if player in pbpRows[i] and player not in notInFirst:
          if player not in qStarters2:
            qStarters2.append(player)

  qStarters1.sort()
  qStarters2.sort()

  return qStarters1, qStarters2

def lineupStorage():

  masterLines = [[] for i in range(30)]

  # ATL, BKN, BOS, CHA, CHI, CLE, DAL, DEN, DET, GSW, HOU, IND, \
  # LAC, LAL, MEM, MIA, MIL, MIN, NO, NYK, OKC, ORL, PHI, PHX, \
  # POR, SAC, SA, TOR, UTA, WAS = ([] for i in range(30))

  masterLines[0].append("ATL")
  masterLines[1].append("BKN")
  masterLines[2].append("BOS")
  masterLines[3].append("CHA")
  masterLines[4].append("CHI")
  masterLines[5].append("CLE")
  masterLines[6].append("DAL")
  masterLines[7].append("DEN")
  masterLines[8].append("DET")
  masterLines[9].append("GSW")
  masterLines[10].append("HOU")
  masterLines[11].append("IND")
  masterLines[12].append("LAC")
  masterLines[13].append("LAL")
  masterLines[14].append("MEM")
  masterLines[15].append("MIA")
  masterLines[16].append("MIL")
  masterLines[17].append("MIN")
  masterLines[18].append("NO")
  masterLines[19].append("NYK")
  masterLines[20].append("OKC")
  masterLines[21].append("ORL")
  masterLines[22].append("PHI")
  masterLines[23].append("PHX")
  masterLines[24].append("POR")
  masterLines[25].append("SAC")
  masterLines[26].append("SA")
  masterLines[27].append("TOR")
  masterLines[28].append("UTA")
  masterLines[29].append("WAS")

  return masterLines

def getNickNames():
  names = [[] for i in range(30)]

  names[0] = "Hawks"
  names[1] = "Nets"
  names[22] = "76ers"
  names[12] = "CLippers"
  names[25] = "Kings"
  names[29] = "Wizards"
  names[19] = "Knicks"
  names[20] = "Thunder"
  names[4] = "Bulls"
  names[13] = "Lakers"
  names[6] = "Mavericks"
  names[2] = "Celtics"
  names[18] = "Pelicans"
  names[14] = "Grizzlies"
  names[5] = "Cavaliers"
  names[21] = "Magic"
  names[11] = "Pacers"
  names[8] = "Pistons"
  names[27] = "Raptors"
  names[26] = "Spurs"
  names[3] = "Bobcats"
  names[10] = "Rockets"
  names[16] = "Bucks"
  names[7] = "Nuggets"
  names[17] = "Timberwolves"
  names[28] = "Jazz"
  names[15] = "Heat"
  names[9] = "Warriors"
  names[24] = "Trail Blazers"
  names[23] = "Suns"

  return names

def NicknametoTeam(nicks, teams):
  nameCheck = {}
  for i in range(len(nicks)):
    nameCheck[nicks[i]] = teams[i]
  
  return nameCheck

def main():

  global nameCheck
  lineCheck = lineupStorage()
  NickNames = getNickNames()
  nameCheck = NicknametoTeam(NickNames, lineCheck)

  # begin storing lineups
  masterLines = lineupStorage()

  players1, players2, starters1, starters2, \
    curLine1, curLine2 = ([] for i in range(6))

# initialize players and starters lists using box score data
  boxScoreSoup = getSoup("http://espn.go.com/nba/boxscore?gameId=400489639")
  players1, players2, starters1, \
  starters2, team1, team2 = getPlayersAndStarters(boxScoreSoup,
                                                  players1, players2,
                                                  starters1, starters2,
                                                  masterLines)

# pull the play by play data
  pbpSoup = \
    getSoup("http://espn.go.com/nba/playbyplay?gameId=400489639&period=0")

# put the soup in a list data structure and add quarter markers
  q2, q3, q4, pbpRows, time = pbpStructure(pbpSoup)

  curLine1 = starters1
  curLine2 = starters2

  curLine1.sort()
  curLine2.sort()

  temp1 = copy.deepcopy(curLine1)
  temp2 = copy.deepcopy(curLine2)

  masterLines[team1].append(lineup(temp1))
  masterLines[team2].append(lineup(temp2))

  # tracking for the first quarter, by far the most straightforward
  getLineChanges(pbpRows, 0, q2, players1, players2, curLine1, curLine2,
                 team1, team2, masterLines)

  # find the second quarter starters
  qStarters1, qStarters2 = getQuarterStarters(pbpRows, q2, q3,
                                              players1, players2)

  appendLine(masterLines, qStarters1, qStarters2, team1, team2)


  # track the changes in the second quarter using the second quarter starters
  getLineChanges(pbpRows, q2, q3, players1, players2, qStarters1, qStarters2,
                 team1, team2, masterLines)
 
  # find the third quarter starters
  qStarters1, qStarters2 = getQuarterStarters(pbpRows, q3, q4,
                                              players1, players2)

  appendLine(masterLines, qStarters1, qStarters2, team1, team2)
 
  # track the changes in the third quarter using the second quarter starters
  getLineChanges(pbpRows, q3, q4, players1, players2, qStarters1, qStarters2,
                 team1, team2, masterLines)

  # find the fourth quarter starters
  qStarters1, qStarters2 = getQuarterStarters(pbpRows, q4, len(pbpRows),
                                              players1, players2)

  appendLine(masterLines, qStarters1, qStarters2, team1, team2)

  # track the changes in the fourth quarter using the second quarter starters
  getLineChanges(pbpRows, q4, len(pbpRows), players1, players2,
                 qStarters1, qStarters2, team1, team2, masterLines)


  # print
  # print "team1 (", masterLines[team1][0], ") lineups:"
  # for i in range(len(masterLines[team1]) - 1):
  #   print masterLines[team1][i + 1].getLine()
  #   print masterLines[team1][i + 1].getRebounds()
  #   print "Points:", masterLines[team1][i + 1].getPointsFor()
  # print
  # print "team2 (", masterLines[team2][0], ") lineups:"
  # for i in range(len(masterLines[team2]) - 1):
  #   print masterLines[team2][i + 1].getLine()
  #   print masterLines[team2][i + 1].getRebounds()
  #   print "Points:", masterLines[team2][i + 1].getPointsFor()
  away = 0
  home = 0
  Aposs = 0
  Hposs = 0
  print "Finding the total points from all the lineups"
  for i in range(len(masterLines[team1])-1):
    away += masterLines[team1][i+1].getPointsFor()
    Aposs+= masterLines[team1][i+1].getPossessions()
  for i in range(len(masterLines[team2])-1):
    home += masterLines[team2][i+1].getPointsFor()
    Hposs+= masterLines[team1][i+1].getPossessions()
  print "Away = ", away, "On", Aposs
  print "Home =" , home, "On", Hposs



main()
