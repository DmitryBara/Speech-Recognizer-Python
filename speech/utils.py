import os
import json
import requests
from django.core.files.storage import FileSystemStorage


class YandexRecognizer:

    @classmethod
    def set_token_to_env(cls):
        """Метод устанавливает iamToken в переменную окружения. Раз в 12 часов должен обновляться """

        token_data = '{"yandexPassportOauthToken": "' + os.getenv("YANDEX_TOKEN") + '"}'
        res = requests.post(url="https://iam.api.cloud.yandex.net/iam/v1/tokens",
                            data=token_data)
        obj = json.loads(res.text)
        os.environ['IAM_TOKEN'] = obj['iamToken']

    @classmethod
    def post_request_to_service(cls, audio, lang):
        """Делает запросы на сторонний Api. Помимо отлавливаемых ошибок может получить ошибку от внешнего сервиса"""

        try:
            response = requests.post(url=f"https://stt.api.cloud.yandex.net/"
                                         f"speech/v1/stt:recognize?folderId={os.getenv('FOLDER_ID')}&lang={lang}",
                                     data=audio,
                                     headers={'Content-Type': 'multipart/form-data', 'Accept': 'application/json',
                                              'Authorization': 'Bearer {}'.format(os.environ['IAM_TOKEN']) })
            response = json.loads(response.text)
            return response
        except Exception as exc:
            err = {'error_code': 'server could not get response from yandex', 'more_info': str(exc)}
            return err

    @classmethod
    def speech_to_text(cls, audio, lang):
        """Метод преобразует голос в текст. Метод сам получит iamToken, если он устаревший или его нет.
        В переменной res могут быть: ответ с текстом, ответ со статусом ошибки, пойманная ошибка в запросе на yandex"""

        res = cls.post_request_to_service(audio, lang)

        if res.get('error_code', None) == 'UNAUTHORIZED':
            cls.set_token_to_env()
            res = cls.post_request_to_service(audio, lang)

        return res


class QueueHelpers:
    """ Класс для управления очередями """
    def save_file_to_media(file):
        """Метод сохранит фаил в хранилище, для будущих реализаций приложения с очередями"""

        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        file_url = fs.url(filename)





