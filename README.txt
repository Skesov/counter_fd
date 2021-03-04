Сборка образа
docker build -t 'flask-app:latest' .

Создание и запуск контейнера
docker run -p 5000:5000 --rm -d --name 'flask-server-fd' flask-app

Получение результата
curl http://localhost:5000/