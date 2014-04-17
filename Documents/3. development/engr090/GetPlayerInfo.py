#engr090
#Joe Keedy & Noah Sterngold
#2/13/14

from bs4 import BeautifulSoup
import urllib
import re



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

  return players1, players2, starters1, starters2, 0, 0

def getSubs(row, players1, players2, curLine1, curLine2):
  rowIndex = 0
  
  # print "\n"
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

def getInfo(soup, p1, p2):
  
  master = []
  for i in p1:
    master.append(i)
  for i in p2:
    master.append(i)

  number = ""
  position = ""
  PTM3 = 0
  PTA3 = 0
  threePerc = 0

  #Find number, position, height and weight of the player
  numpos = soup.find('li', attrs={'class' : 'first'})
  text = numpos.text
  for i in range(len(text)):
    if text[i] == " ":
      number = text[1:i]
      position = text[i+1:]
    i += 1
  hw = numpos.find_next('li')
  text2 = hw.text
  single = text2.find("'")
  double = text2.find('"')
  lbs = text2.find("lbs")
  feet = int(text2[:single])
  inches = int(text2[single+1:double])
  height = feet*12 + inches
  weight = int(text2[double+3:lbs-1])

  print
  print number
  print position
  print feet, inches, "(", height, "inches),", weight, "lbs."

  #Find Shooting Numbers
  count = 0
  for row in soup.find_all("tr"):
    check = row.text
    if "Regular Season" in check:
      for col in row.find_all("td"):
        if count == 5:
          threes = col.text
          for i in range(len(threes)):
            if threes[i] == "-":
              PTM3 = threes[:i]
              PTA3 = threes[i+1:]
        if count == 6:
          perc = float(col.text)
          threePerc = perc*100
        count += 1

  # print PTM3
  # print PTA3
  # print threePerc
  return

def getPlayerID(soup, players1, players2):
  links = soup.findAll('a', href=re.compile('http://espn.go.com/nba/player/_/id/'))
  cleanLinks = []
  for i in links:
    clean = i['href']
    begin = clean.find("player") + 7
    newlink = clean[:begin] + "stats/" + clean[begin:]
    cleanLinks.append(newlink)
    cleanLinks.sort()

  for i in cleanLinks:
    soupy = getSoup(i)
    getInfo(soupy, players1, players2)




def main():

  masterLines = lineupStorage()

  players1, players2, starters1, starters2, \
    curLine1, curLine2 = ([] for i in range(6))

  boxScoreSoup = getSoup("http://espn.go.com/nba/boxscore?gameId=400489636")
  players1, players2, starters1, starters2, team1, team2 = getPlayersAndStarters(boxScoreSoup,
                                                  players1, players2,
                                                  starters1, starters2,
                                                  masterLines)

# initialize players and starters lists using box score data
  print players1
  print players2
  print
  getPlayerID(boxScoreSoup, players1, players2)

  # infoSoup = getSoup("http://espn.go.com/nba/player/_/id/3244/thaddeus-young")
  # getInfo(infoSoup, players1, players2)



main()
