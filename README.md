# Election Analysis
Module 3 Challenge: Make use of Python language to open a CSV file containing the data with the congressional election results of three counties in the state of Colorado, calculate the total votes in the election, the total votes per county and per candidate and indicate the candidadte that has won the election.

## 1) Overview of Election Audit:

The state election commission needs to analyze the results of the elections in 3 counties of the state, for this purpose we have received a CSV file containing 3 columns and 369,712 rows (including the row with the column headers).

The election data does not contain information about blank votes or invalid votes.  **Each line of the CSV file corresponds to one valid vote.  This information is very important since the total number of votes for each candidate or county is obtained by counting the number of lines that meet certain criteria.  

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

The county with the largest number of votes was Denver with 82.8% of the total valid votes.  This result was not to be expected, since the population of the 3 counties analyzed  is similar:

Information from the 2022 Census shows that the number of inhabitants in each of the 3 counties is:

Denver     760,049

Arapahoe   670,969

Jefferson  593,348

- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.

- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?




## 3) Election Audit-Summary
