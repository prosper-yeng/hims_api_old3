from django.db import models
from choice.views import LanguageChoice, StatusChoice
from django.core.validators import FileExtensionValidator


class Language(models.Model):
    name = models.CharField(max_length=100, choices=LanguageChoice.choices, unique=True)
    status = models.CharField(
        max_length=100, choices=StatusChoice.choices, default=StatusChoice.APPROVED
    )

    def __str__(self):
        if self.name:
            return "{}".format(self.name)
