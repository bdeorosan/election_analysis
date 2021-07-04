# Adding dependencies
import csv
import os
import math

# Assigning variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assigning variable to save a file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initializing variable that will hold total vote count
total_votes = 0

# Placeholder list to gather name of each candidate in the election
candidate_options = []

# Placeholder dictionary to gather the total votes for each candidate
candidate_votes = {}

#Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Opening the file to "read"; creating memory object named "election_data"
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Skipping header row during analysis
    headers = next(file_reader)
    # print(headers)

    # Iterate through all ballot rows and total the accumulation of iterations and fine candidate options
    for row in file_reader:
        total_votes += 1       
        candidate_name = row[2]        

        # Makikng sure unique candidate names only show up once within final options list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            # Start count with everyone at zero       
            candidate_votes[candidate_name] = 0

        # Track each candidate's vote count as the code iterates through the rows in the CSV
        candidate_votes[candidate_name] += 1

for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100

    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    # Winning vote count and candidate
    # Are votes greater than winning count?
    if (votes > winning_count) and (vote_percentage > winning_percentage):

        # If true then set winning_count = votes and winning_percent = vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage

        #And, set the winning_candidate equal to the candidate's name
        winning_candidate = candidate_name

for candidate in candidate_votes:
    winning_candidate_summary = (
        f"--------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------------\n")
    print(winning_candidate_summary)

    #print(f"{candidate_name}: received {round(vote_percentage, 1)}% of the vote.")

# Print the total number of iterations the for loop ran, 
# which is also the total number of votes cast in the election
print(total_votes)
print(candidate_options)
print(candidate_votes)

