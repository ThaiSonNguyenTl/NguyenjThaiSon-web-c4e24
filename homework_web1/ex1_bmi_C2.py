from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def home():
    return " "
@app.route("/bmi/<int:weight>/<int:height>")
def calcul_BMI(weight,height):
    h = height / 100
    BMI = weight/(h*h)
    bmi_dict = {
        "lv1" : "Severely underweight", 
        "lv2":  "Underweight",
        "lv3":  "Normal",
        "lv4":  "Overweight",
        "lv5":  "Obese"
    }
    
    return render_template("bmi.html",bmi_dict = bmi_dict,BMI =BMI)

if __name__ == '__main__':
  app.run(debug=True)