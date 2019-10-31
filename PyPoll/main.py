# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 20:41:37 2019

@author: tdryg
"""
# Import modules
import csv
import os

# Create path to csv
csvpath = os.path.join('election_data.csv')

# Total Votes Counter
total_votes = 0

# Candidate options and vote counter
candidate_option = []
candidate_votes = {}

# Winning candidate and vote counter
winning_count = 0
winning_candidate = ""

# Read csv
with open(csvpath, 'r') as csvfile:
    data = csv.reader(csvfile, delimiter= ',')

    # Read the header
    header = next(data)

    for row in data:

        # Count total votes
        total_votes += 1

        # Extract candidate name from each row
        candidate_name = row[2]

        if candidate_name not in candidate_option:

            # Add candidate name to candidate_option
            candidate_option.append(candidate_name)

            # Add to the candidates vote counter
            candidate_votes[candidate_name] = 0
            candidate_votes[candidate_name] += 1
        else:
            candidate_votes[candidate_name] += 1

# Export results to text file and print to terminal
export_path = os.path.join('Election_Results.txt')
with open(export_path, "w") as txt_file:
    output_1 = (
    f"\nElection Results\n"
    f"----------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"----------------------------\n")
    txt_file.write(output_1) 

    print(output_1)

    # Determine vote count
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]

        # Calculate vote percentages
        vote_percentage = (votes/total_votes) * 100

        # Determine winning candidate and vote count
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        # Print each candidate's voter count and percentage (to terminal)
        output_2 = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        txt_file.write(output_2)
        print(output_2)

    # Print winning candidate and export to text file
    output_3 = (
        f"--------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"--------------------------")
    txt_file.write(output_3)
print(output_3)