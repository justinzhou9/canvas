# canvas
need to install Flask, django 2.0, and pymysql in project interpreter

1. use command in terminal: python manage.py makemigrations 
    This will migrate all the tables I created from the code to local mysql (need to update admin and password)
2. use command : python manage.py createsuperuser
    This will create an account for administrator so that I can upload cvs files 
3. use command : python manage.py runserver
    This will generate our web link : 127.0.0.1:8000
4. log in with admin account and upload both professor and student csv files
5. Now I can log in with whatever student and professor emails and their passwords
