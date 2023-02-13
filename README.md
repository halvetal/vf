### Создание БД
>в терминале
```
psql -U postgres -h localhost -W
createdb video_fragments
```

### Создание виртуального окружения
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```



### Запуск сервера 
```
cd video_test/
python manage.py runserver
```

>Ctrl-c
```
python manage.py makemigrations fragment_saver
python manage.py makemigrations accounts
python manage.py migrate
python manage.py createsuperuser
```

>Ввести почту и пароль
```
python manage.py runserver
```
