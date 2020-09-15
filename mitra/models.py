from django.db import models

class Mitra(models.Model):
    nama = models.CharField( max_length=255)
    alamat = models.CharField( max_length=255)
    deskripsi = models.TextField(default='')
    pic = models.CharField( max_length=255)
    telp = models.IntegerField(default='')
