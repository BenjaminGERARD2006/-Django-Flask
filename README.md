# NAHB – Not Another Hero’s Book

Interactive Story Platform (Django + Flask)

A full-stack web application inspired by *Choose Your Own Adventure* books.
Users can play branching stories, track gameplay, rate stories, comment, and report content.

This project is built with a **separated architecture**:

* **Flask** → REST API for story content
* **Django** → Web interface, gameplay engine, users, statistics

---

## 🚀 Features Implemented

### 🎮 Story gameplay

* Play interactive stories with multiple pages and choices
* Reach different endings
* Navigation system: start → choices → next page → ending

### 📊 Gameplay tracking

* Play sessions saved in Django
* Ending reached stored per play
* Basic statistics ready

### 👤 User system

* Django authentication
* Logged-in users can interact with stories
* Plays linked to users

### ⭐ Community features

* Rate stories (1–5 stars)
* Comment on stories
* Report stories to moderation

### 🧠 Architecture

**Flask API**

* Stores:

  * stories
  * pages
  * choices
* Exposes REST endpoints

**Django Web App**

* UI templates
* Gameplay engine
* Ratings / comments / reports
* Play tracking
* Authentication

---

## 🧱 Tech Stack

* Python
* Django
* Flask
* SQLite
* HTML / CSS
* REST API

---

## 📁 Project Structure

```
project-root/
│
├── django_app/
│   ├── game/
│   ├── config/
│   └── manage.py
│
├── flask_api/
│   ├── app/
│   └── run.py
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Run

### 1️⃣ Clone repository

```
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
```

### 2️⃣ Create virtual environment

```
python -m venv .venv
.venv\Scripts\activate
```

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run Flask API

```
cd flask_api
python -m app.app
```

API runs at:

```
http://127.0.0.1:5000
```

Test:

```
http://127.0.0.1:5000/stories
```

---

## ▶️ Run Django app

```
cd django_app
python manage.py migrate
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000
```

---

## 🔌 Main API Endpoints (Flask)

### Reading

* GET `/stories`
* GET `/stories/<id>`
* GET `/stories/<id>/start`
* GET `/pages/<id>`

### Writing

* POST `/stories`
* PUT `/stories/<id>`
* DELETE `/stories/<id>`
* POST `/stories/<id>/pages`
* POST `/pages/<id>/choices`

---

## 🎯 Learning Objectives

* Full-stack Django + Flask architecture
* REST API design
* Gameplay engine logic
* Database modeling
* Authentication & permissions
* Community features implementation

---

## 📌 Current Status

✔ Story creation
✔ Story playing
✔ Page navigation
✔ Ending detection
✔ Play tracking
✔ Ratings
✔ Comments
✔ Reports
✔ Django + Flask integration

---

## 🔮 Possible Improvements

* Average rating display
* Advanced statistics dashboard
* Author tools
* Story graph visualization
* Player path visualization
* Docker deployment
* Public hosting

---

## 👨‍💻 Author

Benjamin — Full-stack Python project
Django & Flask architecture practice

---

