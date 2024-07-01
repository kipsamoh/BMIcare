from flask import Flask, render_template, request
from bmi_calculator import bmi_calculator_blueprint

app = Flask(__name__)
app.register_blueprint(bmi_calculator_blueprint)

# Importing the necessary function from bmi_calculator module
from bmi_calculator import calculate_bmi

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
