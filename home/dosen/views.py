from django.shortcuts import render, redirect
from . import models, forms
from mitra.models import Mitra

def index(req):
    dosen = forms.DosenForm()
    if req.POST:
        dosen = forms.DosenForm(req.POST)
        if dosen.is_valid():
            dosen.instance.owner=req.user
            dosen.save()
        return redirect('/dosen/')

    tasks = models.Dosen.objects.filter(owner=req.user)
    group = req.user.groups.first()
    if group is not None and group.name == 'staf':
        tasks = models.Dosen.objects.all()
    return render(req, 'dosen/index.html',{
        'data': tasks,
        'dosen' : dosen,
    })


def detail(req, id):
    task = models.Dosen.objects.filter(pk=id).first()
    return render(req, 'dosen/detail.html', {
        'data': task,
    })

def delete(req, id):
    models.Dosen.objects.filter(pk=id).delete()
    return redirect('/dosen/')
    
def update(req, id):
    if req.POST:
        dosen = models.Dosen.objects.filter(pk=id).update(nama_dosen=req.POST['nama_dosen'], nip=req.POST['nip'], kelompok=req.POST['kelompok'])
        return redirect('/dosen/')

    dosen = models.Dosen.objects.filter(pk=id).first()
    return render(req, 'dosen/update.html', {
        'data': dosen,
    })