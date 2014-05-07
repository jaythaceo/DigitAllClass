#!/usr/bin
import csv
grab = open("Arrest.csv", "r")

row = list(grab)
total = len(row)

for i, row in enumerate(row):
    print("Row %d/%d" % (i+1, total))