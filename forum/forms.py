from django.forms import ModelForm

from . import models

class ForumForm(ModelForm):
    class Meta :
        model = models.Forum
        exclude=['waktu']

class PostingForm(ModelForm):
    class Meta :
        model = models.Posting
        exclude=['user','waktu']