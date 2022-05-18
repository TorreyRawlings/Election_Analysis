# Election_Analysis
#### The purpose of this analysis is to example and categorize all of the voting data for Colorado state elections to determine a winner and which county had the most votes. After auditing all the data here are some highlights: 

  - There was a total of 369,711 votes cast. 
  - Each county had the following votes / percentage of votes: 
     -  Jefferson: 38,855 votes / 10.5%
     -  Denver: 306,055 votes / 82.8% 
     -  Arapahoe: 24,801 votes / 6.7%
  - Denver by far had the majority of the votes taking up 82.8% of all votes.
  - Each candidate had the following votes / percentage of votes: 
     -  Charles Stockham: 85,213 votes / 23.0%
     -  Diana Degette: 272,892 votes / 73.8%
     -  Raymon Doane: 11,606 votes / 3.1% 
  - The winner by a significant amount was Diana Degette. She received nearly 3/4ths of all the votes counted.

## Summarizing how we were able to conclude the above information and how this can be utilized in the future: 

  In order to get the above stats for the election we used python. We created several variables, loops, mathematical calculations, lists and dictionaries to get the end result. You can review the whole code [here](https://github.com/TorreyRawlings/Election_Analysis/blob/main/PyPoll_Challenge.py) for further details. If you would like to utilize this script for a different election you will need to modify the following: 
  - Where the 'file_to_load' variable is defined, we have it joining to the .csv file we had the election information in. You would need to adjust the path given and the .csv file to whatever file you have your data stored.
  - Where the 'file_to_save' variable is definied, we have it set to an open txt file where we would print the information we collected. You would need to adjust this as well to the path to a new txt file to input the new results. 
  - Keep in mind this file only calculates the total number of votes, number of votes/percentage for each county, number of votes/percentage for each candidate. If you wanted to break it down even further, like calculate that for cities for example, then you would need to add additional code. Just to start you'd need a new list and dictionary created with newly defined variables as well as a for loop with an if statement to pull in this data. 

We hope this helps anyone in the future who is pulling data for election results.
