# ScoreTrackerApp

This Django web application is designed to manage candidate information, test scores, and provide utility functions to import data from CSV and JSON files.


## Features

1. Database Models:
   - **Candidate:** Stores candidate details
   - **Score:** Stores test scores for candidates. A candidate can have multiple scores.

2. Management Commands:
   - **Import CSV data:** Read a CSV file containing candidate and score information and add it to the database.
   - **Read JSON data and sort:** Read a JSON file, create a CSV file with candidates ordered by score (and name in case of a tie).

3. Views:
   - **Candidates View:** Displays a list of all candidates sorted alphabetically by name. Each candidate's scores are shown in ascending order, and the candidate with the highest score is highlighted.

## Getting set up
1. Ensure Python 3.x is installed.
2. Create venv
3. Install necessary libraries using ```pip install -r requirements.txt```.
4. Run the migrations: ```python manage.py migrate```
5. Run the app: ```python manage.py runserver```
6. Access the web application in a browser at http://localhost:8000
7. Access the admin interface at http://localhost:8000/admin/ (if you've created a superuser through ```python manage.py createsuperuser```)

## Import CSV data
- To import candidate and score data from a CSV file, use the following command:
- ```python manage.py read_csv path/to/yourfile.csv```

## Read JSON Data and Sort
- To read a JSON file, create a CSV file with candidates ordered by score (and name in case of a tie), use the following command:
- ```python manage.py read_json path/to/yourfile.json --output path/to/output.csv```

## Candidates View
- Visit http://127.0.0.1:8000/candidates/ to view the list of candidates, their scores, and the candidate with the highest score highlighted.

## Logging
- The application uses the Python logging module to log errors and messages. By default, logs are displayed in the console.

## Testing
- The application uses the pytest library for testing. Run ```pytest``` in order to run the tests.
