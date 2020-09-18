from django.shortcuts import render, redirect
from . import models, forms
from mitra.models import Mitra

def index(req):

    tasks = models.Pkl.objects.filter(owner=req.user)
    group = req.user.groups.first()
    if group is not None and group.name == 'staf':
        tasks = models.Pkl.objects.all()
    return render(req, 'mahasiswa/index.html',{
        'data': tasks,  
    })

def input(req):

    # if req.POST:
    #     pkl = models.Pkl.objects.create(judul=req.POST['judul'], nama=req.POST['nama'], alamat=req.POST['alamat'], deskripsi=req.POST['deskripsi'], telp=req.POST['telp'])
    #     return redirect('/mahasiswa')
    #     # if form_input.is_valid():
    #     #     form_input.save()
    #     # return redirect('/')

    # mitra = Mitra.objects.first()
    # return render(req, 'mahasiswa/input.html', {
    #     'd': mitra,
    # })
    form_input = forms.PklForm()

    if req.POST:
        form_input = forms.PklForm(req.POST, req.FILES)
        if form_input.is_valid():
            form_input.instance.owner = req.user
            form_input.save()
        return redirect('/mahasiswa')
        
    mitra = Mitra.objects.first()
    return render(req, 'mahasiswa/input.html', {
        'form' : form_input,
        'd': mitra,
    })

def detail(req, id):
    pkl = models.Pkl.objects.filter(pk=id).first()    
    return render(req, 'mahasiswa/detail.html', {
        'data': pkl,
    })

def delete(req, id):
    models.Pkl.objects.filter(pk=id).delete()
    return redirect('/mahasiswa')

def update(req, id):
    if req.POST:
        pkl = models.Pkl.objects.filter(pk=id).update(judul=req.POST['judul'], nama=req.POST['nama'], alamat=req.POST['alamat'], deskripsi=req.POST['deskripsi'], telp=req.POST['telp'])
        return redirect('/mahasiswa')

    pkl = models.Pkl.objects.filter(pk=id).first()    
    return render(req, 'mahasiswa/update.html', {
        'data': pkl,
    })