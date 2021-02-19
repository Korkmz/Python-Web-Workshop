from flask import Flask,render_template
import requests

app=Flask(__name__)

@app.route("/")
def home():
    url="--"
    result=requests.get(url)
    json= result.json()
    print("hava")
    print(json['weather'][0]['main'])
    print(result.json())
    return render_template("index.html")

if __name__ =="__main__":
    app.run(debug=True)