'''
engr090
Joe Keedy & Noah Sterngold

'''

from bs4 import BeautifulSoup
import copy
from e90classes import *
from e90utilityFunctions import *

def getTurnover(string, home, away, team1, team2, masterLines):
  if "lost" in string:
    if "bounds" in string:
      end = string.find("out")
    else:
      end = string.find("lost")
    turner = string[:end-1]
    checkHome = getTeam(home, turner)
    checkAway = getTeam(away, turner)
    if checkHome:
      for i in range(len(masterLines[team1])):
        line = masterLines[team1][i].getLine()
        if line == home:
          masterLines[team1][i].addTurnover()
          masterLines[team1][i].addPossession()
          for k in range(len(masterLines[team2])):
            defline = masterLines[team2][k].getLine()
            if defline == away:
              masterLines[team2][k].addDefPossession()

    elif checkAway:
      for i in range(len(masterLines[team2])):
        line = masterLines[team2][i].getLine()
        if line == away:
          masterLines[team2][i].addTurnover()
          masterLines[team2][i].addPossession()
          for k in range(len(masterLines[team1])):
            defline = masterLines[team1][k].getLine()
            if defline == home:
              masterLines[team1][k].addDefPossession()
    else:
      print "Couldn't Find turner in lineup", string
      print turner, home, away
    # if "steals" in string:
    #   getSteal(string, home)
    #   stats[15] += 1

  elif "shot clock" in string:
    turner = "Team"
    #Need to check team and add possession

  elif "turnover" in string:
    end = string.find("turnover")
    turner = string[:end-1]
    checkHome = getTeam(home, turner)
    checkAway = getTeam(away, turner)
    if checkHome:
      for i in range(len(masterLines[team1])):
        line = masterLines[team1][i].getLine()
        if line == home:
          masterLines[team1][i].addTurnover()
          masterLines[team1][i].addPossession()
          for k in range(len(masterLines[team2])):
            defline = masterLines[team2][k].getLine()
            if defline == away:
              masterLines[team2][k].addDefPossession()
    elif checkAway:
      for i in range(len(masterLines[team2])):
        line = masterLines[team2][i].getLine()
        if line == away:
          masterLines[team2][i].addTurnover()
          masterLines[team2][i].addPossession()
          for k in range(len(masterLines[team1])):
            defline = masterLines[team1][k].getLine()
            if defline == home:
              masterLines[team1][k].addDefPossession()
    else:
      print "Couldn't Find turner in lineup", string
      print turner, home, away
    # if "steals" in string:
    #   getSteal(string, home)
    #   stats[15] += 1

  elif "bad pass" in string:
    end = string.find("bad")
    turner = string[:end-1]
    checkHome = getTeam(home, turner)
    checkAway = getTeam(away, turner)
    if checkHome:
      for i in range(len(masterLines[team1])):
        line = masterLines[team1][i].getLine()
        if line == home:
          masterLines[team1][i].addTurnover()
          masterLines[team1][i].addPossession()
          for k in range(len(masterLines[team2])):
            defline = masterLines[team2][k].getLine()
            if defline == away:
              masterLines[team2][k].addDefPossession()
    elif checkAway:
      for i in range(len(masterLines[team2])):
        line = masterLines[team2][i].getLine()
        if line == away:
          masterLines[team2][i].addTurnover()
          masterLines[team2][i].addPossession()
          for k in range(len(masterLines[team1])):
            defline = masterLines[team1][k].getLine()
            if defline == home:
              masterLines[team1][k].addDefPossession()
    else:
      print "Couldn't Find turner in lineup", string
      print turner, home, away
  #   # if "steals" in string:
  #   #   getSteal(string, home)
  #   #   stats[15] += 1

  elif "traveling" in string:
    end = string.find("traveling")
    turner = string[:end]
    checkHome = getTeam(home, turner)
    checkAway = getTeam(away, turner)
    if checkHome:
      for i in range(len(masterLines[team1])):
        line = masterLines[team1][i].getLine()
        if line == home:
          masterLines[team1][i].addTurnover()
          masterLines[team1][i].addPossession()
          for k in range(len(masterLines[team2])):
            defline = masterLines[team2][k].getLine()
            if defline == away:
              masterLines[team2][k].addDefPossession()
    elif checkAway:
      for i in range(len(masterLines[team2])):
        line = masterLines[team2][i].getLine()
        if line == away:
          masterLines[team2][i].addTurnover()
          masterLines[team2][i].addPossession()
          for k in range(len(masterLines[team1])):
            defline = masterLines[team1][k].getLine()
            if defline == home:
              masterLines[team1][k].addDefPossession()
    else:
      print "Couldn't Find turner in lineup", string
      print turner, home, away

  return

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
      for i in range(len(masterLines[team1])):
        line = masterLines[team1][i].getLine()
        if line == home:
          masterLines[team1][i].addPointsFor(points)
          for j in range(len(masterLines[team2])):
            oppLine = masterLines[team2][j].getLine()
            if oppLine == away:
              masterLines[team2][j].addPointsAgainst(points)
      if last:
        masterLines[team1][i].addPossession()
        masterLines[team2][j].addDefPossession()
    elif checkAway:
      for i in range(len(masterLines[team2])):
        line = masterLines[team2][i].getLine()
        if line == away:
          masterLines[team2][i].addPointsFor(points)
          for j in range(len(masterLines[team1])):
            oppLine = masterLines[team1][j].getLine()
            if oppLine == home:
              masterLines[team1][j].addPointsAgainst(points)
      if last:
        masterLines[team2][i].addPossession()
        masterLines[team1][j].addDefPossession()
    else:
      print "Couldn't Find shooter in lineup", string
      print shooter, home, away
  elif "three" in string:
    points = 3
    if checkHome:
      for i in range(len(masterLines[team1])):
        line = masterLines[team1][i].getLine()
        if line == home:
          masterLines[team1][i].addPointsFor(points)
          masterLines[team1][i].addPossession()
          for j in range(len(masterLines[team2])):
            oppLine = masterLines[team2][j].getLine()
            if oppLine == away:
              masterLines[team2][j].addPointsAgainst(points)
              masterLines[team2][j].addDefPossession()
    elif checkAway:
      for i in range(len(masterLines[team2])):
        line = masterLines[team2][i].getLine()
        if line == away:
          masterLines[team2][i].addPointsFor(points)
          masterLines[team2][i].addPossession()
          for j in range(len(masterLines[team1])):
            oppLine = masterLines[team1][j].getLine()
            if oppLine == home:
              masterLines[team1][j].addPointsAgainst(points)
              masterLines[team1][j].addDefPossession()
    else:
      print "Couldn't Find shooter in lineup", string
      print shooter, home, away
  else:
    points = 2
    if checkHome:
      for i in range(len(masterLines[team1])):
        line = masterLines[team1][i].getLine()
        if line == home:
          masterLines[team1][i].addPointsFor(points)
          masterLines[team1][i].addPossession()
          for j in range(len(masterLines[team2])):
            oppLine = masterLines[team2][j].getLine()
            if oppLine == away:
              masterLines[team2][j].addPointsAgainst(points)
              masterLines[team2][j].addDefPossession()
    elif checkAway:
      for i in range(len(masterLines[team2])):
        line = masterLines[team2][i].getLine()
        if line == away:
          masterLines[team2][i].addPointsFor(points)
          masterLines[team2][i].addPossession()
          for j in range(len(masterLines[team1])):
            oppLine = masterLines[team1][j].getLine()
            if oppLine == home:
              masterLines[team1][j].addPointsAgainst(points)
              masterLines[team1][j].addDefPossession()
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

