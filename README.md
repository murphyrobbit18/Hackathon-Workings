# Clinic Management Web Application

## Project Overview
This is a Django-based web application for clinic management, focusing on patient intake, SOAP charting, and physician dashboards. AI features are planned for later integration.  

---

## Getting Started

Follow these steps to get the project running locally.

## Quick Setup (First-Time)

Run these commands to get started:

```bash
# 1. Create virtual environment
python -m venv venv

# 2. Activate virtual environment
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate

# 3. Install dependencies
pip install django
# Or if requirements.txt exists:
# pip install -r requirements.txt

# 4. Apply database migrations
python manage.py migrate

# 5. Run the development server
python manage.py runserver

# 6. (Optional) Create superuser for admin/clinician access
python manage.py createsuperuser


