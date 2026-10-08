# Application architecture

```mermaid
flowchart TD
    CSV["Dataset/AUSTLANG.csv"] --> APP["app.py: Flask backend"]
    USER["Browser"] --> APP
    APP --> SEARCH["Main.py: find_language"]
    SEARCH --> APP
    APP --> BROWSE["Filter, sort and paginate"]
    BROWSE --> APP
    APP --> STATS["Calculate statistics"]
    STATS --> APP
    APP --> HTML["HTML templates"]
    HTML --> USER
    CSS["static/style.css"] --> USER
```

## Components
- Browser displays the pages and submits searches
- Flask handles requests and loads the CSV into memory
- "find_language" searches records by - code/name/alternative name
- Insight route calculates alternative-name coverage
- HTML templates displat the supplied values
- 1 CSS file provides consistent styling

## Search algorith
1. Trim the query + convert into uppercase.
2. Return "None" if the query is blank
3. Examine each record in CSV order
4. Compare - code and main name with the query
5. Split alternative names + compare each one
6. Return the 1st matching record
7. Return "None" after all records have been checked "without a match"

- This is linear search. A query without a match examines every record + its alternative names.
- The function does not prioritise matches across the whole dataset: an earlier match can returned before a later name is match

## Data handling
The application reads the CSV without modifying it. Prepared records are held in memory.
The browser receives rendered results rather than direct access to the Python files. 