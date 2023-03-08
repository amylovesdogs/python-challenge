import csv
import os
import os.path

my_dir = os.getcwd()
data_file = os.path.join(my_dir, "Resources/election_data.csv")
print(data_file)

with open(data_file, encoding='utf') as csvfile:
   csvreader = csv.reader(csvfile, delimiter=',')
   print(csvreader)
    
   for row in csvreader:
       print(row)
