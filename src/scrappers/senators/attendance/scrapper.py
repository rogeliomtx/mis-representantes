"""
https://www.senado.gob.mx/{legislature}/attendance/{senator_id}#info
Obtiene las fechas de asistencia de un senador en una determinada legislatura.
- fecha
- asistencia
- enlace al pase de lista
"""

from bs4 import BeautifulSoup
from scrappers.generic import Scrapper
from datetime import datetime


class AttendanceScrapper(Scrapper):
    # example: https://www.senado.gob.mx/64/asistencias/1068
    url = "https://www.senado.gob.mx/{legislature}/asistencias/{senator_id}"

    @classmethod
    def get_url(cls, legislature, senator_id, *args, **kwargs):
        return cls.url.format(legislature=legislature, senator_id=senator_id)

    @classmethod
    def create_model(cls, legislature, senator_id, *args, **kwargs):
        soup = BeautifulSoup(
            cls.get_source(legislature, senator_id, *args, **kwargs),
            "html.parser",
        )

        items = soup.find("div", class_="activityContent").find("table").find_all("tr")
        for item in items:
            i = item.find_all("td")
            if i:
                attendance_date = i[1].get_text(strip=True)
                url = i[1].find("a")["href"]
                url = f"https://www.senado.gob.mx{url}"
                attendance_status = i[2].get_text(strip=True)

                print(
                    attendance_date,
                    url,
                    attendance_status,
                    sep="\t",
                )
            else:
                i = item.find("th").get_text(strip=True)
                print(i)


def run(legislature, senator_id, *args):
    # AttendanceScrapper.create_local_sample(legislature, senator_id)
    AttendanceScrapper.create_model(legislature, senator_id)
