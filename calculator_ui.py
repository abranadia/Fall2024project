import tkinter as tk
from calculator_logic import *

def calculate(operation):
    try:
        input_data = input_text.get("1.0", "end").strip()
        if operation == "mean":
            values = list(map(float, filter(None, input_data.splitlines())))
            result = compute_mean(values)
        elif operation == "sample_std_dev":
            values = list(map(float, filter(None, input_data.splitlines())))
            result = compute_sample_std_dev(values)
        elif operation == "population_std_dev":
            values = list(map(float, filter(None, input_data.splitlines())))
            result = compute_population_std_dev(values)
        elif operation == "z_score":
            value, mean, std_dev = map(float, input_data.split(","))
            result = compute_z_score(value, mean, std_dev)
        elif operation == "linear_regression":
            pairs = [tuple(map(float, line.split(","))) for line in filter(None, input_data.splitlines())]
            slope, intercept = compute_linear_regression(pairs)
            result = f"{slope}, {intercept}"
        elif operation == "predict_y":
            x, slope, intercept = map(float, input_data.split(","))
            result = predict_y(x, slope, intercept)
        else:
            result = "Invalid operation!"
        result_text.delete("1.0", "end")
        result_text.insert("1.0", result)
    except Exception as e:
        result_text.delete("1.0", "end")
        result_text.insert("1.0", f"Error: {e}")

# Setting up the UI
app = tk.Tk()
app.title("Calculator")

input_label = tk.Label(app, text="Input:")
input_label.pack()

input_text = tk.Text(app, height=10, width=50)
input_text.pack()

button_frame = tk.Frame(app)
button_frame.pack()

operations = [
    ("Compute Mean", "mean"),
    ("Sample Std Dev", "sample_std_dev"),
    ("Population Std Dev", "population_std_dev"),
    ("Compute Z-Score", "z_score"),
    ("Linear Regression", "linear_regression"),
    ("Predict Y", "predict_y"),
]

for label, operation in operations:
    tk.Button(button_frame, text=label, command=lambda op=operation: calculate(op)).pack(side="left")

result_label = tk.Label(app, text="Result:")
result_label.pack()

result_text = tk.Text(app, height=5, width=50)
result_text.pack()

tk.Button(app, text="Clear", command=lambda: [input_text.delete("1.0", "end"), result_text.delete("1.0", "end")]).pack()

app.mainloop()
