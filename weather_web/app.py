from flask import Flask,render_template,request ,jsonify
from datetime import datetime
import requests
from geopy.geocoders import Nominatim
import geocoder
app=Flask(__name__)

@app.route("/")
def home():
      return render_template("index.html")
   
def locationFindFucn():     #Kişinin lokasyonun bulmaktadır(Şehir geri döner)
    geolocator = Nominatim(user_agent="geoapiExercises")
    myloc = geocoder.ip('me')

    Latitude = str(myloc.latlng[0])
    Longitude = str(myloc.latlng[1])
    location = geolocator.reverse(Latitude+","+Longitude)
    return location.raw['address']['city']

@app.route("/save/",methods=["POST"])
def save():
    if request.method=="POST":        
        searchText= request.form["data"]

        if(searchText==""): #Hiçbir şey aratma yapmaz ise kişinin lokasyonuna ait hava durum bilgisi döner
            searchText=locationFindFucn()
        
        url="http://api.openweathermap.org/data/2.5/forecast?q="+searchText+"&id=524901&appid=e885b85ed11e3dddf35c2160d37709ef"
        result=requests.get(url)
        json =result.json()
        result=requests.get(url)

        listWeather =[]
        for item in json['list']:
            x=0
            for item2 in listWeather:
                if item['dt_txt'].split(" ")[0] ==item2["dt_txt"].split(" ")[0]:
                   x=1

            if x != 1 :
                listWeather.append({
                         'date': (datetime.fromtimestamp(item['dt'])).strftime("%A") ,
                         'weather':item['weather'][0]['main'],
                         'description':item['weather'][0]['description'],
                         'temp_mid':"↓"+str(round(item['main']['temp_min']-273.15))+"°"+ " ↑"+str(round(item['main']['temp_max']-273.15))+"°",
                         'temp':str(round(item['main']['temp']-273.15)),
                         'humidity': str(item['main']['humidity'])+'%',
                         'wind' :  str(item['wind']['speed'])+'km/h',
                         'icon': item['weather'][0]['icon'],
                         'dt_txt':item['dt_txt']
                })

            
                   
                    
        return jsonify(
            cityName= json['city']['name'],
            listWeather= listWeather
        )
    else:
        return "get"


if __name__ =="__main__":
    app.run(debug=True)