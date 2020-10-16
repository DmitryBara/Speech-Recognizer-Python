from django import forms
from django.core.files.images import get_image_dimensions
# from .models import Article

class AudioForm(forms.Form):

    # class Meta:
    #     model = Article
    #     fields = ('title', 'text', 'image', 'hiden')


    def __init__(self, *args, **kwargs):
        super(AudioForm, self).__init__(*args, **kwargs)

    title = forms.CharField(max_length=50)
    # image = forms.ImageField()
    audio = forms.FileField()

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if not image:
            raise forms.ValidationError('Изображение не загружено')
        if not self.article_id:
            w, h = get_image_dimensions(image)
            if w < 200 or h < 200:
                raise forms.ValidationError('Минимальное разрешение изображения 200x200')
            if image.size > 5242880:
                raise forms.ValidationError('Максимальный допустимый рамер фаила 5 MB')
        return image