# Django Sessions with Authentication

This project demonstrates **Django session management** and the use of the **built-in authentication system**.  
It covers both a simple login/logout flow using custom session logic and the recommended Django way with authentication middleware.

## Features
- Custom session-based login and logout (educational purpose, not secure for production)
- Secure authentication using Django's built-in `auth` system
- Login and logout views
- Session storage of username
- Protected dashboard view
- Example templates for login and dashboard

## Structure
- `acct_management/` – custom session-based login and logout
- `pages/` – simple pages including dashboard
- `mysite/` – project settings

## Requirements
- Python 3.x
- Django 5.x

## Running the project
```bash
# Apply migrations
python manage.py migrate

# Run server
python manage.py runserver
```

Then visit:
- `http://127.0.0.1:8000/login/` – Login page
- `http://127.0.0.1:8000/dashboard/` – Dashboard (requires login)
- `http://127.0.0.1:8000/logout/` – Logout
