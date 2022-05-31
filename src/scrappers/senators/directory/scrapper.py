"""
https://www.senado.gob.mx/64/senadores/directorio_de_senadores
Obtiene la lista de senadores federales
- nombre
- dirección
- telefóno
- dirección
- correo electrónico
- legislatura

y ligas de:
- perfil https://www.senado.gob.mx/64/senador/{id}
- attendance https://www.senado.gob.mx/64/asistencias/{id}#info
- votaciones https://www.senado.gob.mx/64/votaciones/{id}#info
- iniciativas
"""

from bs4 import BeautifulSoup
from scrappers.generic import Scrapper


class SenatorScrapper(Scrapper):
    # example: https://www.senado.gob.mx/64/senadores
    url = "https://www.senado.gob.mx/{legislature}/senators"

    @classmethod
    def get_url(cls, legislature, *args, **kwargs):
        return cls.url.format(legislature=legislature)

    @classmethod
    def create_model(cls, legislature, *args, **kwargs):
        soup = BeautifulSoup(
            cls.get_source(legislature, *args, **kwargs), "html.parser"
        )

        items = soup.find_all("div", class_="panel")
        for item in items:
            body = item.find("div", class_="panel-body").find_all("p")
            name = body[0].get_text(strip=True)
            address = body[1].get_text(strip=True)
            phone = body[2].get_text(strip=True).split("Ext.")[0].replace("Tel:", "")
            ext = body[2].get_text(strip=True).split("Ext.")[1].split("Correo")[0]
            email = body[2].get_text(strip=True).split("Correo electrónico:")[1]
            print(name, address, phone, ext, email, sep="\n")

            footer = item.find("div", class_="panel-footer")
            print("social media")
            for a in footer.find_all("a", href=True):
                print(a["class"][1].replace("btn-", ""), a["href"])
            print("========")


def run(legislature, *args):
    # SenatorScrapper.create_local_sample(legislature=legislature)
    SenatorScrapper.create_model(legislature=legislature)
