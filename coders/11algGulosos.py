#List of states to include and creat hash table 
states_include=set(["ab", "cd", "ef", "gh", "ij", "kl", "mn","op"])
stations={}
stations["Ione"]=set(["ab", "cd", "ef")]
stations["Itwo"]=set(["op", "ab", "ij"])
stations[("Ithree")]=set(["mn", "cd", "kl"])
stations[("Ifour")]=set(["cd", "ef"])
stations[("Ifive")]=set(["kl", "gh"])

#Store the final set of stations
stations_end=set()

#As long as states need coverage
while states_include:
  best_station = None
  states_covered = set()
  for station, states_station in stations.items():
    covered=states_include & states_stations:
      if len(covered)>len(states_covered):
        best_station=station
        states_covered=covered
states_include-=states_covered
stations_end.add(best_station)

print(stations_end)
