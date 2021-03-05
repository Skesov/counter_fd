Сборка образа
docker build -t 'flask-app:latest' .

Создание и запуск контейнера
docker run -p 5000:5000 --rm -d --name 'flask-server-fd' flask-app

Получение результата
curl http://localhost:5000/



Ссылки:

Git-репозитарий:
https://github.com/Skesov/counter_fd

Проект на travis-ci.org:
https://travis-ci.org/github/Skesov/counter_fd

Смонитированные образы на Docker Hub:
https://hub.docker.com/r/skesov/counter_fd/tags?

Собранное приложение на Heroku:
https://evening-woodland-98547.herokuapp.com/