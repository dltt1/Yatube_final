# Yatube

Социальная сеть для публикации текстов и фотографий, а также подписки на других авторов.

### Стек технологий:

<div>
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"/>
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green"/>
  <img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white"/>
  <img src="https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)"/>
</div>
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)

### Функционал:
- Регистрация и аутентификация пользователей
- Создание, редактирование и удаление постов
- Добавление и удаление фотографий к постам
- Подписка на авторов и просмотр их постов в ленте
- Комментирование постов
- Модерирование комментариев (доступно только администраторам)
- Лайки и дизлайки для постов
- Поиск по постам

### Запуск проекта в dev-режиме
### 1. Клонируйте репозиторий:

```bash
git clone git@github.com:dltt1/hw05_final.git  
```

### 2. Установите зависимости:

```
pip install -r requirements.txt
``` 

### 3. Создайте и примените миграции: 

```
python manage.py makemigrations
python manage.py migrate
```

### 4. Создайте суперпользователя:

```
python manage.py createsuperuser
```

### 5. Запустите сервер:

```
python3 manage.py runserver
```

### Авторы
Дима Шапченко