def getRebound(string, home, away, team1, team2, masterLines):
  if "team" in string:
    if "defensive" in string:
      end = string.find("defensive")
      team = string[:end-1]
      if masterKeys[team1] in nameCheck[team]:
        for i in range(len(masterLines[team2])):
          line = masterLines[team2][i].getLine()
          if line == away:
            masterLines[team2][i].addPossession()
            for k in range(len(masterLines[team1])):
              defline = masterLines[team1][k].getLine()
              if defline == home:
                masterLines[team1][k].addDefPossession()
      elif masterKeys[team2] in nameCheck[team]:
        for i in range(len(masterLines[team1])):
          line = masterLines[team1][i].getLine()
          if line == home:
            masterLines[team1][i].addPossession()
            for k in range(len(masterLines[team2])):
              defline = masterLines[team2][k].getLine()
              if defline == away:
                masterLines[team2][k].addDefPossession()
    return 0
  else:
    if "defensive" in string:
      end = string.find("defensive")
      boarder = string[:end]
      checkHome = getTeam(home, boarder)
      if checkHome:
        for i in range(len(masterLines[team1])):
          line = masterLines[team1][i].getLine()
          if line == home:
            masterLines[team1][i].addRebound()
            masterLines[team1][i].addDefPossession()
            for k in range(len(masterLines[team2])):
              possline = masterLines[team2][k].getLine()
              if possline == away:
                masterLines[team2][k].addPossession()
                return
      else:
        for i in range(len(masterLines[team2])):
          line = masterLines[team2][i].getLine()
          if line == away:
            masterLines[team2][i].addRebound()
            masterLines[team2][i].addDefPossession()
            for k in range(len(masterLines[team1])):
              possline = masterLines[team1][k].getLine()
              if possline == home:
                masterLines[team1][k].addPossession()
                return

    else:
      end = string.find("offensive")
      boarder = string[:end]
      checkHome = getTeam(home, boarder)
      if checkHome:
        for i in range(len(masterLines[team1])):
          line = masterLines[team1][i].getLine()
          if line == home:
            masterLines[team1][i].addRebound()
            return
      else:
        for i in range(len(masterLines[team2])):
          line = masterLines[team2][i].getLine()
          if line == away:
            masterLines[team2][i].addRebound()
            return
    return 1


