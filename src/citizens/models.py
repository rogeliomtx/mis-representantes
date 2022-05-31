from django.db import models
from generics.models import Base


class Citizen(Base):
    first_name = models.CharField(max_length=100)
    first_surname = models.CharField(max_length=100)
    last_surname = models.CharField(max_length=100, null=True, blank=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.first_surname} {self.last_surname}"

    class Meta:
        verbose_name = "citizen"
        verbose_name_plural = "citizens"


class SocialMedia(Base):
    class SocialMedia(models.TextChoices):
        facebook = "facebook", "facebook"
        twitter = "twitter", "twitter"
        youtube = "youtube", "youtube"

    citizen = models.ForeignKey(
        "citizens.Citizen", on_delete=models.CASCADE, related_name="social_networks"
    )
    is_active = models.BooleanField(default=False)
    url = models.URLField()
    social_network = models.CharField(choices=SocialMedia.choices, max_length=50)
