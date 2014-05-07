#!/usr/bin

import csv

grab = open("cctv.csv", "r")

for r in csv.reader(grab):
    cameraLocation, cameraNumber, cameraProject, Location = r
    print(r)
    
