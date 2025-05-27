# 📝 Django Task Management System

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.x-success.svg)](https://www.djangoproject.com/)
[![Build](https://img.shields.io/badge/Build-Production%20Ready-brightgreen)]()

> **Modular Django task manager with JWT auth, MySQL, email notifications, and Swagger-documented REST API. Ready for production and frontend integration.**

---

## 🚀 Features

- Custom user model with JWT authentication
- Task CRUD with labels, priority, due dates, and assignments
- Email notifications and reminders
- REST API with Swagger and Redoc documentation
- MySQL backend with environment-based settings
- Production-ready configuration using `python-decouple`

---

## 🛠️ Tech Stack

- **Backend**: Django, Django REST Framework
- **Database**: MySQL
- **Auth**: JWT via DRF SimpleJWT
- **Docs**: Swagger / Redoc (`drf-yasg`)
- **Config**: `python-decouple`, dev/prod settings
- **Deployment**: Render (or any WSGI-compatible host)

---

## ⚙️ Setup Instructions

```bash
# Clone repo
git clone https://github.com/yourusername/todo-app.git
cd todo-app

# Create virtualenv and activate
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env for DB, SECRET_KEY, etc.

# Apply migrations
python manage.py migrate

# Run server
python manage.py runserver
