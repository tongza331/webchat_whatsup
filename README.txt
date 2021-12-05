- Framework we used
    1. Frontend Framework: HTML,CSS,JS
    2. Backend Framwork: Django
    3. Websocket: Django channels
    4. DBMS: PostgreSQL, Redis
## Step install my code.
1. Install library from requirements.txt by command: pip install -r requirements.txt
2. Activate enviroment in folder venv_channels 
3. In setting.py you need to change name and password database to your pgAdmin4
4. Enter folder mysite to run: python manage.py makemigrations
5. Run: python manage.py migrate for migrate from models.py to your pgAdmin4
6. If you want to enter admin site in Django you have to create super user first: python manage.py createsuperuser
7. Run: python manage.py runserver for start using web chat.
8. To run websocket:
    8.1 If you use windows you can use Memurai: https://www.memurai.com/ download and install it.
    8.2 If you use ubuntu can use redis server: https://redis.io/topics/quickstart: 
        use this command for start redis server: $ redis-server (If port already use please type : $ sudo service redis-server stop and run it again.)
