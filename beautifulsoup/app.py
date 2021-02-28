from flask import Flask,render_template
from bs4 import BeautifulSoup
import requests

app=Flask(__name__)

@app.route("/")
def home():

    r=requests.get("https://www.trendyol.com/kucuk-ev-aletleri-x-c1104") #siteye istektee bulunyorç
    #print(r.status_code)  #Yapılan isteğini başarı durumu
    soup= BeautifulSoup(r.content)

   # print(soup.prettify())  

    secim =soup.find_all("div",attrs={"class":"p-card-wrppr"})#prdct-desc-cntnr-wrppr
    for item1 in secim:
        ad = item1.find("span",attrs={"class":"prdct-desc-cntnr-name"})
        fiyat =item1.find("div",attrs={"class":"prc-box-sllng"})
        resim = item1.find("img",attrs={"class":"p-card-img"})
        genel =item1.find("div",attrs={"class":"image-container"})

        link ="https://www.trendyol.com/"+ (item1.find("a")).get("href") #ürün detayına giriyor
        detail = requests.get(link) 
        soup_detail = BeautifulSoup(detail.content)
        urunler_detay=soup_detail.select(".pr-in-dt-cn >ul>span>li")
        for item in urunler_detay:
            print(item.text) #ürün detayi listesini döndürüyor.

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
    