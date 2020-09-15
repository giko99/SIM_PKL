from django.shortcuts import render, redirect
from . import models, forms

def index(req):
    mitra = models.Mitra.objects.all()
    return render(req, 'mitra/index.html',{
        'data': mitra,
    })

def new(req):
    form_input = forms.MitraForm()
    if req.POST:
        form_input = forms.MitraForm(req.POST)
        if form_input.is_valid():
            form_input.save()
        return redirect('/mitra/')
    return render(req, 'mitra/new.html',{
        'form' : form_input,
    })

def detail(req, id):
    mitra = models.Mitra.objects.filter(pk=id).first()
    return render(req, 'mitra/detail.html', {
        'data': mitra,
    })

def delete(req, id):
    models.Mitra.objects.filter(pk=id).delete()
    return redirect('/mitra/')

def update(req, id):
    if req.POST:
        mitra = models.Mitra.objects.filter(pk=id).update(nama=req.POST['nama'], alamat=req.POST['alamat'], deskripsi=req.POST['deskripsi'], pic=req.POST['pic'], telp=req.POST['telp'])
        return redirect('/mitra/')

    mitra = models.Mitra.objects.filter(pk=id).first()
    return render(req, 'mitra/update.html', {
        'data': mitra,
    })