from django.forms import ModelForm
from mitra.models import Mitra

from . import models

class PklForm(ModelForm):
    # class Meta:
    #     model = model.Mitra
    #     exclude = ['pic']

    class Meta:
        model = models.Pkl
        exclude = ['owner']
        # fields = ['judul']