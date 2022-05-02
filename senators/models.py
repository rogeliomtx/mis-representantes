from django.db.models import Model
from django.db import models


class Base(Model):
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        abstract = True


class Citizen(Base):
    first_name = models.CharField()
    first_surname = models.CharField()
    last_surname = models.CharField()


class SocialMedia(Base):
    citizen = models.ForeignKey("senators.Citizen",
                                on_delete=models.CASCADE,
                                related_name="social_media")
    active = models.BooleanField()
    url = models.URLField()

class PoliticalParty(Base):
    name = models.CharField()


class Senator(Base):
    citizen = models.OneToOneRel("senators.Citizen", on_delete=models.CASCADE)
    faction = models.ForeignKey()
    url = models.URLField()


class Initiative(Base):
    description = models.TextField()
    publication_date = models.DateField()
    url = models.URLField()


class Vote(Base):
    senator = models.ForeignKey("senators.Senator", on_delete=models.CASCADE)
    initiative = models.ForeignKey("senators.Initiative", on_delete=models.CASCADE)
    url = models.URLField()


class Comission(Base):
    name = models.CharField()
    address = models.CharField()
    phone = models.CharField()
    ext = models.CharField()
    email = models.CharField()
    president = models.ForeignKey()
    url = models.URLField()


class ComissionTeam(Base):
    comission = models.ForeignKey()
    senator = models.ForeignKey()
