# Python Calculator Web Application

This project is a web-based calculator that performs statistical calculations using Flask. It includes various operations like computing mean, standard deviation, z-score, regression formula, and more.

## Features

- **Compute Mean**: Calculate the average of a list of numbers.
- **Compute Sample Standard Deviation**: Compute sample standard deviation.
- **Compute Population Standard Deviation**: Compute population standard deviation.
- **Compute Z Score**: Calculate z-score for a given value, mean, and standard deviation.
- **Compute Regression Formula**: Calculate the linear regression formula (y = mx + b) from x,y pairs.
- **Predict Y**: Predict y value using the regression formula.

## Requirements

- Python 3.7 or newer
- Flask
- Playwright for end-to-end testing 

How to run the code in the terminal : 
 App
 Paste: python app.py in the terminal with the app.py file open

Unit tests 
paste: pytest tests/test_calculator_logic.py in the terminal with the test_calculator_logic.py file open

The unit test failed to run successfully. I spent most of my time trying to fix it, but it still won't run.

End-to-end tests
Paste: pytest tests/test_playwright.py in the terminal with test_playwright.py file open

Project Architecture: 

calculator-project/
├── app.py                  # Flask application (Controller)
├── calculator_logic.py     # Calculator logic (Domain Logic)
├── templates/              # HTML templates for the web interface (View)
│   └── index.html          # Main HTML page
├── tests/                  # Testing folder
│   ├── test_calculator.py  # Unit tests for calculator logic
│   └── test_playwright.py # End-to-end tests for the web interface
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation

Final presentation 
https://www.loom.com/share/544bed1561fe4a8eb8d4ef3ca7e97ede?sid=d1a261d3-9bfa-413b-a855-241f05636c44


