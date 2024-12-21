web: gunicorn health_expenses.wsgi --log-file - 
#or works good with external database
web: python manage.py migrate && gunicorn health_expenses.wsgi

