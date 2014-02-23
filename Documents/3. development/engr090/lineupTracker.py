def main():
  #Spurs
  lineup1 = ["Duncan", "Parker", "Ginabli", "Splitter", "Leanard"]
  lineup2 = ["Duncan", "Mills", "Ginabli", "Splitter", "Leanard"]
  lineup3 = ["Diaw", "Parker", "Ginabli", "Splitter", "Green"]
 
  #Pacers
  lineup4 = ["Hibbert", "George", "Hill", "Stephenson", "West"]
  lineup5 = ["Hibbert", "George", "Bynam", "West", "Stephenson"]

  #Wizards
  lineup6 = ["Wall", "Nene", "Bradley", "Ariza", "Gortat"]

  #sort so same names with a different order are considered as the same lineup
  lineup1.sort()
  lineup2.sort()
  lineup3.sort()
  lineup4.sort()
  lineup5.sort()
  lineup6.sort()

  #lists can't be hashed, so turn them into strings
  lineup1_string = list_to_string(lineup1)
  lineup2_string = list_to_string(lineup2)
  lineup3_string = list_to_string(lineup3)
  lineup4_string = list_to_string(lineup4)
  lineup5_string = list_to_string(lineup5)
  lineup6_string = list_to_string(lineup6)
 
  print "list_to_string(lineup1): ", lineup1_string  

  #give each lineup a unique integer id
  #do this so we can loop through all of the lineups easily...
  lineup_to_id = {}
  
  lineup_to_id[lineup1_string] = 1
  lineup_to_id[lineup2_string] = 2
  lineup_to_id[lineup3_string] = 3
  lineup_to_id[lineup4_string] = 4
  lineup_to_id[lineup5_string] = 5
  lineup_to_id[lineup6_string] = 6
  
  print "lineup_to_id[lineup1_string]: ", lineup_to_id[lineup1_string]


  #this dict keeps all of the lineups with stats
  stats = {}
  #    id  = lineup, pts per game, pts against, minutes played, +/- 
  stats[1] = [lineup1, 100, 98, 480, 100]
  stats[2] = [lineup2, 109, 112, 100, -40]
  stats[3] = [lineup3, 94, 94, 200, 0]
  stats[4] = [lineup4, 100, 99, 410, 56]
  stats[5] = [lineup5, 87, 98, 280, -160]
  stats[6] = [lineup6, 101, 105, 380, -200]

  #What an entry looks like...
  for i in range(1,7):
    data = stats[i]
    print "entry ", i, ": ", data[0], ": ", data[1:]
  

  #Example: get the best pts per game average
  pts_per_game = 0
  for i in range(1,7):
    data = stats[i]
    line = data[0]
    pts = data[1]

    if pts > pts_per_game:
      pts_per_game = pts
      best_line = line

  print "Best pts per game average: ", best_line, " - ", pts_per_game

  #I'd also make list of lists for each team...
  master_list = []
  #atlanta would be 0, washington would be 29
  for i in range(30):
    master_list.append([])

  #now you should append each lineup to the ind. teams lineup list
  #should do this right after you read in data

  #spurs
  master_list[27].append(stats[1])
  master_list[27].append(stats[2])
  master_list[27].append(stats[3])

  #pacers
  master_list[15].append(stats[4])
  master_list[15].append(stats[5])

  #wizards
  master_list[29].append(stats[6])

  #by doing this, you can get best lineups for each team
  #for example, get the best spurs lineup that scores the most per game

  pts_per_game = 0
  for data in master_list[27]:
    line = data[0]
    pts = data[1]

    if pts > pts_per_game:
      pts_per_game = pts
      best_line = line

  print "Best Spurs pts per game average: ", best_line, " - ", pts_per_game


  #lastly, you can easily get overall lineup averages  
  pts_per_game_avg = 0
  for i in range(1,7):
    data = stats[i]
    pts = data[1]
    print pts

    pts_per_game_avg += pts


  print "Average pts per game average: ", pts_per_game_avg / 6.0




def list_to_string(lineup):

  string = ""
  for name in lineup:
    string = string + name + ","

  return string




main()