from django.db import models

class TextData(models.Model):
    file_name = models.FileField(upload_to='uploads/')
    uploaded_on = models.DateTimeField(auto_now_add=True)