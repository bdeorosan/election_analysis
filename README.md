# An Analysis of Election Results

### UCBE Bootcamp: Week 3 - PyPolls - Seth and Tom need further help on their analysis of election results

#### Overview of Project
The purpose of this project was to use a Python script to determine the vote spread, by candidate and county, from a recently held election.  More specifically, the aim was to determine a number of metrics from the collection of de-identified voting results, which included nothing more than the ballot ID, county of origin, and the candidate selected for each vote cast across three counties within a CSV file.  The necessary metrics included the following: voter turnout per county, percentage of votes from each county out of the total count, and the county with the highest turnout.

#### Election-Audit Results

![Figure 1: Summary of election outcomes as viewed within the command line.](https://github.com/bdeorosan/election_analysis/blob/main/Resources/election_results.png)
<p align="center">
Figure 1: Summary of election outcomes as viewed within the command line.
</p>

##### * How many votes were cast in this congressional election?
The script revealed that the total number of votes cast within the election was 369,711.

##### * Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
The script also revealed the total number of votes cast within each county, as well as the percentage of the total votes cast that the counties’ vote totals represented.  Jefferson county cast 38,855 votes, representing 10.5% of the total votes cast.  Denver county cast 306,055 votes, representing 82.8% of the total votes cast.  Lastly, Arapahoe county cast 24,801 votes, representing 6.7% of the total votes cast.

##### * Which county had the largest number of votes?
The analysis revealed that Denver county cast the largest number of votes at 38,855, representing 82.8% of the votes cast.

##### * Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
The script was also used to find the total number of votes cast for each candidate, as well as the percentage of the total votes cast that the candidates’ vote totals represented.  Charles Casper Stockham received 85,213 votes, representing 23% of the total votes cast.  Diana DeGette received 272,892 votes, representing 73.8% of the total votes cast.  Raymon Anthony Doane received 11,606 votes, representing 3.1% of the total votes cast.

##### * Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
The winner of the election was candidate Diana DeGette, who earned 73.8% of the total vote at 272,892 votes cast.

#### Election-Audit Summary

The Python script used for this analysis should not be thought of singularly useful for this particular election.  In theory, with the way that it has been constructed, an election composed of any number of counties and any number of candidates could be analyzed using the exact same script.  That is because none of the code has been composed with a specific number of either counties or candidates in mind at any step in the process.  As a matter of fact, the code has been specifically composed to determine the number of both counties and candidates at the start, collect them all within a list, and then attach appropriate vote metrics to each.  

Should the code be modified for use in other elections, one assumption is key: the election must be of a “traditional” democratic format, in which a single candidate gets a single vote per voter.  With that being said, it could potentially be used for city elections, in which county names could be replaced with neighborhoods, wards, or districts as appropriate.  On the other hand, this script would not be appropriate for “ranked choice” voting, as it would not account for a voter being able to select more than one candidate for the same position.  The script would need to be modified to for this, especially in terms of the “weight” given to each vote receiver, as first choice, second choice, etc.  
