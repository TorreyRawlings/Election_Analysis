# The data we need to retrieve Resources/election_results.csv
# 1. The total number of votes cast
# 2. a complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Add our dependencies.
import csv 
# this imports the code needed to read a csv
import os
# imports code to work with file system/operating system
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize total vote counter
total_votes = 0
# Candidate Options
candidate_options = []

#Decalre the empty dictionary.

candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    #opens the file and names it election data
    file_reader = csv.reader(election_data)
    #this election data but turned into an object that help you manipuldate .csv

    # Read the header row.
    headers = next(file_reader)
     #'next' - interable (anything you can do step by step). isnt specific to headers, it just pulls the first thing in the iterable and if run again would pull the next set of data

    # Print each row in the CSV file.
    for row in file_reader:
    # add total vote count
        total_votes += 1
        #everytime you go through a row it adds 1
    #print the total votes 
        candidate_name = row[2]
        # [2] is really the 3rd column or 'C'
   # If the candidate does not match any existing candidate..     
        if candidate_name not in candidate_options:
     # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)  
     #begin tracking that candidates vote count
            candidate_votes[candidate_name] = 0
            #candidate_votes { "casper": 0 }

 # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
                    # candidate_votes { "charles": 2, "casper": 1 }

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.

for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
   
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
   
    print(winning_candidate_summary)
    
