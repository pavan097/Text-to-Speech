from django.db import models

class TextData(models.Model):
    file_name = models.FileField(upload_to='uploads/')
    uploaded_on = models.DateTimeField(auto_now_add=True)

class SpeechText(models.Model):
    text_data = models.CharField(max_length=255)
    uploaded_text_on = models.DateTimeField(auto_now=True)