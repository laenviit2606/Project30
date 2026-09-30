import csv

with open("Dataset/AUSTLANG.csv", encoding="utf-8-sig", newline="") as file: 
    #encoding "utf-8-sig": This will reads the text and handle the special invisible marker at the start of CSV
    #newline: for CSV reader handle line endings correctly
    reader = csv.DictReader(file) #Read each row as a dictionary - using column headings as keys
    records = list(reader) #Collects rows into a list called records

print ("Number of records:", len(records)) #Counts the records
print("First language:", records [0]["language_name"]) #records[0] - get the first record position start at zero
while True:
#Find language by its code
    search_code = input("Enter a language code: ").strip().upper() 
    #.strip: remove spaces from the beginning and end
    #.upper: converts letters to uppercase - exp: y75 -> Y75
    if search_code == "":
        print ("Please enter a language code.")
    else:
        found_record = None #Create a variable => hold the result
        for record in records:
            if record["language_code"].strip().upper() == search_code: #get the record's code => "==" Checks whether the 2 codes match
                found_record = record #Saves the matching dictionary
                break #Stop searching once a match is found
        #Display the result
        if found_record is not None:
            print("Language code:", found_record["language_code"])
            print("Language name:", found_record["language_name"])
            break
        else:
            print("No matching language found. Please enter a valid code.")