# Flask CRUD Application

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0%2B-lightgrey.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A lightweight yet powerful **Student Management System** built with Flask, offering full CRUD (Create, Read, Update, Delete) operations. Designed for educational purposes, this application demonstrates clean architecture, separation of concerns, and easy extensibility.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [Configuration](#configuration)
- [Usage](#usage)

---

## 📖 Overview

This application allows users to manage student records efficiently. It stores data in a JSON file (or SQLite, depending on your implementation) and provides a clean web interface to perform CRUD operations. The project is structured to be modular, making it easy to swap out the data layer or add new features.

---

## ✨ Features

- **Create** – Add new students with name, email, and course.
- **Read** – View a paginated list of all students.
- **Update** – Edit existing student details.
- **Delete** – Remove a student permanently.
- **Responsive UI** – Built with HTML and Bootstrap for a modern look.
- **Data Persistence** – Stores data in a local JSON file (or SQLite).
- **Environment Configuration** – Uses a `.env` file for sensitive settings.
- **Error Handling** – Graceful handling of invalid requests.

---

## 🧰 Technology Stack

| Technology | Purpose |
|------------|---------|
| **Python 3.8+** | Backend programming language |
| **Flask** | Web framework |
| **Jinja2** | Templating engine |
| **Bootstrap 5** | Frontend styling |
| **JSON / SQLite** | Data storage (choose one) |
| **python-dotenv** | Environment variable management |
| **Git** | Version control |

---

## 📁 Project Structure

```

flask_crud_app/
├── env/                          # Virtual environment (ignored by Git)
├── project/                      # Application root
│   ├── database/                 # Database files (if using SQLite)
│   ├── model/                    # Data models
│   │   └── Student.py            # Student model class
│   ├── templates/                # HTML templates
│   │   └── auth/                 # Authentication-related templates
│   │       └── index.html        # Main dashboard
│   ├── app.py                    # Application entry point
│   ├── config.py                 # Configuration settings
│   └── students.json             # JSON data store (if using JSON)
├── .env                          # Environment variables (ignored)
├── .gitignore                    # Git ignored files
├── requirements.txt              # Python dependencies
└── README.md                     # This file

```

---

## 🔧 Prerequisites

Ensure you have the following installed on your system:

- **Python** (3.8 or higher) – [Download](https://www.python.org/downloads/)
- **pip** (comes with Python)
- **Git** (optional, for cloning)

---

## ⚙️ Installation & Setup

### 1. Clone the repository (or download the ZIP)

```bash
git clone https://github.com/your-username/flask-crud-app.git
cd flask-crud-app
```

2. Create and activate a virtual environment

· Windows:
  ```bash
  python -m venv env
  env\Scripts\activate
  ```
· macOS / Linux:
  ```bash
  python3 -m venv env
  source env/bin/activate
  ```

3. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4. Configure environment variables

Create a .env file in the project root (next to app.py) with the following content:

```env
SECRET_KEY=your-secret-key-here
DEBUG=False
DATABASE_TYPE=json   # or 'sqlite'
```

Important: Replace your-secret-key-here with a strong, random key.

5. Run the application

```bash
python project/app.py
```

6. Access the application

Open your browser and navigate to:

```
http://127.0.0.1:5000
```

---

🔐 Configuration

All settings are managed in project/config.py. The following variables can be adjusted:

Variable Description Default
SECRET_KEY Used for session signing Required
DEBUG Enable/disable debug mode False
DATABASE_TYPE Choose json or sqlite json
JSON_FILE_PATH Path to JSON data file project/students.json
SQLITE_DB_PATH Path to SQLite database project/database/students.db

---

🚀 Usage

Web Interface

· Home – Displays the list of all students.
· Add Student – Fill in the form and submit to create a new record.
· Edit – Click the edit icon next to a student to update their details.
· Delete – Click the delete icon to remove a student (with confirmation).

API Endpoints (if you have them)

If your application exposes a REST API, list them here:

Method Endpoint Description
GET /students Get all students
GET /students/<id> Get a single student
POST /students Add a new student
PUT /students/<id> Update a student
DELETE /students/<id> Delete a student
