from django.shortcuts import render
from django.http import HttpResponse
from text_speech.models import TextData, SpeechText
from datetime import datetime

def getVoice(request):
    if request.method == 'POST':
        file_data = request.FILES['textFile']
        print('text file is :',file_data)
        d = TextData(file_name = file_data, uploaded_on = datetime.now())
        d.save()
        print('file is uploaded')
        return HttpResponse('success')

    return render(request, 'upload_data.html', {})

def getTextVoice(request):
    if request.method == 'POST':
        text_data = request.POST['text_data']
        s = SpeechText(text_data = text_data, uploaded_text_on = datetime.now())
        s.save()
        print('user text is saved')
        return HttpResponse('success')
    return render(request, 'user_text.html', {})