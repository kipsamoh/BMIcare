from flask import request, render_template
from app import app

@app.route('/calculate_bmi', methods=['POST'])
def calculate_bmi():
    height = float(request.form['height'])
    weight = float(request.form['weight'])
    bmi = calculate_bmi_value(height, weight)
    category = get_bmi_category(bmi)
    return render_template('result.html', bmi=bmi, category=category)

def calculate_bmi_value(height, weight):
    return round(weight / ((height / 100) ** 2), 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

