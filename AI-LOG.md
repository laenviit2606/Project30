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
