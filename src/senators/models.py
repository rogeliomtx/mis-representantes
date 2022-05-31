from django.db import models

from generics.models import Base, Catalog


class PoliticalParty(Catalog):
    logo = models.ImageField()


class Senator(Base):
    citizen = models.OneToOneField(
        "citizens.Citizen", on_delete=models.CASCADE, related_name="senators"
    )
    political_party = models.ForeignKey(
        "senators.PoliticalParty", on_delete=models.CASCADE, related_name="senators"
    )
    soruce_url = models.URLField()


class Initiative(Catalog):
    publication_date = models.DateField()
    url = models.URLField()


class Vote(Base):
    class VoteType(models.TextChoices):
        pro = "pro", "pro"
        abstained = "abstained", "abstención"
        agains = "contra", "contra"
        absent = "absent", "ausente"

    senator = models.ForeignKey(
        "senators.Senator", on_delete=models.CASCADE, related_name="votes"
    )
    initiative = models.ForeignKey(
        "senators.Initiative", on_delete=models.CASCADE, related_name="initiatives"
    )
    vote = models.CharField(choices=VoteType.choices, max_length=15)
    url = models.URLField()


class Comission(Base):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    ext = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    president = models.ForeignKey(
        "senators.Senator",
        on_delete=models.CASCADE,
        related_name="comission_presidencies",
    )
    url = models.URLField()


class ComissionTeam(Base):
    class Roles(models.TextChoices):
        president = "president", "presidente"
        secretary = "secretary", "secreatario(a)"
        member = (
            "member",
            "miembro",
        )

    comission = models.ForeignKey(
        "senators.Comission", on_delete=models.CASCADE, related_name="members"
    )
    senator = models.ForeignKey(
        "senators.Senator", on_delete=models.CASCADE, related_name="comissions"
    )
    role = models.CharField(choices=Roles.choices, max_length=50)

    class Meta:
        unique_together = ("comission", "senator")
