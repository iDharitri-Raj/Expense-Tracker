# Expense Tracker

## Overview

The Expense Tracker is a full-stack web application designed to help users manage and track their expenses effectively. The application is built using Django, a powerful Python web framework, and includes essential features like user authentication, expense categorization, and detailed expense tracking.

## Features

- **User Authentication**: Secure login and registration functionality for users.
- **Expense Management**: Add, update, and delete expenses with ease.
- **Expense Categorization**: Organize expenses into different categories.
- **Expense Reports**: Generate detailed reports to analyze spending patterns.
- **Responsive Design**: User-friendly interface built with Bootstrap for a seamless experience on all devices.

## Project Structure

- **ExpenseTracker/**: The main Django project directory containing global settings and configurations.
  - `settings.py`: Contains configuration settings including database connections, installed apps, middleware, etc.
  - `urls.py`: Defines the URL routing for the entire project.
  - `wsgi.py` and `asgi.py`: Configuration files for deploying the project.
  
- **tracker/**: The main application handling expense-related functionalities.
  - `models.py`: Defines the database models such as Expense and Category.
  - `views.py`: Contains the view logic for handling HTTP requests and returning appropriate responses.
  - `urls.py`: URL routing specific to the tracker app.
  - `admin.py`: Configuration for managing tracker models in the Django admin interface.
  - `templates/`: Directory containing HTML templates rendered by views.
  
- **db.sqlite3**: The SQLite database file used to store application data.

- **manage.py**: A command-line utility to interact with this Django project.

- **public/**: Contains static files (CSS, JavaScript, images) and media files for the project.
