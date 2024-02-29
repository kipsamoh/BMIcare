from flask import Blueprint, render_template, request

bmi_calculator_blueprint = Blueprint('bmi_calculator', __name__)

@bmi_calculator_blueprint.route('/')
def index():
    return render_template('index.html')

@bmi_calculator_blueprint.route('/calculate_bmi', methods=['POST'])
def calculate_bmi():
    # Extracting height and weight from the form
    height = float(request.form['height'])
    weight = float(request.form['weight'])

    # Calculating BMI
    bmi = weight / ((height / 100) ** 2)

    # Determining recommendation based on BMI
    if bmi < 18.5:
        recommendation = "You are underweight. You should consider gaining some weight."
    elif bmi >= 18.5 and bmi < 24.9:
        recommendation = "Your weight is normal. Keep up the good work!"
    elif bmi >= 25 and bmi < 29.9:
        recommendation = "You are overweight. You should consider losing some weight."
    else:
        recommendation = "You are obese. It's important to prioritize weight loss for your health."

    # Rendering the result template with BMI value and recommendation
    return render_template('result.html', bmi=bmi, recommendation=recommendation)

