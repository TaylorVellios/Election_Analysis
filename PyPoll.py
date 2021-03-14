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

winner_vote_count = 0
winner_vote_percent = 0.0
winner_name = ""

# ---------LOOP TO DISPLAY EACH CANDIDATES % OF VOTE AND TOTAL COUNT - DETERMINE WINNER AND STORE IN VARIABLES
print("-----------------------------------------------")
for cand, vote_p in voting_percents.items():
    print(f"{cand}: {round(vote_p,1)}%  ({candidate_votes[cand]:,})")
    if (candidate_votes[cand] > winner_vote_count) and (vote_p > winner_vote_percent):
        winner_vote_count = candidate_votes[cand]
        winner_vote_percent = vote_p
        winner_name = cand
print("------------------------------------------------\n")

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winner_name}\n"
    f"Winning Vote Count: {winner_vote_count:,}\n"
    f"Winning Percentage: {winner_vote_percent:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)





with open(file_to_write, 'w') as OutputFile:

    OutputFile.write("")
OutputFile.close()