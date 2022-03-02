# Election Analysis
Module 3 Challenge: Make use of Python language to open a CSV file contianing the data with the congressional election results of three counties, calculate the total votes in the election, the total votes per county and per candidate and indicate the candidadte that has won the election.

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




- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.

- Which county had the largest number of votes?

- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.

- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?




## 3) Election Audit-Summary
