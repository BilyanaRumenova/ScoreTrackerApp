import csv
import json
import logging
from typing import List, Dict, Any

from django.db import transaction
from django.core.exceptions import ValidationError

from candidates.models import Candidate, Score
from candidates.serializers import CandidateSerializer, ScoreSerializer

logger = logging.getLogger(__name__)


def import_csv_data(csv_file_path: str) -> None:
    """
    Read a CSV file into to the system to add candidates and scores to the DB.

    :param csv_file_path: The path to the CSV file.
    """
    with open(csv_file_path, encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader, None)

        for row in reader:
            try:
                candidate_reference, candidate_name, score = row
                with transaction.atomic():
                    candidate = Candidate(
                        name=candidate_name,
                        candidate_reference=candidate_reference
                    )
                    candidate.full_clean()
                    candidate.save()

                    score = Score(
                        candidate=candidate,
                        score=score
                    )
                    score.full_clean()
                    score.save()

            except (ValidationError, ValueError) as e:
                logger.error(f"Error processing row {row}: {e}")


def read_json_data(json_file_path: str, output_file_path: str) -> None:
    """
    Read data from a JSON file and write out a CSV file with candidates ordered by score.

    :param json_file_path: The path to the JSON file.
    :param output_file_path: The path to the CSV output file.
    """
    with open(json_file_path, 'r') as json_file:
        data: List[Dict[str, Any]] = json.load(json_file)

    sorted_candidates = sorted(data, key=lambda x: (x['score'], x['name']))
    headers = data[0].keys()

    with open(output_file_path, 'w', newline='\n') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        for candidate_data in sorted_candidates:
            candidate_serializer = CandidateSerializer(data={
                'name': candidate_data['name'],
                'candidate_reference': candidate_data['candidate_ref'],
            })
            score_serializer = ScoreSerializer(data={
                'score': candidate_data['score']
            })

            if candidate_serializer.is_valid() and score_serializer.is_valid():
                writer.writerow({
                    'candidate_ref': candidate_data['candidate_ref'],
                    'name': candidate_serializer.validated_data['name'],
                    'score': score_serializer.validated_data['score'],
                })
            else:
                error_message = f"Validation error for candidate: {candidate_data}."
                logger.error(error_message)
