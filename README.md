# testapp
# Deploying the project to Heroku
1- touch Procfile
    добавлять ==> web: gunicorn djangoherokuapp.wsgi --log-file -
2- добавлять  runtime.txt файл в корневом каталоге проекта и укажите правильную версию Python
3- pip install gunicorn dj-database-url whitenoise psycopg2
4- pip freeze > requirements.txt
5- Добавьте static.settings настройки в файл настроек
    STATIC_ROOT  =   os.path.join(PROJECT_ROOT, 'staticfiles')
    STATIC_URL = '/static/'
6- heroku create "AppName"
7- Добавьте в setting.py 
        ALLOWED_HOSTS = ['AppName.herokuapp.com']
8- git init
9- git add .
10- git commit -m "First commit"       
11- git push heroku master
