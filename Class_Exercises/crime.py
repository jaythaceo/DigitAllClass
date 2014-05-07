#!/usr/bin

import csv

grab = open("Arrest.csv", "r")

#for r in csv.reader(grab):
 #  arrest, age, sex, race, arrestDate, arrestTime, arrestLocation, incidentOffense,incidentLocation, charge, chargeDescription, district, post, neighborhood, Location = r
  # print("{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14}".format(*r))

row = list(grab)
total = len(row)

for i, row in enumerate(row):
    print("Row %d/%d" % (i+1, total))
    