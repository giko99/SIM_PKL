from django.forms import ModelForm

from . import models

class PklForm(ModelForm):
    class Meta:
        model = models.Pkl
        exclude = []