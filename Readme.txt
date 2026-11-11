LITTLE LEMON - DJANGO REST FRAMEWORK CAPSTONE

Project overview
A Django REST Framework API for restaurant menu items and table bookings.
The project includes a simple HTML home page, MySQL configuration, token
authentication, user registration, admin pages, and API tests.

API ENDPOINTS FOR PEER REVIEW
- GET    /restaurant/menu/
- POST   /restaurant/menu/              (authenticated)
- GET    /restaurant/menu/<id>/
- PUT    /restaurant/menu/<id>/         (authenticated)
- PATCH  /restaurant/menu/<id>/         (authenticated)
- DELETE /restaurant/menu/<id>/         (authenticated)
- GET    /restaurant/booking/           (authenticated; own bookings)
- POST   /restaurant/booking/           (authenticated)
- GET    /restaurant/booking/<id>/      (authenticated; own booking or staff)
- PUT    /restaurant/booking/<id>/      (owner or staff)
- DELETE /restaurant/booking/<id>/      (owner or staff)
- POST   /auth/register/                (public; returns a token)
- POST   /api-token-auth/               (username and password; returns token)
- GET    /                                (HTML home page)
- /admin/                                (Django admin)

AUTHENTICATION
Use this header for protected endpoints:
Authorization: Token YOUR_TOKEN_VALUE

Register with JSON:
{"username":"reviewer","email":"reviewer@example.com","password":"StrongPass123!"}

Get a token with JSON:
{"username":"reviewer","password":"StrongPass123!"}

MENU EXAMPLE
{"title":"Greek salad","price":"12.50","inventory":20,"description":"Fresh salad"}

BOOKING EXAMPLE
{"name":"Taylor","no_of_guests":2,"booking_date":"2026-12-01T19:00:00Z","comments":"Window seat"}

WINDOWS QUICK START
1. Install Python 3.11 or newer and Git.
2. Open this folder in VS Code.
3. In the VS Code terminal run:
   py -m venv .venv
   .venv\Scripts\activate
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   copy .env.example .env
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
4. Open http://127.0.0.1:8000/ and http://127.0.0.1:8000/restaurant/menu/

DATABASE
For the first local run, DB_ENGINE=sqlite in .env is convenient.
MySQL support is configured in settings.py. To use MySQL:
- Install MySQL Server and create a database named littlelemon.
- Edit .env: DB_ENGINE=mysql, DB_NAME=littlelemon, DB_USER, DB_PASSWORD,
  DB_HOST=127.0.0.1, DB_PORT=3306.
- Run python manage.py migrate again.
The project uses PyMySQL as the MySQL driver to simplify Windows setup.

TESTS
Run:
python manage.py test restaurant

INSOMNIA
Create a request collection and use http://127.0.0.1:8000 as the base URL.
For protected requests, add Authorization: Token <token>.
Menu list is public. Booking endpoints require authentication.
Use JSON request bodies for POST, PUT and PATCH.

GIT AND GITHUB
Before publishing, create a GitHub repository and run:
git init
git add .
git commit -m "Build Little Lemon Django REST API"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main

IMPORTANT
Replace the GitHub URL above with your own repository URL. Do not commit .env,
database passwords, secret keys, virtual environments, or local database files.
For production, set DEBUG=False and use a strong secret key and HTTPS.
