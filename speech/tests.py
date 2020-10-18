from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

class SpeechRecognize(TestCase):

    def test_interface_get(self):
        res = self.client.post('/recognize_interface/')
        self.assertEqual(res.status_code, 200)

    def test_api_case_1(self):

        with open("test_data/test1.ogg", "rb") as f:
            binary_data = f.read()
            upload_file = SimpleUploadedFile('not_matter', binary_data)

        response = self.client.post('/recognize_api/?secret_key=aaa12&lang=ru-RU', data={'audio': upload_file})
        expected = '{"result": "Привет как дела спасибо хорошо"}'
        self.assertEqual(response.content.decode('utf8'), expected)


    def test_api_case_2(self):

        with open("test_data/test2.opus", "rb") as f:
            binary_data = f.read()
            upload_file = SimpleUploadedFile('not_matter', binary_data)

        response = self.client.post('/recognize_api/?secret_key=aaa12&lang=ru-RU', data={'audio': upload_file})
        expected = '{"result": "Настройках установленные счетчики децибел чтобы не превышать допустимый уровень шума"}'
        self.assertEqual(response.content.decode('utf8'), expected)


    def test_api_case_eng_1(self):

        with open("test_data/test_eng1.opus", "rb") as f:
            binary_data = f.read()
            upload_file = SimpleUploadedFile('not_matter', binary_data)

        response = self.client.post('/recognize_api/?secret_key=aaa12&lang=en-US', data={'audio': upload_file})
        expected = '{"result": "Apprentice program Google Films list"}'
        self.assertEqual(response.content.decode('utf8'), expected)


    def test_api_case_eng_2(self):

        with open("test_data/test_eng2.opus", "rb") as f:
            binary_data = f.read()
            upload_file = SimpleUploadedFile('not_matter', binary_data)

        response = self.client.post('/recognize_api/?secret_key=aaa12&lang=en-US', data={'audio': upload_file})
        expected = '{"result": "If you eat package contains several modules sew mitred washer tutorials about modules and packages confuse later when we get the jango"}'
        self.assertEqual(response.content.decode('utf8'), expected)

