from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from mitra.models import Mitra


class Pkl(models.Model):
    owner = models.ForeignKey(User, on_delete = models.DO_NOTHING,related_name='mahasiswa')
    judul = models.CharField(max_length=255)
    nama_mitra = models.ForeignKey(Mitra, on_delete = models.DO_NOTHING)
    dosen = models.CharField(max_length=255, default='')
    tanggal_mulai = models.DateField(default=datetime.now)
    tanggal_selesai = models.DateField()


