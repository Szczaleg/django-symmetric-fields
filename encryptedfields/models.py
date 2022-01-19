from django.db import models
from .fields import FernetEncryptedTextField
# Create your models here.


class TestModel(models.Model):
    cos = models.TextField()
    test = FernetEncryptedTextField(show_values=True, null=True, blank=True)
    hidden = FernetEncryptedTextField(show_values=False, null=True, blank=True)