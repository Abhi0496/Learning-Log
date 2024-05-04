# Learning-Log

Learning Log is a web application built with Django, a high-level Python web framework. It allows users to log the topics they're interested in and make journal entries as they learn about each topic.


## Features

1) User authentication (registration and login)
2) Create, read, update, and delete topics
3) Create, read, and edit entries associated with topics
4) Admin site for managing users, topics, and entries
5) Secure password storage using password hashing
6) SQLite database for data storage
7) Template inheritance for a consistent UI across pages

## Models

The application consists of the following models:
1) Topic: Represents a topic of interest for a user.
2) Entry: Represents a journal entry associated with a specific topic.

The Entry model has a one-to-many relationship with the Topic model, allowing multiple entries to be associated with a single topic.

## Technologies Used

1) Python 3.x
2) Django 5.0.4
3) SQLite (default Django database)
4) HTML/CSS/Bootstrap (for UI)

## Installation

1) Clone the repository: git clone https://github.com/Abhi0496/Learning-Log.git
2) Create a virtual environment: *python -m venv env*
3) Activate the virtual environment:
    On Windows: env\Scripts\activate
    On Unix or Linux: source env/bin/activate
4) Install the required packages: *pip install -r requirements.txt*
5) Apply database migrations: *python manage.py migrate*
6) Create a superuser: *python manage.py createsuperuser*
7) Start the development server: *python manage.py runserver*
8) Access the application at *http://localhost:8000/*

## Usage

1) Register a new account or log in with an existing one.
2) Create new topics or view existing ones.
3) Add entries to a topic, describing what you've learned.
4) Edit or delete existing entries as needed.
5) Explore the admin site (accessible at http://localhost:8000/admin/) for managing users, topics, and entries.

## Images

![Admin Page](/images/admin_page.png)