from django.contrib import admin

from candidates.models import Candidate, Score


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ("name", "candidate_reference")


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = ("candidate", "score")
