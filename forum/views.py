from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from mahasiswa.models import Pkl
from . import models, forms
from django.contrib import messages

def index_dosen(req):
    tasks = models.Forum.objects.all()
    form_input = forms.ForumForm()

    if req.POST:
        form_input = forms.ForumForm(req.POST, req.FILES)
        if form_input.is_valid():
            form_input.instance.owner = req.user
            form_input.save()
            messages.success(req, 'Data telah ditambahkan.')
            return redirect('/forums/')

    return render(req, 'forums/index.html',{
        'data': tasks,
        'form' : form_input,
    })

def index_mhs(req):
    tasks = models.Forum.objects.all()
    form_input = forms.ForumForm()

    if req.POST:
        form_input = forms.ForumForm(req.POST, req.FILES)
        if form_input.is_valid():
            form_input.instance.owner = req.user
            form_input.save()
            messages.success(req, 'Data telah ditambahkan.')
            return redirect('/forum/')

    return render(req, 'forum/index.html',{
        'data': tasks,
        'form' : form_input,
    })

def delete_dosen(req, id):
    models.Forum.objects.filter(pk=id).delete()
    messages.success(req, 'data telah di hapus.')
    return redirect('/forums/')

def delete_mhs(req, id):
    models.Forum.objects.filter(pk=id).delete()
    messages.success(req, 'data telah di hapus.')
    return redirect('/forum/')

def detail_forum(req, id):
    forum = models.Forum.objects.filter(pk=id).first() 
    form_input = forms.PostingForm()
    form_komen = forms.KomenForm()
    form_balas = forms.BalasForm()

    if req.POST:
        form_input = forms.PostingForm(req.POST, req.FILES)
        if form_input.is_valid():
            form_input.instance.owner = req.user
            form_input.instance.forum = forum
            form_input.save()
        return redirect(f'/forums/{id}')
    # if req.POST:
    #     form_komen = forms.PostingForm(req.POST, req.FILES)
    #     if form_komen.is_valid():
    #         form_komen.instance.owner = req.user
    #         form_komen.save()
    #         return redirect('/forums/detail')

    # if req.POST:
    #     form_balas = forms.PostingForm(req.POST, req.FILES)
    #     if form_balas.is_valid():
    #         form_balas.instance.owner = req.user
    #         form_balas.save()
    #         return redirect('/forums/detail')

    return render(req, 'forums/detail.html', {
        'form': form_input,
        'form_komen': form_komen,
        'form_balas': form_balas,
        'data': forum,
    })

def detail_forum_mhs(req, id):
    forum = models.Forum.objects.filter(pk=id).first() 
    form_input = forms.PostingForm()
    form_komen = forms.KomenForm()
    form_balas = forms.BalasForm()

    if req.POST:
        form_input = forms.PostingForm(req.POST, req.FILES)
        if form_input.is_valid():
            form_input.instance.owner = req.user
            form_input.instance.forum = forum
            form_input.save()
        return redirect(f'/forum/{id}')

    return render(req, 'forum/detail.html', {
        'form': form_input,
        'form_komen': form_komen,
        'form_balas': form_balas,
        'data': forum,
    })


def delete_posting(req, id, id_posting):
    models.Posting.objects.filter(pk=id_posting).delete()
    messages.success(req, 'data telah di hapus.')
    return redirect(f'/forum/{id}')

def delete_posting_mhs(req, id, id_posting):
    models.Posting.objects.filter(pk=id_posting).delete()
    messages.success(req, 'data telah di hapus.')
    return redirect(f'/forum/{id}')
    



