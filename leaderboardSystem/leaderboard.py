import csv

#creates the csv file and assigns the headers to the first row
#header = ["firstName", "lastName", "phoneNum", "dob", "age"]
#file = open("patients.csv", "a", newline = "")
#db = csv.writer(file)
#db.writerow(header)
#file.close()

#This code fills data into the csv file
#record1 = ["Joan", "Byrne", "0981 45877", "2/2/75", "45"]
#record2 = ["Gideon", "Jones", "0983 76800", "4/7/59", "61"]
#record3 = ["Noor", "Patel", "0983 54689", "3/6/03", "17"]

#file = open("patients.csv", "a", newline="")

#db = csv.writer(file)
#db.writerow(record1)
#db.writerow(record2)
#db.writerow(record3)

#file.close()

file = open("patients.csv", "r")
records = list(csv.reader(file))
file.close()
#print(records)

#prints everything in new lines
for record in records[1:]: #controls row of data
    print(record[3]) #controls column being accessed