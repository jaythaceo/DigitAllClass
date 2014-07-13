#!/usr/bin

import csv

grab = open("cctv.csv", "r")

for r in csv.reader(grab):
    cameraNumber, cameraProject, Location = r
    print(r)

