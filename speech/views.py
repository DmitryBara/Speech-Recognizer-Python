from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import AudioForm


def recognize(request):
    if request.method == "POST":
        form = AudioForm(request.POST, request.FILES)
        if form.is_valid():
            # audio = form.save(commit=False)
            audio = form.fields['audio']
            # article.author_id = request.user.id
            # article.uuid = request.session['a_uid']
            # article.save()
            # url = article.get_url()
            # return HttpResponseRedirect('aaaaaa')
            return HttpResponse(audio)

    if request.method == "GET":
        form = AudioForm()
        # request.session['a_uid'] = uuid.uuid4().hex

    context = {'form': form, 'user': request.user}
    return render(request, 'recognize.html', context)
