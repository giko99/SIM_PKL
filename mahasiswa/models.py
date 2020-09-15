from django.db import models

# class Mahasiswa(models.Model):
#     nama = models.CharField(max_length=255)
#     nim = models.CharField(max_length=255)
#     jurusan = models.CharField(max_length=255)
#     prodi = models.CharField(max_length=255)
#     sks = models.CharField(max_length=255)

class Pkl(models.Model):
    judul = models.CharField(max_length=255)
    nama = models.CharField(max_length=255)
    alamat = models.CharField(max_length=255)
    deskripsi = models.TextField(default='')
    telp = models.CharField(max_length=255)

# class Kelompok(models.Model):
#     nim = models.CharField(max_length=255)
#     nama = models.CharField(max_length=255)
#     jurusan = models.CharField(max_length=255)
#     prodi = models.CharField(max_length=255)


