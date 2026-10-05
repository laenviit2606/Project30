import csv

def find_language(records, search_text): #Define a function with 2 inputs - records + the code to find
    search_text = search_text.strip().upper()

    if search_text == "":
        return None

    for record in records: #Check if record
        language_code = record["language_code"].strip().upper()
        language_name = record["language_name"].strip().upper()
        alternative_names = record["language_synonym"].split("|") #Add alternative names = variable
        #Split turns a string into a list => ["Name A", "Name B", Name C"]

        if language_code == search_text or language_name == search_text: #Check if the code/name matches the search text
            return record #Send matching dictionary back and immediately ends the function
        for alternative in alternative_names:
            if alternative.strip().upper() == search_text:
                return record
            
    return None #runs after the loop if no match was found
    
#Load the CSV File
def main():
    with open("Dataset/AUSTLANG.csv", encoding="utf-8-sig", newline="") as file: 
        #encoding "utf-8-sig": This will reads the text and handle the special invisible marker at the start of CSV
        #newline: for CSV reader handle line endings correctly
        reader = csv.DictReader(file) #Read each row as a dictionary - using column headings as keys
        records = list(reader) #Collects rows into a list called records

    print("Number of records:", len(records)) #Counts the records

#print("First language:", records [0]["language_name"]) #records[0] - get the first record position start at zero
    valid_code = True
    while valid_code:
        #Find language by its code
        search_text = input("Enter a language code or name: ").strip() #.strip: remove spaces from the beginning and end
        if search_text == "":
            print ("Please enter a language code or name.")
        else:
            found_record = find_language(records, search_text)
            
            #Display the result
            if found_record:
                print("Language code:", found_record["language_code"])
                print("Language name:", found_record["language_name"])

                source_url = found_record["uri"].strip() #uri: gets the source link from the matching CSV record
                if source_url: 
                    print("Original source:", source_url)
                else:
                    print("No source link available.")

                #Stop asking after a successful search
                valid_code=False
            else:
                print("No matching language found. Please enter a valid code.")
if __name__ == "__main__":
    main()