import os
import csv


#Creating an output path to store variables
print_path = os.path.join("..","Analysis","PyPoll_analyzed.txt")

# output string defined
output = (     
f'\n
Election Results\n\
-------------------------\n\
Total Votes: 3521001\n\
-------------------------\n\
Khan: 63.000% (2218231)\n\
Correy: 20.000% (704200)\n\
Li: 14.000% (492940)\n\
O'Tooley: 3.000% (105630)\n\
-------------------------\n\
Winner: Khan\n\
-------------------------\n'
 )

# declaring dictionary
candidate = {}






#variable for csv using Dictionary Reader
data = csv.DictReader(open(os.path.join('..','Resources','PyPoll','election_data.csv')))

for row in data:
    # print(row)
    