def getPlayersAndStarters(soup, players1, players2,
                          starters1, starters2, masterKeys):
  rowIndex = 0
  start = 0
  bench = 0
  teamCount = 0
  firstTeamCount = 0
  for row in soup.find_all("tr"):
    for i in range(len(masterKeys)):
      if masterKeys[i] in row.text:
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
  playerOut = getPlayerOut(row, players1, players2)
  playerIn = getPlayerIn(row, players1, players2)

  # print
  # print "player in:", playerIn
  # print "player out:", playerOut

  if playerOut in curLine1:
    curLine1.append(playerIn)
    curLine1.remove(playerOut)

  elif getPlayerOut(row, players1, players2) in curLine2:
    curLine2.append(playerIn)
    curLine2.remove(playerOut)

  else:
    print "ERROR in getSubs"

  return curLine1, curLine2, playerIn

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

def appendLine(masterLines, line1, line2, team1, team2):
  line1.sort()
  line2.sort()
  temp1 = copy.deepcopy(line1)
  temp2 = copy.deepcopy(line2)

  new1 = 1
  new2 = 1

  for i in range(len(masterLines[team1])):
    if temp1 == masterLines[team1][i].getLine():
      new1 = 0
  if new1 == 1:
    masterLines[team1].append(lineup(temp1))

  for i in range(len(masterLines[team2])):
    if temp2 == masterLines[team2][i].getLine():
      new2 = 0
  if new2 == 1:
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

  masterKeys = []
  masterLines = [[] for i in range(30)]

  masterKeys.append("ATL")
  masterKeys.append("BKN")
  masterKeys.append("BOS")
  masterKeys.append("CHA")
  masterKeys.append("CHI")
  masterKeys.append("CLE")
  masterKeys.append("DAL")
  masterKeys.append("DEN")
  masterKeys.append("DET")
  masterKeys.append("GSW")
  masterKeys.append("HOU")
  masterKeys.append("IND")
  masterKeys.append("LAC")
  masterKeys.append("LAL")
  masterKeys.append("MEM")
  masterKeys.append("MIA")
  masterKeys.append("MIL")
  masterKeys.append("MIN")
  masterKeys.append("NO")
  masterKeys.append("NYK")
  masterKeys.append("OKC")
  masterKeys.append("ORL")
  masterKeys.append("PHI")
  masterKeys.append("PHX")
  masterKeys.append("POR")
  masterKeys.append("SAC")
  masterKeys.append("SA")
  masterKeys.append("TOR")
  masterKeys.append("UTA")
  masterKeys.append("WAS")

  return masterLines, masterKeys

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

