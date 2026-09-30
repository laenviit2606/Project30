import csv

with open("Dataset/AUSTLANG.csv", encoding="utf-8-sig", newline="") as file: 
    #encoding "utf-8-sig": This will reads the text and handle the special invisible marker at the start of CSV
    #newline: for CSV reader handle line endings correctly
    reader = csv.DictReader(file) #Read each row as a dictionary - using column headings as keys
    records = list(reader) #Collects rows into a list called records

print ("Number of records:", len(records)) #Counts the records
print("First language:", records [0]["language_name"]) #records[0] - get the first record position start at zero