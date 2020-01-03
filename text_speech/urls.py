from django.conf.urls import url
from text_speech.views import getVoice

urlpatterns = [
    url(r'upload_data/', getVoice)
]
