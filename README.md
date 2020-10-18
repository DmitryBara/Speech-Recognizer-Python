# Speech-Recognizer-Python
Python, Yandex API

Приложение принимает от пользователя бинарные данные(аудио) в формате data={'audio': b'BinaryData'} и преобразует речь в текст.
Обращается к внешнему сервису Яндекс.SpeechKit.
Документация, требования к загружаемым файлам:
https://cloud.yandex.ru/docs/speechkit/stt/request


--RUN--
Сборка image и запуск docker контейнера вместе с приложением:
docker-compose up

Приложение станет доступно по адресу localhost:8000/recognize_interface/


*TEST
Для запуска тестов, войдите в интерактивную консоль docker контейнера:
docker exec -it django_app_dmitry /bin/sh
docker exec -it django_app_dmitry /bin/bash (optional)

Затем запустите тесты:
python manage.py test


**В ближайщем будущем будет реализовано/улучшено
1. Интерфейс по загрузке файлов будет содержать checkbox для предпочтительного языка 
2. Очередь задач
3. Обращение к другому внешнему API, в случае торможения яндекса
4. Стоит подумать об преезде с джанго и ассинхронной реализации приложения, так как время ожидания ответа от внешнего сервиса достаточно велико.



***Postman request example__
POST /recognize_api/?secret_key=aaa12&lang=ru-RU HTTP/1.1
Host: localhost:8000
Cookie: csrftoken=4UfRg3vaLdXtVXwVvSivfRq4qP2bEpoPS8d0fyaLcMaeMoxx9MqSYdOOxQ019LqiContent-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW

----WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="audio"; filename="test2.ogg"
Content-Type: <Content-Type header here>

(data)
----WebKitFormBoundary7MA4YWxkTrZu0gW
