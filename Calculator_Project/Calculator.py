import tkinter as tk
import math
from statistics import mean, stdev, pstdev

# Define the Calculator class
class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Calculator")

        # Create a text entry widget for displaying the calculation result
        self.result_var = tk.StringVar()
        self.result_var.set("0")
        self.result_display = tk.Entry(root, textvariable=self.result_var, font=("Arial", 24), bd=10, relief="sunken", justify="right")
        self.result_display.grid(row=0, column=0, columnspan=4)

        # Create buttons for digits and operations
        self.create_buttons()

    def create_buttons(self):
        # Button layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('Mean', 5, 0), ('Stdev (Sample)', 5, 1), ('Stdev (Population)', 5, 2), ('Z-Score', 5, 3),
            ('Regression', 6, 0), ('Predict Y', 6, 1)
        ]
        
        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, width=10, height=2, font=("Arial", 14), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col)

        # Clear button
        clear_button = tk.Button(self.root, text="C", width=5, height=2, font=("Arial", 18), command=self.clear)
        clear_button.grid(row=7, column=0, columnspan=4)

    def on_button_click(self, text):
        current_text = self.result_var.get()

        if text == "=":
            try:
                # Evaluate the expression and show result
                result = str(eval(current_text))
                self.result_var.set(result)
            except Exception:
                self.result_var.set("Error")
        elif text == "Mean":
            self.compute_mean()
        elif text == "Stdev (Sample)":
            self.compute_stdev(sample=True)
        elif text == "Stdev (Population)":
            self.compute_stdev(sample=False)
        elif text == "Z-Score":
            self.compute_z_score()
        elif text == "Regression":
            self.compute_regression()
        elif text == "Predict Y":
            self.predict_y()
        else:
            if current_text == "0" or current_text == "Error":
                self.result_var.set(text)
            else:
                self.result_var.set(current_text + text)

    def clear(self):
        self.result_var.set("0")

    # Compute mean from a list of numbers
    def compute_mean(self):
        try:
            numbers = self.get_numbers_from_input()
            result = mean(numbers)
            self.result_var.set(f"Mean: {result}")
        except Exception:
            self.result_var.set("Error")

    # Compute standard deviation (sample or population)
    def compute_stdev(self, sample=True):
        try:
            numbers = self.get_numbers_from_input()
            if sample:
                result = stdev(numbers)
            else:
                result = pstdev(numbers)
            self.result_var.set(f"Stdev: {result}")
        except Exception:
            self.result_var.set("Error")

    # Compute Z-score from a value, mean, and standard deviation
    def compute_z_score(self):
        try:
            value = float(self.result_var.get())
            mean_val = float(input("Enter mean: "))
            stdev_val = float(input("Enter standard deviation: "))
            result = (value - mean_val) / stdev_val
            self.result_var.set(f"Z-Score: {result}")
        except Exception:
            self.result_var.set("Error")

    # Compute linear regression (y = mx + b)
    def compute_regression(self):
        try:
            pairs = self.result_var.get().strip().split('\n')
            x_vals = []
            y_vals = []
            for pair in pairs:
                x, y = pair.split(',')
                x_vals.append(float(x))
                y_vals.append(float(y))

            # Compute the slope (m) and intercept (b)
            n = len(x_vals)
            m = (n * sum(x * y for x, y in zip(x_vals, y_vals)) - sum(x_vals) * sum(y_vals)) / (n * sum(x ** 2 for x in x_vals) - sum(x_vals) ** 2)
            b = (sum(y_vals) - m * sum(x_vals)) / n

            result = f"y = {m}x + {b}"
            self.result_var.set(result)
        except Exception:
            self.result_var.set("Error")

    # Predict Y from x using regression formula
    def predict_y(self):
        try:
            x_value = float(input("Enter X value: "))
            m = float(input("Enter slope (m): "))
            b = float(input("Enter intercept (b): "))
            y = m * x_value + b
            self.result_var.set(f"Predicted Y: {y}")
        except Exception:
            self.result_var.set("Error")

    def get_numbers_from_input(self):
        # Get numbers from current input string
        input_text = self.result_var.get().strip()
        return list(map(float, input_text.split(',')))

# Create the main window
root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
