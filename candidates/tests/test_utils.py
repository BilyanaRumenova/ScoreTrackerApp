import json
import os
import tempfile

import pytest

from candidates.models import Candidate, Score
from candidates.utils import import_csv_data, read_json_data


@pytest.fixture
def json_data():
    json_data = [
        {"candidate_ref": "ABCD1234", "name": "Bilyana Konstantinova", "score": 75.0},
        {"candidate_ref": "WXYZ6789", "name": "Jane Smith", "score": 90.0},
        {"candidate_ref": "EFGH5678", "name": "Test Reference", "score": 60.0},
        {"candidate_ref": "EFGH56788", "name": "Invalid Reference", "score": 60.0},
        {"candidate_ref": "IGKL5678", "name": "Invalid Points", "score": 600.0},
    ]
    return json_data


@pytest.fixture
def csv_data():
    csv_data = (
        "candidate_ref,name,score\n"
        "ABCD1234,Bilyana Konstantinova,75.0\n"
        "EFGH56788,Invalid reference,60.0\n"
        "IGKL5678,Invalid points,600.0\n"
        "WXYZ6789,John Doe, 90.0"
    )
    return csv_data


@pytest.mark.django_db
def test_import_csv_data(csv_data):
    with tempfile.NamedTemporaryFile(
        mode="w+", suffix=".csv", delete=False
    ) as temp_file:
        temp_file.write(csv_data)
        temp_file_path = temp_file.name

    import_csv_data(temp_file_path)

    assert Candidate.objects.count() == 2
    assert Score.objects.count() == 2

    os.remove(temp_file_path)


def test_read_json_data(json_data):
    with tempfile.NamedTemporaryFile(
        mode="w+", suffix=".json", delete=False
    ) as json_file:
        json.dump(json_data, json_file)
        json_file_path = json_file.name

    with tempfile.NamedTemporaryFile(
        mode="w+", suffix=".csv", delete=False
    ) as csv_file:
        csv_file_path = csv_file.name

    read_json_data(json_file_path, csv_file_path)

    with open(csv_file_path, "r") as csv_file:
        csv_content = csv_file.readlines()

    expected_rows = [
        "candidate_ref,name,score\n",
        "EFGH5678,Test Reference,60.0\n",
        "ABCD1234,Bilyana Konstantinova,75.0\n",
        "WXYZ6789,Jane Smith,90.0\n",
    ]

    assert csv_content == expected_rows
    assert "EFGH56788,Invalid Reference,60.0" not in csv_content
    assert "IGKL5678,Invalid Points,600.0" not in csv_content

    os.remove(json_file_path)
    os.remove(csv_file_path)
