import csv
import numpy as np
import matplotlib.pyplot as plt

categories = [] # strip out first row of text
installs = [] # push the installs data here
ratings = [] # push the ratings data here

# open the csv file and parse it
with open("data/googeplaystore.csv") as csvfile:
		reader = csv.reader(csvfile)
		line_count = 0

		for row in reader:
			if line_count is 0: # strip the headers out
				print("pushing text row to categories array")
				categories.append(row)
				line_count += 1
			else:
				# collect the ratings info
				ratings.append(row[2]);
				ratingsData = ratingsData.replace("Nan", "0")
				ratings.append(float(ratingsData))


				installData = (row[5])
				installData = installData.replace(",", "")
				installData = installData.replace("Free", "0")
				installs.append(int(np.char.strip(installData, "+")))
				line_count += 1

print("processed", line_count,"rows of data")
print("first line:", ratings[0])
print("last line:", ratings[-1])
