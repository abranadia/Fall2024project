# Fall2024project
Calculator Project
I created this project using Python. Basically it a calculator with a graphical user interface (GUI) built using Tkinter. It performs basic statistical calculations, including standard deviation, mean, z-scores, and linear regression.

Features 
Sample Standard Deviation: Calculates standard deviation for a sample dataset.
Population Standard Deviation: Calculates standard deviation for a population dataset.
Mean: Computes the average of a dataset.
Z-Score: Computes the z-score using a value, mean, and standard deviation.
Linear Regression Formula: Derives the slope (m) and intercept (b) from X, Y pairs.
Predict Y: Predicts a Y value using the regression formula.

The Installation needed for the project: 

Clone the Repository:
Type code
git clone <repository-url>
cd Calculator_Project

Install Required Libraries:
Type code
pip install -r requirements.txt

Install Playwright (For UI Tests):

Type code
pip install playwright
playwright install

To Run the Calculator:
Type code
python calculator_ui.py

To Run the Unit Tests
To test the calculator logic:
Type code
python -m unittest discover -s tests
Run UI Tests
Ensure the calculator is running, then:

Type code
pytest tests/test_ui.py

My Folder Structure

Calculator_Project (folder)
│
├── calculator.py    # Contains the core calculation logic
├── calculator_ui.py  # Main UI file for the calculator
│
├── tests (folder)               # Contains unit and UI tests
│   ├── test_calculator_logic.py
│   ├── test_ui.py
│
├── README.md              # Contains project documentation

Project Requirements
Python 3.8+
Tkinter (pre-installed with Python)
Playwright (for UI testing)

Project Usage
Open the calculator, input the required values, and click the relevant button to calculate results.
The test is not working but i tried my best with giving it a try 
