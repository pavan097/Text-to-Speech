from django.conf.urls import url
from text_speech.views import getVoice, getTextVoice

urlpatterns = [
    url(r'upload_data/', getVoice),
    url(r'user_text/',getTextVoice),
]
