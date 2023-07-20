#import necessary modules
import os
import csv

#create text file to export to
text_file = "Analysis/PyPoll_analysis.txt"
#locate file to pull data from
poll_data = os.path.join('Resources', 'election_data.csv')

#vote counter
vote_counter= 0
#create lists/dictionaires to be utilized later
candidate_choices = []
candidate_votes = {}

#create variables to be utilized later
winning_candidate = ""
winning_count = 0

#open up csv file as a dictionary to utilize header rows
with open(poll_data, "r") as csvfile:
    csvreader = csv.DictReader(csvfile)

    #start the loop for each row within the dictionary
    for row in csvreader:
        # count total number of rows (therefore counting total number of votes)
        vote_counter = vote_counter + 1

        #take the candidate name for each row and save it for later
        candidate_name = row["Candidate"]

        #run through each row reviewing candidate name; if it's not on the candate options list - add it; if it is, add a vote
        if candidate_name not in candidate_choices:
            candidate_choices.append(candidate_name)

            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

#Print total vote results and export to text file
with open(text_file, "w") as txt_file:
    
    election_results = (
        f"\n\nElection Results\n"
        f"-----------------------------------\n"
        f"Total Votes: {vote_counter}\n"
        f"-----------------------------------\n"
    )
    print(election_results)

    txt_file.write(election_results)

    #loop through vote counts
    for candidate in candidate_votes:
        #determine votes for each candate and use float to avoid being rounded
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes)/float(vote_counter) * 100

        #Winning count starts at zero, and if votes is greater, that becomes the new winning count & candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
        #breaking down each candidate with their % of vote and number of votes
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output)
        #print to same text file
        txt_file.write(voter_output)
        
    #adding winning candidate to text file
    winning_candidate_summary = (
        f"-----------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-----------------------------------\n"
    )

    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
             
           
