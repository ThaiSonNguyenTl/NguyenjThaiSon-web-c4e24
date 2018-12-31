from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def home():
    return " CALCULATE BMI "


@app.route("/bmi/<int:weight>/<int:height>")
def calculate_bmi(weight,height):
    h = height / 100
    BMI = weight/(h*h)
    if BMI < 16:
        return " Severely underweight "
    elif BMI < 18.5:
        return "Underweight"
    elif BMI < 25:
       return "Normal"
    elif BMI < 30:
        return "Overweight"
    else:
        return "Obese"
    
if __name__ == '__main__':
  app.run(debug=True)