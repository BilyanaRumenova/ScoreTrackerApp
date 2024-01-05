from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    MinLengthValidator,
)
from django.db import models


class Candidate(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    candidate_reference = models.CharField(
        max_length=8, blank=False, null=False, validators=[MinLengthValidator(8)]
    )

    def __str__(self):
        return self.name


class Score(models.Model):
    candidate = models.ForeignKey(
        Candidate, on_delete=models.CASCADE, related_name="scores"
    )
    score = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return f"{self.score}"
        # return f"{self.candidate.name} - {self.score}"
