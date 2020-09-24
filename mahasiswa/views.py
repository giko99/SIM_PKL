from django.shortcuts import render, redirect
from . import models, forms
from mitra.models import Mitra

def index(req):

    tasks = models.Pkl.objects.filter(owner=req.user)
    form_input = forms.PklForm()

    if req.POST:
        form_input = forms.PklForm(req.POST, req.FILES)
        if form_input.is_valid():
            form_input.instance.owner = req.user
            form_input.save()
            return redirect('/mahasiswa')
        else:
            print(form_input.errors)
            print('databelumasuk')

    group = req.user.groups.first()
    if group is not None and group.name == 'staf':
        tasks = models.Pkl.objects.all()
    return render(req, 'mahasiswa/index.html',{
        'form' : form_input,
        'data': tasks,  
    })
    

def index_staf(req):
    tasks = models.Pkl.objects.filter(owner=req.user)
    form_input = forms.PklForm()
    
    if req.POST:
        form_input = forms.PklForm(req.POST, req.FILES)
        if form_input.is_valid():
            form_input.instance.owner = req.user
            form_input.save()
        return redirect('/mahasiswas')

    group = req.user.groups.first()
    if group is not None and group.name == 'staf':
        tasks = models.Pkl.objects.all()
    return render(req, 'mahasiswas/index.html',{
        'data': tasks,  
    })


def input(req):
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

def input_staf(req):
    form_input = forms.PklForm()

    if req.POST:
        form_input = forms.PklForm(req.POST, req.FILES)
        if form_input.is_valid():
            form_input.instance.owner = req.user
            form_input.save()
        return redirect('/mahasiswas')
        
    mitra = Mitra.objects.first()
    return render(req, 'mahasiswas/input.html', {
        'form' : form_input,
        'd': mitra,
    })


def detail(req, id):
    pkl = models.Pkl.objects.filter(pk=id).first()    
    return render(req, 'mahasiswa/detail.html', {
        'data': pkl,
    })

def detail_staf(req, id):
    pkl = models.Pkl.objects.filter(pk=id).first()    
    return render(req, 'mahasiswas/detail.html', {
        'data': pkl,
    })


def delete(req, id):
    models.Pkl.objects.filter(pk=id).delete()
    return redirect('/mahasiswa')

def delete_staf(req, id):
    models.Pkl.objects.filter(pk=id).delete()
    return redirect('/mahasiswas')


def update(req, id):
    if req.POST:
        pkl = models.Pkl.objects.filter(pk=id).update(judul=req.POST['judul'], dosen=req.POST['dosen'], tanggal_mulai=req.POST['tanggal_mulai'], tanggal_selesai=req.POST['tanggal_selesai'])
        return redirect('/mahasiswa')

    pkl = models.Pkl.objects.filter(pk=id).first()    
    return render(req, 'mahasiswa/update.html', {
        'data': pkl,
    })

def update_staf(req, id):
    if req.POST:
        pkl = models.Pkl.objects.filter(pk=id).update(judul=req.POST['judul'], dosen=req.POST['dosen'], tanggal_mulai=req.POST['tanggal_mulai'], tanggal_selesai=req.POST['tanggal_selesai'])
        return redirect('/mahasiswas')

    pkl = models.Pkl.objects.filter(pk=id).first()    
    return render(req, 'mahasiswas/update.html', {
        'data': pkl,
    })

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