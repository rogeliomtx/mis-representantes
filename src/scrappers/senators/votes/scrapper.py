"""
https://www.senado.gob.mx/64/senadores
Obtiene la lista de senators federales
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


class VotesScrapper(Scrapper):
    # example: https://www.senado.gob.mx/64/votaciones/1131
    url = "https://www.senado.gob.mx/{legislature}/votaciones/{senator_id}"

    @classmethod
    def get_url(cls, legislature, senator_id, *args, **kwargs):
        url = cls.url.format(legislature=legislature, senator_id=senator_id)
        print(f"getting: {url}")
        return url

    @classmethod
    def create_model(cls, legislature, senator_id, *args, **kwargs):
        soup = BeautifulSoup(
            cls.get_source(legislature=legislature, senator_id=senator_id),
            "html.parser",
        )

        items = soup.find("div", class_="panel panel-default").findChildren(
            "div", recursive=False
        )

        title = None
        vote_date = None
        for i in items:
            if i["class"] == ["panel-heading", "text-center"]:
                title = i.get_text(strip=True)
                continue

            if i["class"] == ["panel-heading"]:
                vote_date = i.get_text(strip=True)
                continue

            vote = i.find("div", class_="col-sm-11").get_text(strip=True)
            position = i.find("div", class_="col-sm-1").get_text(strip=True)
            print(vote, position, title, vote_date, sep="\n")
            print("============")


def run(legislature, senator_id, *args):
    # VotesScrapper.create_local_sample(legislature, senator_id)
    VotesScrapper.create_model(legislature, senator_id)
