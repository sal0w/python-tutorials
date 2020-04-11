"""
Write a program to read the csv file and store in a specific data structure
"""
with open("test.csv") as f:
    for line in f:
        print(line.split(","))