# PyPoll.py

import os
import csv

# LOAD FROM SYS - OS.PATH.JOIN WILL AUTOMATICALLY CONNECT A HIGHER FOLDER TO A FILEWITHIN
file_to_load = os.path.join('Resources','election_results.csv')

# WRITE TO TXT
file_to_write = os.path.join('analysis', 'election_analysis.txt')
print()
with open(file_to_load,'r') as vote_data:
    reader = csv.reader(vote_data)
    headers = next(reader)

    print(headers)
    Candidates = []
    Votes = {}
    for i in reader:
        if i[2] not in Candidates:
            Candidates.append(i[2])
    print(f"The Candidates Are: {', '.join(Candidates)}")
    #for i in reader:




vote_data.close()

with open(file_to_write, 'w') as OutputFile:

    OutputFile.write('Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson')
OutputFile.close()