# Exam Result Management System

A Django-based CRUD web application for managing student exam results.

## Features

- 📋 **List Results** – View all student results in a paginated, sortable table
- ➕ **Add Result** – Add a new student result with name, roll number, subject, marks, and grade
- ✏️ **Edit Result** – Update any existing student result
- 🗑️ **Delete Result** – Remove a student result with a confirmation prompt
- 📊 **Dashboard Stats** – See total students, passed/failed counts, and average marks
- 🎨 **Grade Color Coding** – Visual grade badges for quick result scanning

## Tech Stack

- **Backend**: Python 3 / Django 6
- **Database**: SQLite3 (default)
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Templating**: Django Template Language (DTL)

## Project Structure

```
crud with django/
├── examresult/          # Django project settings
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── results/             # Main app
│   ├── migrations/      # DB migrations
│   ├── templates/
│   │   └── results/
│   │       ├── base.html
│   │       ├── result_list.html
│   │       ├── result_form.html
│   │       └── confirm_delete.html
│   ├── models.py        # Result model
│   ├── views.py         # CRUD views
│   ├── forms.py         # ModelForm
│   ├── urls.py          # App URL patterns
│   └── admin.py         # Admin registration
├── manage.py
├── .gitignore
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/sandeshbhandari99/crudwithdjango.git
cd crudwithdjango

# 2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux/Mac

# 3. Install dependencies
pip install django

# 4. Apply migrations
python manage.py migrate

# 5. Run the development server
python manage.py runserver
```

Open your browser at **http://127.0.0.1:8000/**

## CRUD Operations

| Operation | URL                  | Method    |
|-----------|----------------------|-----------|
| List      | `/`                  | GET       |
| Add       | `/add/`              | GET, POST |
| Edit      | `/edit/<id>/`        | GET, POST |
| Delete    | `/delete/<id>/`      | GET, POST |

## Model Fields

| Field          | Type        | Description                     |
|----------------|-------------|---------------------------------|
| `student_name` | CharField   | Full name of the student        |
| `roll_number`  | IntegerField| Unique roll number              |
| `subject`      | CharField   | Subject name                    |
| `marks`        | IntegerField| Marks obtained (0–100)          |
| `grade`        | CharField   | Grade (A+, A, B+, B, C+, C, D, F) |

## License

MIT License — feel free to use and modify.
