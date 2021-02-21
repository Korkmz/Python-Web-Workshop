from flask import Flask,render_template,request ,jsonify
from datetime import datetime
import requests

app=Flask(__name__)

@app.route("/")
def home():
      return render_template("index.html")
   
      

@app.route("/save/",methods=["POST"])
def save():
    if request.method=="POST":
        print("successsss")
        searchText= request.form["data"]
        
        url="http://api.openweathermap.org/data/2.5/weather?q="+searchText+"&appid="
        result=requests.get(url)
        json =result.json()
        result=requests.get(url)
        

        return jsonify(
            cityName= json['name'],
            weather=json['weather'][0]['main'],
            description=json['weather'][0]['description'],
            temp_mid ="↓"+str(round(json['main']['temp_min']-273.15))+"°"+ " ↑"+str(round(json['main']['temp_max']-273.15))+"°",
           
            temp= str(round(json['main']['temp']-273.15))+"°",
            date = datetime.now().strftime('%x'),
            wind =  'Wind '+str(json['wind']['speed'])+'km/h',
            day =datetime.today().strftime('%A')
        )
    else:
        return "get"


if __name__ =="__main__":
    app.run(debug=True)