from django.forms import ModelForm
from django.forms import ClearableFileInput
from . import models

class CatatanForm(ModelForm):
    class Meta :
        model = models.Catatan
        exclude=['owner']
       
class GambarForm(ModelForm):
    class Meta :
        model = models.Gambar
        fields = ['upload_img']
        widgets = {
            'upload_img': ClearableFileInput(attrs={'multiple': True}),
        }
