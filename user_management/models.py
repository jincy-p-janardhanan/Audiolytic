from django.db import models
import logging

def validate_file_extension(value):
    logging.info('validating file')
    if not value.name.endswith('.mp3'):
        logging.info('not mp3')
        raise ValidationError(u'Error message')

class UploadAudio(models.Model):
    uploaded_file = models.FileField(validators=[validate_file_extension])
    uploaded_at = models.DateTimeField(auto_now_add=True)

