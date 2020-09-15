from django.db import models
from datetime import datetime

class Catatan(models.Model):
    tgl_kegiatan = models.DateField(default=datetime.now)
    judul = models.CharField(max_length=100)
    ket = models.TextField(max_length=200)
    upload_img = models.ImageField(default='', upload_to='images/')
    

