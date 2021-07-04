import csv
import os


file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    headers = next(file_reader)
    print(headers)

"""
    for row in file_reader:
        print(row)
"""
'''

with open(file_to_save, "w") as txt_file:
    txt_file.write("Counties in the election:\n")
    txt_file.write("_________________________\n")
    txt_file.write("Arapahoe\n")
    txt_file.write("Denver\n")
    txt_file.write("Jefferson")
'''
