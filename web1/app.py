from flask import Flask,render_template

app = Flask(__name__) #khoi tao

@app.route("/") #router
def home(): #view funtion
    c = {
        "name":"AQUAMAN",
        "company":"DC COMICS",
        "image":"https://znews-photo.zadn.vn/w860/Uploaded/spuocaw/2018_12_21/aquaman12801543622354275_960w.jpg",
        "abilities":["Speed","Streght","Reflexes","Underwater","Telepathy"]
    }
    
    return render_template("home.html",
                            character=c)  #serve html



@app.route("/c4e") 
def c4e():
    return "code for everyone 24"
@app.route("/hi/<name>")
def say_hi(name):
    print(name)
    return "Hi" + name
@app.route("/add/<int:x>/<int:y>")
def add(x,y):
    s = x+y
    return str(s)



if __name__ == "__main__":
    app.run(debug=True)