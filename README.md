<h1 align="center">Проект социальная сеть Yatube</a> 
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/></h1>
<h3 align="center">Социальная сеть для публикации текстов и фотографий, а также подписки на других авторов.</h3>


### Стек технологий:

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
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
