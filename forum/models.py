from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from mitra.models import Mitra

# Create your models here.

class Forum(models.Model):
    nama_mitra = models.ForeignKey(Mitra, on_delete = models.DO_NOTHING)
    mahasiswa = models.ForeignKey(User,on_delete = models.DO_NOTHING,related_name='mahasiswas')
    waktu = models.DateTimeField(default=datetime.now)
    desc = models.TextField()
    # upload_img = models.ImageField(default='', upload_to='images/', null=False, blank=True)

class Posting(models.Model):
    forum = models.ForeignKey(Forum, on_delete = models.DO_NOTHING,related_name='posting')
    owner = models.ForeignKey(User, on_delete = models.DO_NOTHING,related_name='owner')
    waktu = models.DateTimeField(default=datetime.now)
    desc = models.TextField()

class Komen(models.Model):
    posting = models.ForeignKey(Posting, on_delete = models.DO_NOTHING,related_name='komentar')
    pengguna = models.ForeignKey(User, on_delete = models.DO_NOTHING,related_name='pengguna')
    waktu = models.DateTimeField(default=datetime.now)
    desc = models.TextField()

class Balas(models.Model):
    komen = models.ForeignKey(Komen, on_delete = models.DO_NOTHING,related_name='balasan')
    user = models.ForeignKey(User, on_delete = models.DO_NOTHING,related_name='user')
    waktu = models.DateTimeField(default=datetime.now)
    desc = models.TextField()


