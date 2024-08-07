#web: gunicorn tejasangeethawebsite.wsgi --log-file -
#web: gunicorn tejasangeethawebsite.wsgi:application --log-file=-`
#web: python manage.py migrate && python manage.py collectstatic --no-input && gunicorn tejasangeethawebsite.wsgi --log-file-
web: gunicorn tejasangeethawebsite.wsgi --log-file - 
#or works good with external database
web: python manage.py migrate && gunicorn tejasangeethawebsite.wsgi
