import os
import csv

total_votes = -1
candidates = []
percents = []
totals = []
totals_candidate_0 = 0
totals_candidate_1 = 0
totals_candidate_2 = 0
totals_candidate_3 = 0

#input path
election_data_csv = os.path.join("..", "Resources", "PyPoll", "election_data.csv")

#pass in path variable and open csv for reading
with open(election_data_csv, 'r') as csvFile:

#specifying csv reader
  csvReader =csv.reader(csvFile, delimiter=',')
  for row in csvReader: 
    total_votes+= 1

    if (total_votes == 1):
      candidates.append(row[2])
      totals_candidate_0 += 1

    elif(total_votes > 1 ):

      if (row[2] not in candidates):        
        candidates.append(row[2])

      if (row[2] == candidates[0]):
        totals_candidate_0 += 1
      elif (row[2] ==  candidates[1]):
        totals_candidate_1 += 1 
      elif (row[2] ==  candidates[2]):
        totals_candidate_2 += 1 
      elif (row[2] ==  candidates[3]):
        totals_candidate_3 += 1  
  
  
  totals.append(totals_candidate_0)
  totals.append(totals_candidate_1)
  totals.append(totals_candidate_2)
  totals.append(totals_candidate_3)

  percent_0 = int(round((totals_candidate_0/total_votes)*100))
  percents.append(percent_0)
  percent_1 = int(round((totals_candidate_1/total_votes)*100))
  percents.append(percent_1)
  percent_2 = int(round((totals_candidate_2/total_votes)*100))
  percents.append(percent_2)
  percent_3 = int(round((totals_candidate_3/total_votes)*100))
  percents.append(percent_3)

  if (percent_0 > percent_1 & percent_0 > percent_2 & percent_0 > percent_3):
    candidates.append(candidates[0])
  elif (percent_1 > percent_0 & percent_1 > percent_2 & percent_1 > percent_3):
    candidates.append(candidates[1])
  elif (percent_2 > percent_1 & percent_2 > percent_0 & percent_2 > percent_3):
    candidates.append(candidates[2])
  elif (percent_3 > percent_1 & percent_3 > percent_2 & percent_3 > percent_0):
    candidates.append(candidates[3])
  else:
      candidates.append("Inconclusive")

# output string defined

output = (   
f"Election Results\n"
f"-------------------------\n"
f"Total: {total_votes}\n"
f"-------------------------\n"
f"{candidates[0]}: {percents[0]:.3f}% ({totals[0]})\n"
f"{candidates[1]}: {percents[1]:.3f}% ({totals[1]})\n"
f"{candidates[2]}: {percents[2]:.3f}% ({totals[2]})\n"
f"{candidates[3]}: {percents[3]:.3f}% ({totals[3]})\n"
f"-------------------------\n"
f"Winner: {candidates[4]}\n"
f"-------------------------\n"
)

print(output)


#Creating an output path to store variables
print_path = os.path.join("..","Analysis","PyPoll_analyzed.txt")

with open(print_path, "w") as textFile:
      textFile.write(output)




