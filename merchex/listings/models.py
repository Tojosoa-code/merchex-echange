from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Band(models.Model):

    class Genre(models.TextChoices):
        HIP_HOP = "HH"
        SYNTH_POP = "SP"
        ALTERNATIVE_ROCK = "AR"

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(max_length=10, choices=Genre.choices)
    biography = models.fields.TextField(max_length=1000)
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1970), MaxValueValidator(2021)]
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class Listing(models.Model):

    class Types(models.TextChoices):
        RECORDS = "RC"
        CLOTHING = "CL"
        MISCELLANEOUS = "ML"
        POSTERS = "PT"

    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=1000)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(null=True)
    type = models.fields.CharField(max_length=10, choices=Types.choices)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.title}"
