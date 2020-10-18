import os
from django import forms


class AudioForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(AudioForm, self).__init__(*args, **kwargs)

    audio = forms.FileField()
    lang = forms.CharField(max_length=5)

    def clean_audio(self):
        audio = self.cleaned_data.get('audio')
        if audio:
            if audio.size > 5 * 1024 * 1024:
                raise forms.ValidationError("Audio file is too large ( > 5mb )")
            if not audio.content_type in ['audio/ogg']:
                raise forms.ValidationError("Content-Type is not audio/ogg")
            if not os.path.splitext(audio.name)[1] in [".ogg", ".opus"]:
                raise forms.ValidationError("Yandex API accept only .ogg, .opus format ")
            return audio
        else:
            raise forms.ValidationError("Couldn't read uploaded audio")

    def clean_lang(self):
        lang = self.cleaned_data.get('lang')
        if lang:
            if lang not in ["ru-RU", "en-US"]:
                raise forms.ValidationError("Укажите язык из списка доступных")
            return lang