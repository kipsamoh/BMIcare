from flask import Flask, render_template
from bmi_calculator import calculate_bmi_value, get_bmi_category

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

