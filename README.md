#  foodgram-project-react
#  IP 84.252.131.104
![example workflow](https://github.com/chaandrey/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)

# Описание. 


С помощью сервиса Foodgram можно публиковать рецепты, подписываться на других пользователей, фильтровать рецепты по тегам, добавлять понравившиеся рецепты в избранное и скачивать файл со списком продуктов.


# Установка.


Для того чтобы развернуть проект, следуйте инструкции:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone [https://github.com/chaandrey/foodgram-project-react
```

```
cd foodgram-project-react
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate

```
Cоздать файл .env в директории /infra/ с содержанием:

```
SECRET_KEY=секретный ключ django
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

Перейти в директирию и установить зависимости из файла requirements.txt:

```
cd backend/
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить сервер:

```
python manage.py runserver
```

# Запуск проекта в Docker контейнере

Установите Docker.

Параметры запуска описаны в файлах docker-compose.yml и nginx.conf которые находятся в директории infra/.
При необходимости добавьте/измените адреса проекта в файле nginx.conf

Запустите docker compose:

```
docker-compose up -d --build
```

После сборки появляются 3 контейнера:

- контейнер базы данных db
- контейнер приложения backend
- контейнер web-сервера nginx

Примените миграции:

```
docker-compose exec backend python manage.py migrate
```

Загрузите ингредиенты:

```
docker-compose exec backend python manage.py load_ingrs
```

Загрузите теги:

```
docker-compose exec backend python manage.py load_tags
```

Создайте администратора:

```
docker-compose exec backend python manage.py createsuperuser
```

Соберите статику:
```
docker-compose exec backend python manage.py collectstatic --noinput
```

