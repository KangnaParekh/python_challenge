#import library
import os
import csv

#path to collect data from the resource folder
election_data=os.path.join('resources','election_data.csv')

#introduce variables and set to zero
candidate_options=[]
candidate_votes={}
total_votes=0

#calculate the winning candidates
winning_candidates=""

#calculate the vote count
winning_count=0

#calculate the winning percentage
winning_percentage=0

#open and read the csv file
with open(election_data,newline="") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")


    #read the header row
    headers = next(csvreader)

# Print each row in CSV file.
    for row in csvreader:
 # Add to the total vote count.
        total_votes +=1
# Print candidate name from each row
        candidate_name = row[2]
# If the candidate does not match any existing candidate...
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name]=1
        else:
            candidate_votes[candidate_name]+=1
    

# Save results to the text file
with open("output.txt","w") as txt_file:
# Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
# Save the final vote count to the next file.
    txt_file.write(election_results)

 #Print the total votes
 # Determine the percentage of votes for each candidate by looping through the counts.
    
    for candidate_name in candidate_votes:
        
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        
 # Determine winning vote count and candidate
 # Print the candidate list
        candidate_results = (f"{candidate_name}: {vote_percentage}% ({votes:,})\n")
# Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
#  Save the candidate results to our text file.
        txt_file.write(candidate_results)
#  Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):

#Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
#Print the candidate name and percentage of votes.
        #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)