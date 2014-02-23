#engr090 
#Joe Keedy & Noah Sterngold
#2/13/14

from bs4 import BeautifulSoup
import urllib


def isPBProw(row):
  if row[2] == ':' or row[1] == ':':
    return 1
  else:
    return 0


#get this working, string is coming in as a BS NavigableString
def isScore(string):
  if len(string) > 0:
    if string[0].isdigit():
      for i in range(len(string)):
        if string[i] == ':':
          return 0
      return 1
    else:
      return 0
  return 0


def isSubstitution(string):
  if len(string) > 0:
    if "enters the game" in string:
      return 1
    else:
      return 0
  return 0

def getPlayer(string):
  count = 0
  for i in range(len(string)):
    if string[i] == " ":
      count += 1
      if count == 2:
        return string[:i]


def main():
  
  url = "http://espn.go.com/nba/playbyplay?gameId=400489639"

  #gets the url file pointer and retrieves the raw HTML from that url
  file_pointer = urllib.urlopen(url)
  soup = BeautifulSoup(file_pointer)


  for row in soup.find_all("tr"):
    col = 0
    for section in row.find_all("td"):
      col += 1
      if isSubstitution(section.text) and col == 2:
        player = getPlayer(section.text)
        print "Spurs sub: " + player
      if isSubstitution(section.text) and col == 4:
        player = getPlayer(section.text)
        print "Pistons sub: " + player

        



main()
