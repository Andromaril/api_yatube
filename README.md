# api_yatube
api_yatube
Начало проекта, полный проект  - api_final_yatube

В проекте api_yatube есть приложение posts с описанием моделей Yatube. Реализовано API для всех моделей приложения.

API должен доступен только аутентифицированным пользователям. В проекте использована аутентификацию по токену TokenAuthentication.

Аутентифицированный пользователь авторизован на изменение и удаление своего контента; в остальных случаях доступ предоставляется только для чтения. При попытке изменить чужие данные возвращаеться код ответа 403 Forbidden.

Для взаимодействия с ресурсами описаны и настроены такие эндпоинты:

  ```
  api/v1/api-token-auth/ (POST): передаём логин и пароль, получаем токен.

  api/v1/posts/ (GET, POST): получаем список всех постов или создаём новый пост.

  api/v1/posts/{post_id}/ (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем пост по id.

  api/v1/groups/ (GET): получаем список всех групп.

  api/v1/groups/{group_id}/ (GET): получаем информацию о группе по id.

  api/v1/posts/{post_id}/comments/ (GET, POST): получаем список всех комментариев поста с id=post_id или создаём новый, указав id поста, который хотим прокомментировать.

  api/v1/posts/{post_id}/comments/{comment_id}/ (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем комментарий по id у поста с id=post_id.
  ```

В ответ на запросы POST, PUT и PATCH API возвращае объект, который был добавлен или изменён.


<h2>Как запустить проект:</h2>
Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Andromaril/api_yatube.git
```

Cоздать и активировать виртуальное окружение:

```
1. python3 -m venv env
2. source env/bin/activate
```

Установить зависимости из файла requirements.txt:*

```
1.python3 -m pip install --upgrade pip
2. pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
