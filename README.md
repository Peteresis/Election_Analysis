# Election Analysis
Module 3 Challenge: Make use of Python language to open a CSV file containing the data with the congressional election results of three counties in the state of Colorado, calculate the total votes in the election, the total votes per county and per candidate and indicate the candidadte that has won the election.

## 1) Overview of Election Audit:

The state election commission needs to analyze the results of the elections in 3 counties of the state, for this purpose we have received a `CSV file` containing `3 columns` and `369,712 rows` (including the row with the column headers).

The election data does not contain information about blank votes or invalid votes.  **Each line of the CSV file corresponds to one valid vote**.  This information is very important since the total number of votes for each candidate or county is obtained by counting the number of lines that meet certain criteria.  

When reviewing the data received, we found the following:

The first row contains the column names, which are as follows (from left to right):

**Ballot ID**: The first column contains the serial numbers of each of the ballots.  The serial number is 7 digits long, all are numeric and no serial number is repeated or duplicated.

**County**: In the second column is the name of the county where the ballot was used.  The name of each county is a text string of variable length and is repeated on many lines, depending on the number of votes cast in each county.

**Candidate**: The names of the candidates are in the third column.  These are also text strings of variable length and are repeated in many lines, depending on the number of votes obtained by each Candidate.

From these three columns we can obtain the rest of the information to give the election results, as described in the next section.

### **Fig. 1: Sample of the data received**
![Sample of the Original Data Received](https://github.com/Peteresis/Election_Analysis/blob/985384a19c594494d89f71477fdba0e7eebf5ecc/Data%20Sample.png)

## 2) Election-Audit Results

### What were the results of the election?

After analyzing the data using the Python code created, the following report with the results of the election was obtained:

### **Fig. 2: Election Results Report Created with Python**
![Election Results Report](https://github.com/Peteresis/Election_Analysis/blob/a090a38f23e9e0bbc69fa9b851f1efc2a543875c/Election_Results.png)

- How many votes were cast in this congressional election?

Based on the data received, there were a total of `369,711` valid votes among the 3 counties audited.  It is not possible to determine the percentage of abstention nor the percentage of invalid or blank votes, since the data on the total number of registered voters and invalid or blank votes was not provided by the electoral commission authorities.

This is the code used to read the data and calculate the total number of votes in the election:
```
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
```
I chose the `pandas` Pyhton library over the `csv` library because it offers more sophisticated functionality for working with data read from a csv file.

The code shown above reads the data from the CSV file and then generates a list of counties `Counties_List` and candidates `Candidates_List` that will be used later in the code to generate results by county and candidate.

The total number of votes cast in the election is calculated by simply counting the number of rows in the first column `Ballot ID`, because each cell in this column contains a unique value, and so the number of elements in this column equals the total number of votes cast by the electors.


- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.

The total number of valid votes cast in each county is as follows:

  1. Denver: 82.8% (306,055)
  2. Jefferson: 10.5% (38,855)
  3. Arapahoe: 6.7% (24,801)

Below is the code used to calculate the number of votes per county:

```
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

```
The code generates an empty list called `Votes_By_County`, then loops through the list of counties produced in the previous section `Counties_List`, counting the number of rows in the data that have the same county name for each element in the `Counties_List`.

The code then adds a new element to the list called `Votes_By_County`.

The new element is added to the `County_Tuple`, which contains the variables `County_Name` and `County_Votes`.

Finally, the list `Votes_By_County` is sorted in descending order using the `lambda` function from Python.

The element `0` of `Votes_By_County` is copied to a Tuple called `My_Tuple_County_Winner` which contains the name of the county with higher vote turnout.  

- Which county had the largest number of votes?

The county with the largest number of votes was Denver with 82.8% of the total valid votes.  This result was not to be expected, since the population of the 3 counties analyzed  is similar.

Information from the 2022 Census shows that the number of inhabitants in each of the 3 counties is:

    - Denver     760,049
    - Arapahoe   670,969
    - Jefferson  593,348

The discrepancy in the number of votes cast in Denver County vs Arapahoe and Jefferson Counties suggests that the latter two counties had a significant rate of abstention.

- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.

There were 3 candidates in this election: Diana DeGette, Charles Casper Stockham and Raymon Anthony Doane.  The total number of votes obtained by each of the candidates was as follows:

  1. Diana DeGette: 73.8% (272,892)
  2. Charles Casper Stockham: 23.0% (85,213)
  3. Raymon Anthony Doane: 3.1% (11,606)

The code used to calculate the total number of votes per candidate is the following:

```
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

```

The code shown above is a copy of the code used to obtain the results by county, but the names of the lists and tuples and variables was changed to use the word `Candidate` instead of `County`.

- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

The election was won by the candidate `Diana DeGette` with a total of `272,892` votes or `73.8%` of the votes cast in the 3 counties.  Certainly a landslide victory.

The reader may have been expecting the analysis of the votes for each candidate in each county, however, that information was not part of the analysis requested for this challenge and therefore was not included in the code and in the analysis.

### Output Table

Once all the work of reading the data, organize it and calculate the total votes is done, the program creates the results table shown in `Fig #2` above.  This table is printed on the screen and also printed in a `TXT File` called `election_results.txt` included in the `Analysis` folder contained within this repository.

The code that generates the output table on the screen consists of a series of `print` statements and a couple of lines to calculate the percentages of votes received by county or by candidate vs the total votes cast in the election.

```
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
```
For the `TXT File` we used a "trick" and changed the standard output from the screen to a file using the `sys library` from Python.  This change allows to print the output table to a TXT File with minimal modifications to the code shown above.  

```
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
```

## 3) Election Audit-Summary

Python is a very versatile language with powerful libraries and functions to manipulate large amounts of data in a relatively easy way.  The use of lists makes it possible to access information very easily without requiring large code structures to obtain the value of a variable in a row or column of a data table.

The `369,712` rows of data contained in the `CSV file` are read very quickly and in a few seconds the table with the results of the analysis is obtained.

The code created for this analysis is made in a generic way so that it can be used for other analyses without modification.  It does not matter the number of candidates or counties to be audited.  Simply load the data with the election results into a `CSV file` containing `3 columns` and name the columns `Ballot ID`, `County` and `Candidate`.  The name of the data file can be different from `election_results`, but it has to be included in line 9 at the beginning of the code, so that the computer can find the file and do the work.

The complete code used in this analysis is included below:
```
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
```


