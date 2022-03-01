# Imports Pandas Library and assigns it to the 'pd' variable
import pandas as pd

# Import os library
import os

# Load data from CSV file
# file_to_load = os.path.join("Resources", "short_election_results.csv")
file_to_load = os.path.join("Resources", "election_results.csv")
df = pd.read_csv(file_to_load)

# Creates a list of candidates from the dataframe
Candidates_List = df['Candidate'].values.tolist()
# Removes duplicates from the list of Candidates
Candidates_List = list(set(Candidates_List))

# Creates a list of counties from the dataframe
Counties_List = df['County'].values.tolist()
# Removes duplicates from the list of Counties
Counties_List = list(set(Counties_List))

# Count the total votes in the election
totalVotesElection = df['Ballot ID'].count()

# Count of the votes per county
Votes_By_County = []
for County in Counties_List:
    Result_County = df[df['County'] == County]
    My_Index = Result_County.index
    Number_Of_Votes = len(My_Index)
    My_Tuple = (County, Number_Of_Votes)
    Votes_By_County.append(My_Tuple)

for County_Name, County_Votes in Votes_By_County:
    County_Tuple = (County_Name, County_Votes)

# Sort the Votes_By_County list to get the county with more votes
# Reverse = True means that the list will have a descending order 
Votes_By_County.sort(key=lambda x:x[1], reverse = True)
My_Tuple_County_Winner = Votes_By_County[0]

# Count of the votes per candidate
Votes_Per_Candidate = []
for Candidate in Candidates_List:
    Result_Candidate = df[df['Candidate'] == Candidate]
    My_Index = Result_Candidate.index
    Number_Of_Votes = len(My_Index)
    My_Tuple = (Candidate, Number_Of_Votes)
    Votes_Per_Candidate.append(My_Tuple)


# Sort the Votes_Per_Candidate list to get the winner
# Reverse = True means that the list will have a descending order 
Votes_Per_Candidate.sort(key=lambda x:x[1], reverse = True)
My_Tuple_Winner = Votes_Per_Candidate[0]


# Output of the election results on screen
print()
print("Election Results")
print("-------------------------")
print("Total Votes: {:,}".format(totalVotesElection))
print("-------------------------")
print()
print("County Votes:")
for County_Name, County_Votes in Votes_By_County:
    CountyVotesPercentage = (County_Votes/totalVotesElection)
    # Note: the sep = '' at the end of the line keeps the spacing between variables and strings as a minimum.  It means Separator = Empty String
    print(County_Name,": ", "{:.1%}".format(CountyVotesPercentage), " ({:,})".format(County_Votes), sep = '')
print()
print("-------------------------")
print("Largest County Turnout: ", My_Tuple_County_Winner[0])
print("-------------------------")
print()
for Candidate, Number_Of_Votes in Votes_Per_Candidate:
    CandidateVotesPercentage = (Number_Of_Votes/totalVotesElection)
    # Note: the sep = '' at the end of the line keeps the spacing between variables and strings as a minimum.  It means Separator = Empty String
    print(Candidate,": ", "{:.1%}".format(CandidateVotesPercentage), " ({:,})".format(Number_Of_Votes), sep = '')
print()
print("-------------------------")
print("Winner:", My_Tuple_Winner[0])
print("Winning Vote Count:", "{:,}".format(My_Tuple_Winner[1]))
Winning_Percentage = My_Tuple_Winner[1]/totalVotesElection
print("Winning Percentage:","{:.1%}".format(Winning_Percentage))
print("-------------------------")
print()


# Output of the election results to a TXT file
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_results.txt")

# We use the sys library to redirect the print() function to write to a file instead of the screen
# and use the same print structure created for the screen section above 
import sys

original_stdout = sys.stdout # Save a reference to the original standard output

with open(file_to_save, 'w') as f:
    sys.stdout = f # Change the standard output to the file we created.
    print()
    print("Election Results")
    print("-------------------------")
    print("Total Votes: {:,}".format(totalVotesElection))
    print("-------------------------")
    print()
    print("County Votes:")
    for County_Name, County_Votes in Votes_By_County:
        CountyVotesPercentage = (County_Votes/totalVotesElection)
        # Note: the sep = '' at the end of the line keeps the spacing between variables and strings as a minimum.  It means Separator = Empty String
        print(County_Name,": ", "{:.1%}".format(CountyVotesPercentage), " ({:,})".format(County_Votes), sep = '')
    print()
    print("-------------------------")
    print("Largest County Turnout: ", My_Tuple_County_Winner[0])
    print("-------------------------")
    print()
    for Candidate, Number_Of_Votes in Votes_Per_Candidate:
        CandidateVotesPercentage = (Number_Of_Votes/totalVotesElection)
        # Note: the sep = '' at the end of the line keeps the spacing between variables and strings as a minimum.  It means Separator = Empty String
        print(Candidate,": ", "{:.1%}".format(CandidateVotesPercentage), " ({:,})".format(Number_Of_Votes), sep = '')
    print()
    print("-------------------------")
    print("Winner:", My_Tuple_Winner[0])
    print("Winning Vote Count:", "{:,}".format(My_Tuple_Winner[1]))
    Winning_Percentage = My_Tuple_Winner[1]/totalVotesElection
    print("Winning Percentage:","{:.1%}".format(Winning_Percentage))
    print("-------------------------")
    print()
f.close()
sys.stdout = original_stdout # Reset the standard output to its original value

