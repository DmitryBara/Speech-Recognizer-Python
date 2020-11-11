# Speech-Recognizer-Python
Python, Yandex API

Приложение принимает от пользователя бинарные данные(аудио) в формате data={'audio': b'BinaryData'} и преобразует речь в текст.
Обращается к внешнему сервису Яндекс.SpeechKit.
Документация, требования к загружаемым файлам:
https://cloud.yandex.ru/docs/speechkit/stt/request


# Run
Сборка image и запуск docker контейнера вместе с приложением:
`docker-compose up`

Приложение станет доступно по адресу http://127.0.0.1:8000/recognize_interface/


# Test
Для запуска тестов, войдите в интерактивную консоль docker контейнера:

`docker exec -it django_app_dmitry /bin/sh`

`docker exec -it django_app_dmitry /bin/bash` (optional)

Затем запустите тесты:
`python manage.py test`


В ближайщем будущем будет реализовано/улучшено
1. Интерфейс по загрузке файлов будет содержать checkbox для предпочтительного языка 
2. Очередь задач
3. Обращение к другому внешнему API, в случае торможения яндекса
4. Стоит подумать об преезде с джанго и ассинхронной реализации приложения, так как время ожидания ответа от внешнего сервиса достаточно велико.



__Postman request example__

```
POST /recognize_api/?secret_key=aaa12&lang=ru-RU HTTP/1.1
Host: localhost:8000
Content-Disposition: form-data; name="audio"; filename="test2.ogg"
(binary-data)
```
