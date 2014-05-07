
#!/usr/bin

import csv

f = open("Dial.csv", "r")
for r in csv.reader(f):
    name, zipcode, neighborhood, councilDistrict, policeDistrict, location = r
    print("{0} {1} {2} {3} {4} {5}".format(*r))
    
    

