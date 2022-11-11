from django.db import models
from common.models import CommonModel

# Create your models here.
class Category(CommonModel):

    """Room or Experience Catogory"""

    class CatogoryKindChoices(models.TextChoices):
        ROOMS = "rooms", "Rooms"
        EXPERIENCES = "experiences", "Experiences"

    name = models.CharField(max_length=70)
    kind = models.CharField(
        max_length=15,
        choices=CatogoryKindChoices.choices,
    )

    def __str__(self) -> str:
        return f"{self.kind.title()}: {self.name}"

    class Meta:
        verbose_name_plural = "Categories"