# once we know who starts each quarter, this will track all changes
def getLineChangesAddTime(pbpRows, time, start, end, players1,
                   players2, curLine1, curLine2,
                   team1, team2, masterLines):

  time1 = 720
  time2 = 0
  
  for i in range(start, end):
    play = pbpRows[i]

    if isSub(pbpRows[i]):

      time2 = stringToSeconds(time[i])
      timeSegment = time1 - time2

      addLineTime(masterLines, curLine1, curLine2, team1, team2, timeSegment)

      curLine1, curLine2, player = getSubs(pbpRows[i], players1, players2,
                                           curLine1, curLine2)

      appendLine(masterLines, curLine1, curLine2, team1, team2)
      time1 = stringToSeconds(time[i])

    elif isStat(play, "rebound"):
      rebs = getRebound(play, curLine1, curLine2, team1, team2, masterLines)

    elif isStat(play, "makes"):
      getScore(play, curLine1, curLine2, team1, team2, masterLines)

    elif isTurnover(play):
      getTurnover(play, curLine1, curLine2, team1, team2, masterLines)

  return curLine1, curLine2, time1

def quarterTracking(pbpRows, time, start, end, players1, players2,
                    team1, team2, masterLines):

  qStarters1, qStarters2 = getQuarterStarters(pbpRows, start, end,
                                            players1, players2)

  appendLine(masterLines, qStarters1, qStarters2, team1, team2)

  curLine1, curLine2, timeRemaining = getLineChangesAddTime(pbpRows, time,
                                    start, end, players1, players2, qStarters1,
                                    qStarters2, team1, team2, masterLines)

  addLineTime(masterLines, curLine1, curLine2, team1, team2, timeRemaining)

def firstQuarterTracking(pbpRows, time, start, end, players1, players2,
                         starters1, starters2, team1, team2, masterLines):
  starters1.sort()
  starters2.sort()
  temp1 = copy.deepcopy(starters1)
  temp2 = copy.deepcopy(starters2)
  masterLines[team1].append(lineup(temp1))
  masterLines[team2].append(lineup(temp2))

  curLine1, curLine2, timeRemaining = getLineChangesAddTime(pbpRows, time,
                                    start, end, players1, players2, starters1,
                                    starters2, team1, team2, masterLines)

  addLineTime(masterLines, curLine1, curLine2, team1, team2, timeRemaining)


def main():

# begin storing lineups
  global masterKeys
  masterLines, masterKeys = lineupStorage()

  global nameCheck
  lineCheck = masterKeys
  NickNames = getNickNames()
  nameCheck = NicknametoTeam(NickNames, lineCheck)

  players1, players2, starters1, starters2, \
    curLine1, curLine2 = ([] for i in range(6))

# initialize players and starters lists using box score data
  boxScoreSoup = getSoup("http://espn.go.com/nba/boxscore?gameId=400489637")
  players1, players2, starters1, \
  starters2, team1, team2 = getPlayersAndStarters(boxScoreSoup, players1,
                            players2, starters1, starters2, masterKeys)

# pull the play by play data
  pbpSoup = \
    getSoup("http://espn.go.com/nba/playbyplay?gameId=400489637&period=0")

# put the soup in a list data structure and add quarter markers
  q2, q3, q4, pbpRows, time = pbpStructure(pbpSoup)

  end = len(pbpRows)

  '''first quarter tracking'''
  firstQuarterTracking(pbpRows, time, 0, q2, players1, players2,
                       starters1, starters2, team1, team2, masterLines)

  '''second quarter tracking'''
  quarterTracking(pbpRows, time, q2, q3, players1, players2,
                  team1, team2, masterLines)

  '''third quarter tracking'''
  quarterTracking(pbpRows, time, q3, q4, players1, players2,
                  team1, team2, masterLines)

  '''fourth quarter tracking'''
  quarterTracking(pbpRows, time, q4, end, players1, players2,
                  team1, team2, masterLines)

  '''prints out all lineups and some tabulated statistics'''
  printLinesInfo(masterLines, masterKeys, team1, team2)

  printTeamTotals(masterLines, masterKeys, team1, team2)

main()
