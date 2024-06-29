Sure, here's the optimized format for the Django IMDB Project:

-------------------------

Django IMDB Project
===================

This project is an API-driven application built using Django and Django Rest Framework (DRF) that emulates the functionality of IMDB. It includes comprehensive features for managing watchlists, stream platforms, and user reviews.

Features
--------

- User Authentication: Secure endpoints accessible only to authenticated users.
- Rate Limiting: Custom throttling to prevent abuse and ensure fair usage.
- Role-Based Permissions: Advanced permissions to restrict actions based on user roles.
- Enhanced Filtering, Searching, and Ordering: Efficient data retrieval mechanisms.
- CRUD Operations: Full create, read, update, and delete functionalities for all models.

![API Animation](https://media.giphy.com/media/xT9IgzoKnwFNmISR8I/giphy.gif)

Installation
------------

1. Clone the repository:
   ```bash
   git clone https://github.com/R4255/rest-api.git
   cd rest-api
   
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   
3. Run migrations:
   ```bash 
   python manage.py migrate
   
4. Create a superuser:
   ```bash
   py manage.py createsuperuser
   
5. Run the development server:
   ```bash
    python manage.py runserver
    
-------------------------
