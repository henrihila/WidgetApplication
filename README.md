# Widget Management Application

Flask-RESTful Widget API 

This project implements API endpoints for creating, reading, listing, updating, and deleting objects called "Widgets".


Main libraries used:
1. Flask - Web Framework 
2. Flask-RESTful - restful API library.
3. Flask-SQLAlchemy - adds support for SQLAlchemy ORM.

Project structure:
```
├── models
│   ├── __init__.py
│   ├── widget.py
├── resources
│   ├── __init__.py
│   ├── widget.py
├── tests
│   ├── test_widget.py
├── app.py
├── db.py
├── openapi.yaml
└── README.md
```
* models - holds all models.
* resources - holds all resurces.
* test - holds all unit testing scripts.
* app.py - flask application initialization.
* db.py - database (SQLAlchemy) initialization

## Running 

1. Clone repository.
2. Setup virtual environment 
3. Install dependencies. Run the following commands:
    - pip install Flask
    - pip install Flask-RESTful
    - pip install Flask-SQLAlchemy
4. Start server by running python app.py or flask run
5. For unit testing: Run test_widget.py script under /tests directory. Instructions (assuming flask server is still up and running):
    - Open a new terminal window
    - Navigate to project directory
    - Activate virtual environment
    - Remove SQLite file database (data.db) for a clean / fresh new database instance