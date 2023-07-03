import csv
import collections
from collections import Counter

csvpath = "H:/Training/DU Boot Camp/Module 3 Challenge Assignment 07052023/PyPoll/Resources/election_data.csv"

voters_candidates = []
votes_per_candidate = []

with open(csvpath, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    for row in csv_reader:
        voters_candidates.append(row[2])

    # Sort the list by ascending order
    sorted_list = sorted(voters_candidates)

    # Arrange the sorted list by most common outcomes
    arrange_list = sorted_list

    #count votes per candidate in most common outcome order
    count_candidate = Counter (arrange_list)
    votes_per_candidate.append(count_candidate.most_common())

    # calculate percentage of votes per candicate in 3 digital points
    for item in votes_per_candidate:

        first = format((item[0][1])*100/(sum(count_candidate.values())),'.3f')
        second = format((item[1][1])*100/(sum(count_candidate.values())),'.3f')
        third = format((item[2][1])*100/(sum(count_candidate.values())),'.3f')
        fourth = format((item[2][1])*100/(sum(count_candidate.values())),'.3f')


#Analysis
print("Election Results")
print("-------------------------")
print(f"Total Votes:  {sum(count_candidate.values())}")
print("-------------------------")
print(f"{votes_per_candidate[0][0][0]}: {first}% ({votes_per_candidate[0][0][1]})")
print(f"{votes_per_candidate[0][1][0]}: {second}% ({votes_per_candidate[0][1][1]})")
print(f"{votes_per_candidate[0][2][0]}: {third}% ({votes_per_candidate[0][2][1]})")
print(f"{votes_per_candidate[0][2][0]}: {fourth}% ({votes_per_candidate[0][2][1]})")
print("-------------------------")
print(f"Winner:  {votes_per_candidate[0][0][0]}")
print("-------------------------")
