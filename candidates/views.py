from typing import List

from django.db.models import Max
from django.views.generic import TemplateView

from candidates.models import Candidate, Score


class CandidatesView(TemplateView):
    template_name = "candidates.html"
    queryset = Candidate.objects.all().order_by("name")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        max_score = self.get_max_score()
        candidates_data = {}
        for candidate in self.queryset:
            scores = self.order_candidate_scores(candidate)
            candidates_data[candidate] = scores

        context["candidates"] = candidates_data
        context["max_score"] = max_score
        return context

    @staticmethod
    def get_max_score() -> float:
        return Score.objects.all().aggregate(Max("score"))["score__max"]

    @staticmethod
    def order_candidate_scores(candidate: Candidate) -> List[Score]:
        return Score.objects.filter(candidate=candidate).all().order_by("score")
