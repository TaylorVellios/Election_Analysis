# PyPoll.py

import os
import csv

# ---------LOAD FROM SYS - OS.PATH.JOIN WILL AUTOMATICALLY CONNECT A HIGHER FOLDER TO A FILEWITHIN
file_to_load = os.path.join('Resources','election_results.csv')

# ---------WRITE TO TXT
file_to_write = os.path.join('analysis', 'election_analysis.txt')

print()


total_votes = 0
Candidates = []
candidate_votes = {}

# ---------OPEN THE FILE, SEPARATE THE HEADER LINE, ITERATE THROUGH ROWS OF DATA
with open(file_to_load,'r') as vote_data:
    reader = csv.reader(vote_data)
    headers = next(reader)

    print(headers)

    for i in reader:
        candidate_name = i[2]
        total_votes += 1

        if candidate_name not in Candidates:
            Candidates.append(candidate_name)
            candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] += 1


    print()        
    print(f"The Candidates Are: {', '.join(Candidates)}\n")
    print(f"Total Number of Votes: {total_votes}")
    print()

vote_data.close()

# ---------DICTIONARY COMPREHENSION TO CONVERT OUR VOTECOUNT DICTIONARY PER CANDIDATE INTO A PERCENTAGE OF TOTAL VOTE PER CANDIDATE
voting_percents = {k:((v / total_votes) * 100) for k,v in candidate_votes.items()}


# ---------LOOP TO DISPLAY EACH CANDIDATES % OF VOTE AND TOTAL COUNT
print("------------------------------------------------------------------------------")
for k,v in voting_percents.items():
    print(f"{k}: received {round(v,2)}% of the vote with {candidate_votes[k]} votes.")

print("------------------------------------------------------------------------------\n")


with open(file_to_write, 'w') as OutputFile:

    OutputFile.write("")
OutputFile.close()