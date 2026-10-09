import csv

#creates the csv file and assigns the headers to the first row
header = ["Team", "wins", "draws", "losses", "date"]
file = open("leaderboard.csv", "a", newline = "")
db = csv.writer(file)
db.writerow(header)
file.close()

#This code fills data into the csv file
record1 = ["Limerick", "5", "2", "4", "2/2/75"]
record2 = ["Cork", "3", "4", "3","4/7/59"]
record3 = ["Dublin", "4", "0", "2","3/6/03"]
file = open("leaderboard.csv", "a", newline="")

db = csv.writer(file)
db.writerow(record1)
db.writerow(record2)
db.writerow(record3)

file.close()

file = open("leaderboard.csv", "r")
records = list(csv.reader(file))
file.close()
#print(records)

#prints everything in new lines
for record in records[1:]: #controls row of data
    print(record[3]) #controls column being accessed