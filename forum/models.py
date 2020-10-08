from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from mitra.models import Mitra

# Create your models here.

class Forum(models.Model):
    nama_mitra = models.ForeignKey(Mitra, on_delete = models.DO_NOTHING)
    mahasiswa = models.ForeignKey(User, on_delete = models.DO_NOTHING,related_name='mahasiswas')
    waktu = models.DateTimeField(default=datetime.now)
    desc = models.TextField()
    # upload_img = models.ImageField(default='', upload_to='images/', null=False, blank=True)

class Posting(models.Model):
    user = models.ForeignKey(User, on_delete = models.DO_NOTHING,related_name='user')
    waktu = models.DateTimeField(default=datetime.now)
    desc = models.TextField()