# ScoreTrackerApp

This Django web application is designed to manage candidate information, test scores, and provide utility functions to import data from CSV files and reading JSON files.

## Features

1. **Database Models:**
   - Candidate: Stores candidate details
   - Score: Stores test scores for candidates. A candidate can have multiple scores as each candidate is allowed to take the test multiple times.

2. **Utility Module:**
   - Contains two function which:
       - Read a CSV file into to the system to add candidates and scores to the DB.
       - Read the provided JSON file and write out a CSV file with candidates ordered by score (and name in case of a tie).

3. **Management Commands:**
   - Import CSV file: Read the first utility function and imports data to the database.
   - Read JSON file: Read the second utility function and writes out a CSV file.

4. **Views:**
   - *Candidates View:* Displays an HTML page at path "/candidates" with an html table containing:
       - The list of all candidates in the database sorted alphabetically by name along with their reference.
       - Each candidate's scores are shown in ascending order, and the candidate with the highest score is highlighted.

## Getting set up
1. Ensure Python 3.x is installed.
2. Create a virtual environment (`venv`).
3. Install necessary libraries using ```pip install -r requirements.txt```.
4. Run the migrations: ```python manage.py migrate```
5. Run the app: ```python manage.py runserver```
6. Access the web application in a browser at http://localhost:8000
7. Access the admin interface at http://localhost:8000/admin/ (if you've created a superuser through ```python manage.py createsuperuser```)

## Importing CSV data
- To import candidate and score data from a CSV file, use the following command:
- ```python manage.py read_csv path/to/yourfile.csv```

## Reading JSON Data and Sort
- To read a JSON file, and write out a CSV file with candidates ordered by score (and name in case of a tie), use the following command:
- ```python manage.py read_json path/to/yourfile.json --output path/to/output.csv```

## Candidates View
- Visit http://127.0.0.1:8000/candidates/ to view the list of candidates, their references, their scores, and the candidate with the highest score highlighted.

## Logging
- The application uses the Python logging module to log errors and messages. By default, logs are displayed in the console.

## Testing
- The application uses the pytest library for testing. Run ```pytest``` in order to run the tests.
