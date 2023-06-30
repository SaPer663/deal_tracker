## Подготовка и запуск проекта
### Склонировать репозиторий на локальную машину:
```
git clone git@github.com:SaPer663/DealTracker.git
```

- запустите контейнеры через терминал:
```
sudo docker-compose -f local.yml up -d --build
```
- cоздать суперпользователя Django:
```
sudo docker-compose -f local.yml run --rm django python manage.py createsuperuser
```
### Документация
После запуска сервера документация API доступна по адресу:
- [swagger](http://0.0.0.0:8000/api/swagger/)
Админ панель:
- [admin](http://0.0.0.0:8000/admin/)



### Автор
Александр
