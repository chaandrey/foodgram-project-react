# foodgram-project-react
#  IP 84.252.131.104
![example workflow](https://github.com/chaandrey/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)

Описание. 


С помощью сервиса Foodgram можно публиковать рецепты, подписываться на других пользователей, фильтровать рецепты по тегам, добавлять понравившиеся рецепты в избранное и скачивать файл со списком продуктов.


Установка.


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




Примеры.

Для того чтобы получить доступ к полному функционалу , пользователь должен зарегестрироваться и получить JWT токен:

```
POST /api/v1/jwt/create/
```
BODY:
```
{
  "username": "username",
  "password": "password"
}
```

Зарегистрированный пользователь может создавать новые посты:

```
POST /api/v1/posts/
```
BODY:
```
{
  "text": "Post text"
}
```
Редактировать / удалять уже существующие посты ( автор поста должен быть тот же пользователь , кто редактирует/удаляет):

```
DELETE /api/v1/posts/1/
```
BODY:
```
{
  "id": "Post id"
}
```


Добавлять комментарии:

```
POST /api/v1/posts/1/comments/
```
BODY:
```
{
  "test": "New Comment"
}
```

Подписаться на другого пользователя
```
POST /api/v1/follow/
```
BODY:
```
{
  "following": "author"
}
```



Анонимный пользователь имеет только read only права.


Запрос всех постов :

```
GET /api/v1/posts/
```


Запрос поста по его id.

```
GET /api/v1/posts/1
```


Запрос комментариев

```
GET /api/v1/posts/1/comments/
```
