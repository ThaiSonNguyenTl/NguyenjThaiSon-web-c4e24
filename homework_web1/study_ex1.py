from flask import Flask,render_template,redirect
app = Flask(__name__)

@app.route("/")
def home():
    return "well come to techkid"

@app.route("/about-me")
def infor_yoursef():
  information = {
    "NAME": "NguyenSon",
    "WORK": "student",
    "SCHOOL": "Hanoi Polytechnic University",
    "HOBBIES": "kungfu",
    "YOURCRUSH": "no"
  }
  return render_template("study.html",
                           information=information)


@app.route("/school")
def schooltechkid():
  return redirect("http://techkids.vn")

if __name__ == '__main__':
  app.run(debug=True)