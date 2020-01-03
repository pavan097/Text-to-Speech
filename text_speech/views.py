from django.shortcuts import render
from django.http import HttpResponse
from text_speech.models import TextData
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