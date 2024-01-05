from django.urls import path

from candidates.views import CandidatesView

urlpatterns = [
    path("", CandidatesView.as_view(), name="candidates"),
]
