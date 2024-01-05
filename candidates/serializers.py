from rest_framework import serializers

from candidates.models import Candidate, Score


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ["name", "candidate_reference"]


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ["score"]
