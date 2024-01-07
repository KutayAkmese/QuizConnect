<h1>QuizConnect</h1>

<h3>Ziel des Projekts</h3>

Das Hauptziel des QuizConnect-Projekts besteht darin, eine Plattform zu schaffen, die Schülern während ihrer High-School- und Universitätszeit ermöglicht, Wissen effektiv zu teilen und voneinander zu lernen, selbst wenn sie keine persönliche Beziehung zueinander haben.


<h2>Zum Laufen bekommen</h2>

1. Clone the repository to local

`git clone https://github.com/KutayAkmese/QuizConnect.git` 

2. Open a terminal and install requirements.txt

`pip install -r requirements.txt`

3. Configuring Database Using Online PostgreSQL (This might be cause the program to run slowly)



3.1 Head into settings.py

3.2 Find this block
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'QuizConnect',
        'USER': 'postgres',
        'PASSWORD': 'Berkan188138',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
```

3.3 Replace this code with the provided code below.

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway',
        'USER': 'postgres',
        'PASSWORD': 'BCc-4GFFG-63gB2D-Gb13B251G2FBGEb',
        'HOST': 'roundhouse.proxy.rlwy.net',
        'PORT': '26991'
    }
}
```

4. Migrate the changes <br>
```python manage.py makemigrations``` <br>
```python manage.py migrate```

5. Run the server <br>
```python manage.py runserver```


<b>After completing all these steps, you can click on the link in the terminal to go to the website, register, and start using the system.</b>

