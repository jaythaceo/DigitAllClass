#!/usr/bin

import csv

grab = open("cctv.csv", "rb")
text = csv.reader(grab)

rownum = 0
for row in text:
	if rownum == 0:
		header = row
	else:
		column = 0
		for col in row:
			print '%-8s: %s' % (header[column],col)
			column += 1
	rownum += 1

grab.close()
