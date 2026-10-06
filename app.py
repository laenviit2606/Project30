import csv
from pathlib import Path
from flask import Flask, render_template, request
from Main import find_language #Reuses search function from Main.py

app = Flask(__name__) #Creates web application

data_path = Path(__file__).parent / "Dataset" / "AUSTLANG.csv" 
#Finds the folder containing app.py => CSV path doesn't depend on terminal's location

with data_path.open(encoding="utf-8-sig", newline="") as file:
    records = list(csv.DictReader(file))

@app.route("/") #Connects the website's home address to the home().
def home():
    search_text = request.args.get("q", "").strip()
    result = None
    message = ""

    if "q" in request.args: #Distinguishes a submitted search form the 1st visit
        if search_text == "":
            message = "Please enter a language code or name."
        else:
            result = find_language(records, search_text) #Searches loaded records

            if result is None:
                message = "No matching language found. Please try again."
    #Find the starting letters available in the dataset
    available_letters = set() #A set stores uniques values. If 100 names with "A", we only need one "A" button

    for record in records:
        name = record["language_name"].strip()

        if name: #Skip empty names
            available_letters.add(name[0].upper()) #name[0]: takes the first character - .add(): puts into the set
    letters = sorted(available_letters) #Turn the set into a sorted list - ["A", "B". "C"]
    
    #Determine which letter the visitor selected
    #Use the selected letter, or the first available letter
    default_letter = letters[0] if letters else "" #If there are no letters, use an empty string
    
    selected_letter = request.args.get("letter", default_letter).upper()

    if selected_letter not in available_letters: 
        selected_letter = default_letter
    #Hadnles invalid value in the URL - by return the default group

    #Collect records beginning with the selected letter
    matching_records = []
    #Creates an empty list to hold the matching records.
    for record in records:
        name = record["language_name"].strip()

        if name and name[0].upper() == selected_letter:
            matching_records.append(record)
    #For each record, Python checks - Does its name exist - Does it start with the selected letter
    #If yes ".append(record)" => adds the whole record to the list

    #Sort the selected records by name, then code
    matching_records = sorted(
        matching_records,
        key=lambda record: (
            record["language_name"].strip().casefold(),
            record["language_code"]
        )
    )
    #sorted(): creates an ordered list - key: tells it what to sort by (Name/ Code)
    #lambda record: short function - supplies sorting value for each record
    #Case-fold: makes the name comparison case-insensitive - avoids separating names because of capitalisation

    #Show 20 records per page
    page_size = 20
    total_matches = len(matching_records)
    total_pages = max(1, (total_matches + page_size -1) // page_size) #Show 20 records at a time and count how many records mnatch the letter
    #"//": performs whole-number division => Keeps the page count at least one, including when the dataset is empty

    page = request.args.get("page", default=1, type=int) #Reads the page number from the URL and converts -> integer
    page = max(1, min(page, total_pages)) #Keep the number in the valid range

    start = (page -1) * page_size
    browse_records = matching_records[start:start + page_size]
    
    return render_template( #Fills the HTML template with the result and feedback
        "index.html",
        result=result,
        message=message,
        search_text=search_text,
        total_records=len(records),
        letters=letters,
        selected_letter=selected_letter,
        browse_records=browse_records,
        total_matches=total_matches,
        page=page,
        total_pages=total_pages
    )

@app.route("/insights")
def insights():
    total_records = len(records)
    records_with_alternatives = 0

    for record in records:
        alternatives = record["language_synonym"].strip()

        if alternatives: 
            records_with_alternatives += 1
    records_without_alternatives = total_records - records_with_alternatives

    if total_records > 0:
        percentage = records_with_alternatives / total_records * 100
    else:
        percentage = 0
    return render_template (
        "insights.html",
        total_records=total_records,
        with_alternatives=records_with_alternatives,
        without_alternatives=records_without_alternatives,
        percentage=round(percentage, 1)
    )
@app.route("/about")
def about():
    return render_template("about.html")
if __name__ == "__main__":
    app.run(port=5001) #Start a local development server on port 5001. Access the website at http://localhost:5001
