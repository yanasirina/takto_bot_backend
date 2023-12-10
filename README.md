# takto_bot_backend
Бэкенд для ЛМС системы школы "Так-то да"

## Установка
версия python: 3.12 \
pip install -r requirements.txt (в виртуальное окружение) \
создать .env файл на основе .env.example

## Настройка базы данных
docker run -d --name takto_db -p 54320:5432 -v /var/docker/takto/data/db:/var/lib/postgresql/data/ --restart always -e POSTGRES_PASSWORD=123 -e POSTGRES_USER=takto_da -e POSTGRES_NAME=takto_da postgres:16.0

python manage.py migrate
python manage.py createsuperuser

## Запуск проекта
python manage.py runserver \
или с помощью конфигурации pycharm:
![image](https://github.com/yanasirina/takto_bot_backend/assets/92913721/07caae76-2b53-449f-9f51-bfd83c91d585)

