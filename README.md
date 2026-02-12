# Interactive Story Game – Django + Flask

A full-stack storytelling platform where users can play interactive stories, rate them, comment, and report content.

Built with:
- Django (frontend + logic)
- Flask (REST API)
- SQLite
- Python

---

## Features

- Play branching stories
- Ratings system
- Comment system
- Report inappropriate stories
- Play history tracking
- Author dashboard
- REST API for stories/pages/choices

---

## Architecture

Django → UI & gameplay  
Flask → API & story engine

---

## Installation

### 1. Clone repo
git clone https://github.com/YOUR_USERNAME/story-game.git
cd story-game

### 2. Create virtual environment
python -m venv .venv
.venv\Scripts\activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run Flask API
cd flask_api
python -m app.app

### 5. Run Django
cd django_app
python manage.py migrate
python manage.py runserver

Open:
http://127.0.0.1:8000
