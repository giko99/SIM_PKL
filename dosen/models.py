from django.db import models

class Dosen (models.Model):
    nip = models.CharField(max_length=100)
    nama_dosen = models.CharField(max_length=100)
    kelompok = models.CharField(max_length=100)
    