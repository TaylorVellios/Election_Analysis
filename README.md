## Ballot Counting in Python
# Overview
Analyzing election ballot data using the core mechanics of Python's CSV Library.<br>
The data used in this demonstration can be found in Resources/election_results.csv<br>
  - This file is based on the ballot data from Colorado's Congressional Race for District 1 in 2018


# Election-Audit Results
![election1](https://user-images.githubusercontent.com/14188580/111091610-7fc4d680-8501-11eb-848d-b7f02a62f9d9.PNG)

</br>
- From the data processed, there is a grand total of 369,711 votes that were counted. This number can be confirmed in the .CSV file that has an extra header row.<br>
- While processing the data within this .csv file, this python program creates dictionary keys of unique candidates and values of the votes they received; as well as the counties from where the votes were cast and how many came from those counties. From the file used in this analysis: Denver County consisted of 82.8% of tallied votes with 306,055, Jefferson County consisted of 10.5% of votes with 38,855, and Arapahoe County made up the final 6.7% with 24,801 votes.<br>
- Denver County supplied the vast majority of votes, far outweighing the other two counties in this district. Considering the population similarities between Denver and Jefferson Counties, it is safe to say that not all of Jefferson is included within the borders of this congressional district.<br>
- Using the same main csv.reader() function as we iterated for County data, the Candidate data is as follows: Charles Casper Stockham received 23% of the vote with 85,213, Diana Degette received 73.8% of the vote with 272,892, and Raymon Anthony Doane made up the final 3.1% with 11,606 votes. Diana won by a landslide with over 187,000 votes more than her opponent.<br>

![election0](https://user-images.githubusercontent.com/14188580/111091616-83585d80-8501-11eb-9660-d6d969ad7832.PNG)

# Election-Audit Summary
What makes this python script so versatile is its data collection system - by using lists and dictionaries we can theoretically output up to as many Candidates and Counties as these python objects allow: all without having to declare any of them manually! Another main advantage is processing speed. Opening and manipulating the .csv file in Excel can be a burden on many machines when there are nearly 370,000 rows of data to process. With only minor modifications, (changing iteration index numbers in the csv.reader() object), this script can be used reliably with any .csv containing voter data.
