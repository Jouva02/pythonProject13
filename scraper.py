from bs4 import BeautifulSoup
import requests


class scraper:

    def __init__(self, filewithurls, ):
        f = open(filewithurls, "r", encoding="utf-8")
        self.listURLS = f.readlines()

    def gethtml(self, url):
        return requests.get(url).text

    def getinfofromproducthtml(self, producthtml):
        url = producthtml.select_one("meta[itemprop=\"url\"]")["content"]
        name = producthtml.select_one("span.productname").text
        image = producthtml.select_one("img")
        price = producthtml.select_one("meta[itemprop=\"price\"]")["content"].replace(',', '.')
        unitprice = producthtml.select_one("span.unitprice").text
        brand = producthtml.select_one("span.brand").text

        if image is None:
            imageURL = "desconocido"
        else:
            imageURL = image["src"]

        return f"{url} ,{imageURL} ,{name},{float(price)},{brand.strip()},{float(unitprice.split('€')[0].replace(',', '.'))}"

    def scrapURL(self, url):
        originalURL = url

        i=0
        siguientepagina = True
        while siguientepagina:
            i+=1
            print(i)
            html = self.gethtml(url)
            soup = BeautifulSoup(html, "lxml")

            listaproductos = soup.select("ul.productlist li:not(.googleads)")

            for producthtml in listaproductos:
                productline = self.getinfofromproducthtml(producthtml)
                print(productline)

            url = originalURL+f"?page={i}#products"
            if len(listaproductos) == 0:
                siguientepagina=False





    def scrapAll(self):
        for URL in self.listURLS:
            self.scrapURL(URL)

