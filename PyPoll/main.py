import os
import csv

#Setting a path for the file
filepath = os.path.join('.', 'Resources', 'election_data.csv')

#Opening the CSV
with open(filepath, newline='') as csvfile:
    #CSV reader
    csvreader = csv.reader(csvfile, delimiter=',')

    #Reading the first row (header)
    csv_header = next(csvreader)

    #List of the candidates with number of votes
    candidate_list = [candidate[2] for candidate in csvreader]

#The number of total votes
total_votes = len(candidate_list)

candidates_info = [[candidate,candidate_list.count(candidate)] for candidate in set(candidate_list)]

#List of the candidates with the number of the votes
candidates_info = sorted(candidates_info, key=lambda x: x[1], reverse=True)

#Printing the results
print('Election Results')
print('---------------------')
print(f'Total Votes: {total_votes}')
print('---------------------')

for candidate in candidates_info:
    percent_votes = (candidate[1] / total_votes) * 100
    print(f'{candidate[0]}: {percent_votes:6.3f}% ({candidate[1]})')

print('--------------------')
print(f'Winner: {candidates_info[0][0]}')
print('----------------------')

#Printing results to text file
#Set path for file
filepath = os.path.join('.', 'Resources', 'PyPoll_Results.txt')
with open(filepath, 'w') as text_file:
    print('Election Results', file=text_file)
    print('----------------------', file=text_file)
    print(f'Total Votes: {total_votes}', file=text_file)
    print('---------------------', file=text_file)

    for candidate in candidates_info:
        percent_votes = (candidate[1] / total_votes) * 100
        print(f'{candidate[0]}: {percent_votes:6.3f}% ({candidate[1]})', file=text_file)

    print('--------------------', file=text_file)
    print(f'Winner: {candidates_info[0][0]}', file=text_file)
    print('----------------------', file=text_file)

