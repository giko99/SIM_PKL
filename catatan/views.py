from django.shortcuts import render, redirect
from . import models, forms

def index(req):
    tasks = models.Catatan.objects.all()
    return render(req, 'catatan/index.html',{
        'data': tasks,
    })
    
def new(req):
    form_input = forms.CatatanForm()

    if req.POST:
        form_input = forms.CatatanForm(req.POST, req.FILES)
        if form_input.is_valid():
            form_input.save()
        return redirect('/catatan/')
    return render(req, 'catatan/new.html',{
        'form' : form_input,
    })

def detail(req, id):
    task = models.Catatan.objects.filter(pk=id).first()
    return render(req, 'catatan/detail.html', {
        'data': task,
    })

def delete(req, id):
    models.Catatan.objects.filter(pk=id).delete()
    return redirect('/catatan/')

def update(req, id):
    if req.POST:
        task = models.Catatan.objects.filter(pk=id).update(
            tgl_kegiatan=req.POST['tgl_kegiatan'], 
            judul=req.POST['judul'], 
            ket=req.POST['ket'], 
            upload_img=req.POST['upload_img'])
        return redirect('/catatan/')

    task = models.Catatan.objects.filter(pk=id).first()
    return render(req, 'catatan/update.html', {
        'data': task,
    })