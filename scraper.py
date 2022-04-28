from bs4 import BeautifulSoup
import requests
import time





def gethtml(url):
    return requests.get(url).text

def getinfofromproducthtml(producthtml):
    url = producthtml.select_one("meta[itemprop=\"url\"]")["content"]
    name = producthtml.select_one("span.productname").text
    image = producthtml.select_one("img")
    price = producthtml.select_one("meta[itemprop=\"price\"]")["content"].replace(',', '.')
    unitprice = producthtml.select_one("span.unitprice").text
    brand = producthtml.select_one("span.brand")

    if brand is None:
        brand = "marca blanca"
    else:
        brand = brand.text

    if image is None:
        imageURL = "desconocido"
    else:
        imageURL = image["src"]

    return f"{url} ,{imageURL} ,{name},{float(price)},{brand.strip()},{float(unitprice.split('€')[0].replace(',', '.'))}"

def scrapURL(url,file):
    originalURL = url

    i=0
    siguientepagina = True
    while siguientepagina:
        time.sleep(1)
        i+=1
        print(i)
        html = gethtml(url)
        soup = BeautifulSoup(html, "lxml")

        listaproductos = soup.select("ul.productlist li:not(.googleads)")

        for producthtml in listaproductos:
            productline = getinfofromproducthtml(producthtml)
            file.write(productline+f",{url}\n")
            print(productline)

        url = originalURL+f"?page={i}#products"
        if len(listaproductos) == 0:
            siguientepagina=False





def scrapAll(filewithurls):
    fr = open(filewithurls, "r", encoding="utf-8")
    listURLS = fr.readlines()
    fr.close()

    f = open("productos.txt","w",encoding="utf-8")
    i = 0
    for URL in listURLS:
        i+=1
        scrapURL(URL.strip(),f)
        if i==10:
            break
