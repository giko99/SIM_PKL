from django.shortcuts import render, redirect
from . import models, forms

def index(req):
    staf = models.Staf.objects.all()
    return render(req, 'staf/index.html',{
        'data': staf,
    })

def new(req):
    form_input = forms.StafForm()
    if req.POST:
        form_input = forms.StafForm(req.POST)
        if form_input.is_valid():
            form_input.save()
        return redirect('/staf/')
    return render(req, 'staf/new.html',{
        'form' : form_input,
    })

def detail(req, id):
    staf = models.Staf.objects.filter(pk=id).first()
    return render(req, 'staf/detail.html', {
        'data': staf,
    })

def delete(req, id):
    models.Staf.objects.filter(pk=id).delete()
    return redirect('/staf/')

def update(req, id):
    if req.POST:
        staf = models.Staf.objects.filter(pk=id).update(nim=req.POST['nim'], nama=req.POST['nama'], prodi=req.POST['prodi'], fakultas=req.POST['fakultas'])
        return redirect('/staf/')

    staf = models.Staf.objects.filter(pk=id).first()
    return render(req, 'staf/update.html', {
        'data': staf,
    })