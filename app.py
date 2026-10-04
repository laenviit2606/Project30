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

    return render_template( #Fills the HTML template with the result and feedback
        "index.html",
        result=result,
        message=message,
        search_text=search_text
    )

if __name__ == "__main__":
    app.run(port=5001) #Start a local development server on port 5001. Access the website at http://localhost:5001