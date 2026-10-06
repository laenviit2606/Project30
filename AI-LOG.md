30/9 - Searching by language code and begin the project
    AI tool: ChatGPT/Codex
    Asked: How to search the CSV using a language code and correctly indent the result-display code
    Help used: input()/ loop/ if/ break
30/09 - Repeat language-code prompt until a match is found.
    Problem: The loop end when enter wrong answer
    Asked: Why my loop end when I entered wrong answer, where I should look at in my code. Also create a loop to ask customer to "Enter a valid code" when wrong received wrong answer
    Help: while True:/ continue/ break/ if - else
03/10 - Searching names and alternative names
    Help used: guidance on seaarching by code/ exact language name. and alternative names using a function
    What I learned: ".split" to separates alternative names into a list => return ends and function and sends back its result
03/10 - First automated search test
    Help used: Guidance on organising the terminal program inside main(), using the "name" check, and creat a unittest for searching by code
    Problem: wrong spelling 
    Fix: double check the spelling 
    What I learned: An automated test runs my function with known input and checks its output. Dictionary kets mnust match exactly.
03/10 - Added exact-name and second-alternative-name tests with AI guidance. Ran all 3 test successful
03/10 - 8 Tests passed
    Help used: guidance on adding tests for search behaviour, invalid input, and edge case
03/10 - AI guidance to create an HTML search form
    Help used: preview the web successfully 
04/10 - Connect the website to Python
    Help used: installing Flask, creating app.py/ import find_language from Main.py/ display search results in an HTML template
    What I learned: Form sends "the search" using a parameter named q. Flask reads it => pass result to index.html. Each form submission sends - new request => website doesn't need terminal input loop
04/10 - Website views, statistics, and styling
    Help used; Guidance on adding Search, insights/ About/ navigation links/ alternative-name statistics/ shared CSS stylesheet
    What I learned: Flask routes connect URLs to Python functions. Python passed calculated values to HTML templates. 
04/10 - Add 6 website tests 
    Help used: Guidance for website tests
05/10 - README and ARCHITECTURE documentation
    Help received: Draft installation, usage, testing, data-source, limitation sections. Flask ended, search function, CSV, and HTML templates connect
    What I learned: The README explains how to use and run the project + The architecture provides a diagram explains how its components interact
06/10 - Alphebetical browsing and pagination
    My request: Improve the homepage so visiotrs can explore records without already knowing a language name or code.
    Help received: Example Python/ HTML/ CSS for an introduction + starting letter links, alphabetical record lists/ pagination/ clickable records/ Also explained how the code works
    Design decision: keep exact-match search + add browsing bhy the 1st character of each language name, displayin 20 records per page.
    What I learned: a set collects unique starting characters - Python filters/ sorts records - HTML template loops display links and rows, while CSS styles them