# PyPoll.py

import os
import csv

# ---------LOAD FROM SYS - OS.PATH.JOIN WILL AUTOMATICALLY CONNECT A HIGHER FOLDER TO A FILEWITHIN
file_to_load = os.path.join('Resources','election_results.csv')

# ---------CREATE VARIABLE FOR OUTPUT FILE
file_to_write = os.path.join('analysis', 'election_analysis.txt')

print()

# ---------DECLARE THE GLOBAL VARIABLES
total_votes = 0
Candidates = []
candidate_votes = {}
counties = []
county_votes = {}

# ---------OPEN THE FILE, SEPARATE THE HEADER LINE, ITERATE THROUGH ROWS OF DATA
with open(file_to_load,'r') as vote_data:
    reader = csv.reader(vote_data)
    headers = next(reader)

    # print(headers)

    for i in reader:
        county_name = i[1]
        candidate_name = i[2]
        total_votes += 1

# -----------PULL UNIQUE CANDIDATE NAMES, INITIALIZE DICTIONARY COUNTS FOR EACH CANDIDATE    
        if candidate_name not in Candidates:
            Candidates.append(candidate_name)
            candidate_votes[candidate_name] = 0
        
# -----------PULL UNIQUE COUNTY NAMES, INITIALIZE DICTIONARY COUNTS FOR EACH COUNTY 
        if county_name not in counties:
            counties.append(county_name)
            county_votes[county_name] = 0

# -----------COUNT VOTES FOR EACH CANDIDATE/COUNTY
        candidate_votes[candidate_name] += 1
        county_votes[county_name] += 1

# -----------WRITING RESULTS TO TXT FILE       
with open(file_to_write, 'w') as OutputFile:

# Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        "County Votes:\n")
    

    print(election_results, end="")
    print()

    # Save the final vote count to the text file.
    OutputFile.write(election_results)


# -----------DICTIONARY COMPREHENSIONS TO CONVERT OUR DICTIONARIES WITH {KEYS:COUNTS} TO {KEYS:%}
    voting_percents = {k:((v / total_votes) * 100) for k,v in candidate_votes.items()}
    counties_percents = {k:((v / total_votes)* 100) for k,v in county_votes.items()}


# -----------INITIALIZE VARIABLES FOR VALUES TO PRINT TO TERMINAL/WRITE TO FILE 
    winner_vote_count = 0
    winner_vote_percent = 0.0
    winner_name = ""

    county_vote_count = 0
    county_vote_percent = 0
    largest_county = ''

# -----------LOOP TO DISPLAY AND ASSIGN VALUES TO CONDITIONAL VARIABLES FOR COUNTY INFO - WRITE TO FILE/PRINT TO CONSOLE
    space = len(max(counties)) + 1

    for c , v in counties_percents.items():
        inside_space = ' ' * (space - len(c))
        county_results = (f'{c}:{inside_space}{round(v,1)}% -- ({county_votes[c]:,})\n')
        print(county_results)
        OutputFile.write(county_results)

        if (county_votes[c] > county_vote_count) and (v > county_vote_percent):
            county_vote_count = county_votes[c]
            county_vote_percent = v
            largest_county = c

# -----------INITIALIZING A STRING TO PRINT SPECIFIC COUNTY DATA
    biggest_turnout = (
        f"-------------------------\n"
        f"Largest County Turnout: {largest_county}\n"
        f"-------------------------\n"
        )

    print(biggest_turnout)
    OutputFile.write(biggest_turnout)

# -----------LOOP TO DISPLAY AND ASSIGN VALUES TO CONDITIONAL VARIABLES FOR BALLOT INFO - WRITE TO FILE/PRINT TO CONSOLE
    space = len(max(Candidates)) + 5

    for cand, vote_p in voting_percents.items():
        inside_space = ' ' * (space - len(cand))
        candidate_results = (f"{cand}:{inside_space}{round(vote_p,1)}% -- ({candidate_votes[cand]:,})\n")
        print(candidate_results)
        OutputFile.write(candidate_results)


        if (candidate_votes[cand] > winner_vote_count) and (vote_p > winner_vote_percent):
            winner_vote_count = candidate_votes[cand]
            winner_vote_percent = vote_p
            winner_name = cand
    

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winner_name}\n"
        f"Winning Vote Count: {winner_vote_count:,}\n"
        f"Winning Percentage: {winner_vote_percent:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)


    OutputFile.write(winning_candidate_summary)