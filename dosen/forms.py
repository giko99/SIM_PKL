from django.forms import ModelForm

from . import models

class DosenForm(ModelForm):
    class Meta :
        model = models.Dosen
        exclude=[]