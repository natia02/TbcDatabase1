# Library Management System

This is a simple library management system implemented in Python. It utilizes SQLite as a database to store information about books.

## Table of Contents

- [Usage](#usage)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)

## Usage

1. **Run the Project:**
    - Navigate to the project directory.
    - Execute the main script:
        ```
        python main.py
        ```
2. **Functionality:**
    - The project provides the following functionalities:
        - Creating a database and filling it with book information from a JSON file.
        - Calculating and printing the average number of pages across all books.
        - Printing the title of the largest book in terms of the number of pages.

## Project Structure

- `main.py`: Main script to run the project.
- `Book.py`: Definition of the Book class.
- `Books.json`: JSON file containing data about books.
- `Library.db`: SQLite database to store book information.
- `README.md`: Documentation file.
- `requirements.txt`: List of Python dependencies.

## Dependencies

- `sqlite3`: Python library for working with SQLite databases.
- `json`: Python library for working with JSON data.
