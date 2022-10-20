# Проект «API для Yatube»

### Описание
«API для Yatube» - API интерфейс для социальной сети Yatube, позволяет создавать и редактировать посты, пописываться на авторов постов, оставлять комментарии.

### Использумые технологии

[Python 3.7](https://docs.python.org/3.7/whatsnew/3.7.html)

[Django 2.2.16](https://docs.djangoproject.com/en/4.1/releases/2.2.16/)

[DjangoRestFramework 3.12.4](https://www.django-rest-framework.org/community/release-notes/)

[DRF-SimpleJWT 4.7.2](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:DoDmAnat/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

## Примеры запросов к API
###  Получение всех публикаций
```
GET api/v1/posts/
```

### Информация о сообществе
```
GET .../v1/groups/{id}/
```
Пример ответа 
```
{
    "id": integer,
    "title": string,
    "slug": string,
    "description": string 
} 
```
### POST-запрос авторизованного пользователя на добавление записи

```
POST .../api/v1/posts/

{
    "text": string (текст публикации),
    "image": string or null <binary>,
    "group": 	integer or null (id сообщества)
} 
```
Пример ответа
```
{
    "id": integer (id публикации),
    "author": string (username пользователя),
    "text": string (текст публикации),
    "pub_date": string <date-time>,
    "image": string or null <binary>,
    "group": integer or null (id сообщества),
} 
```
### POST-запрос авторизованного пользователя на добавление комментария
```
POST .../api/v1/posts/14/comments/

{
    "text": string (текст комментария)
} 
```
Пример ответа
```
{
    "id": integer (id комментария),
    "author": "string (username пользователя)",
    "text": "string (текст комментария)",
    "created": string <date-time>,
    "post": integer (id публикации),
} 
```
Автор: [Домрачев Дмитрий](https://github.com/DoDmAnat)
