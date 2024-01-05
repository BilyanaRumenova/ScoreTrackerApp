import pytest
from django.test import Client
from django.urls import reverse
from candidates.models import Candidate, Score


@pytest.fixture
def candidates_data():
    # Create test data for candidates and scores
    candidate1 = Candidate.objects.create(candidate_reference="WXYZ6789", name="Jane Smith")
    candidate2 = Candidate.objects.create(candidate_reference="ABCD1234", name="Bilyana Konstantinova")
    Score.objects.create(candidate=candidate1, score=60.0)
    Score.objects.create(candidate=candidate1, score=45.0)
    Score.objects.create(candidate=candidate2, score=55.0)


@pytest.fixture
def client():
    client = Client()
    return client


@pytest.mark.django_db
def test_candidates_view(client, candidates_data):
    response = client.get(reverse('candidates'))

    assert response.status_code == 200
    max_score = response.context['max_score']
    candidates = response.context['candidates']
    candidates_names = list(candidates.keys())
    candidates_scores = list(candidates.values())
    assert len(candidates) == 2

    assert candidates_names[0].name == 'Bilyana Konstantinova'
    assert candidates_scores[0].first().score == 55.0
    assert candidates_names[1].name == 'Jane Smith'
    assert candidates_scores[1].first().score == 45.0
    assert candidates_scores[1].last().score == 60.0
    assert max_score == 60
