import csv
with open("SentiWords_1.1.csv") as csv_file:
	reader=csv.reader(csv_file)
	next(reader)
	for row in reader:
		if( len(row)<3):
			print(row)
		