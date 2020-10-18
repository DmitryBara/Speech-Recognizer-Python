import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import YandexRecognizer
from .forms import AudioForm


def recognize_interface(request):
    if request.method == "POST":
        form = AudioForm(request.POST, request.FILES)
        if form.is_valid():
            audio = form.cleaned_data['audio']
            lang = form.cleaned_data['lang']
            result = YandexRecognizer.speech_to_text(audio, lang)
            return HttpResponse(json.dumps(result, ensure_ascii=False), content_type="application/json")

    if request.method == "GET":
        form = AudioForm()

    context = {'form': form}
    return render(request, 'recognize.html', context)


# Временное решение
# В будущем функционал будет расширен выдачей токена и проверкой валидности токена по базе
active_secret_keys = ['aaa12', 'bbb23', 'ccc34', 'ddd45', 'eee56']

@csrf_exempt
def recognize_api(request):
    if request.method == "POST":
        if request.GET.get('secret_key') not in active_secret_keys:
            return HttpResponse('Не передан параметр secret_key, либо передан недействительный')
        lang = request.GET.get('lang')
        audio = request.FILES['audio']
        result = YandexRecognizer.speech_to_text(audio, lang)
        return HttpResponse(json.dumps(result, ensure_ascii=False), content_type="application/json")
    else:
        return JsonResponse({'error': 'Not valid request method (accepting only POST)'})
