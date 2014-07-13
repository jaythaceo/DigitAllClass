#!/usr/bin

import csv

f = open("Arrest.csv")
r= csv.DictReader(f,['arrest','age','sex','race','arrestdate','arresttime','location'])
for a in r:
    print("{arrest} {age} {sex} {race} {arrestdate} {arresttime} {location}".format(**a))


