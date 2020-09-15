from django.shortcuts import render, redirect
from . import models, forms

def index(req):

    pkl = models.Pkl.objects.all()
    return render(req, 'mahasiswa/index.html', {
        'data' : pkl,
    }) 

def input(req):
    form_input = forms.PklForm()

    if req.POST:
        form_input = forms.PklForm(req.POST)

        if form_input.is_valid():
            form_input.save()
        return redirect('/')

    pkl = models.Pkl.objects.all()
    return render(req, 'mahasiswa/input.html', {
        'data': pkl,
        'form': form_input,
    })

def detail(req, id):
    pkl = models.Pkl.objects.filter(pk=id).first()    
    return render(req, 'mahasiswa/detail.html', {
        'data': pkl,
    })

def delete(req, id):
    models.Pkl.objects.filter(pk=id).delete()
    return redirect('/')

def update(req, id):
    if req.POST:
        pkl = models.Pkl.objects.filter(pk=id).update(judul=req.POST['judul'], nama=req.POST['nama'], alamat=req.POST['alamat'], deskripsi=req.POST['deskripsi'], telp=req.POST['telp'])
        return redirect('/')

    pkl = models.Pkl.objects.filter(pk=id).first()    
    return render(req, 'mahasiswa/update.html', {
        'data': pkl,
    })