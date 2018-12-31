from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def home():
  return " "

@app.route("/user/<username>")
def infor(username):
    Users = {
        "huy" :{
                "name" : "Nguyen Quang Huy",
                "age" : 29,
                "gender": "nam",
                "hobbies":"code"
                },
        "tuananh" :{
                "name" : "Huynh Tuan Anh",
                "age" : 22,
                "gender": "nam",
                "hobbies": "Music"
        }
    }
    return render_template("infor.html",Users = Users,username = username)



if __name__ == '__main__':
  app.run(debug=True)