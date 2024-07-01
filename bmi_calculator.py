from flask import Blueprint, render_template, request

bmi_calculator_blueprint = Blueprint('bmi_calculator', __name__)

# Route for the BMI Calculator page
@bmi_calculator_blueprint.route('/')
def index():
    return render_template('index.html')

# Route to handle BMI calculation
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

# Route for the About page
@bmi_calculator_blueprint.route('/about')
def about():
    return render_template('about.html')

# Route for the Blog page
@bmi_calculator_blueprint.route('/blog')
def blog():
    # Assuming you have a list of blog posts to pass to the template
    blog_posts = [
        {'title': 'First Blog Post', 'content': 'Lorem ipsum dolor sit amet...'},
        {'title': 'Second Blog Post', 'content': 'Consectetur adipiscing elit...'},
        {'title': 'Third Blog Post', 'content': 'Sed do eiusmod tempor incididunt...'}
    ]
    return render_template('blog.html', blog_posts=blog_posts)

# Route for the Contact Us page
@bmi_calculator_blueprint.route('/contact')
def contact():
    return render_template('contact.html')
