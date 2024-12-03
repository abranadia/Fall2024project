# app.py

from flask import Flask, render_template, request, jsonify
from calculator_logic import CalculatorLogic

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compute', methods=['POST'])
def compute():
    operation = request.form.get('operation')
    values = [float(val) for val in request.form.get('values').splitlines() if val.strip()]
    
    try:
        if operation == 'mean':
            result = CalculatorLogic.compute_mean(values)
        elif operation == 'sample_std_dev':
            result = CalculatorLogic.compute_sample_std_dev(values)
        elif operation == 'population_std_dev':
            result = CalculatorLogic.compute_population_std_dev(values)
        elif operation == 'z_score':
            value, mean, std_dev = values
            result = CalculatorLogic.compute_z_score(value, mean, std_dev)
        elif operation == 'regression':
            x_values = [float(val.split(',')[0]) for val in values]
            y_values = [float(val.split(',')[1]) for val in values]
            m, b = CalculatorLogic.compute_regression(x_values, y_values)
            result = f"y = {m}x + {b}"
        elif operation == 'predict':
            x, m, b = values
            result = CalculatorLogic.predict_y(x, m, b)
        else:
            raise ValueError("Invalid operation")
    except Exception as e:
        result = str(e)
    
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
