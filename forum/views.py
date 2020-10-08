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
        else:
            messages.danger(req, 'A problem has been occurred while submitting your data.')

    return render(req, 'forums/index.html',{
        'data': tasks,
        'form' : form_input,
    })

def delete_dosen(req, id):
    models.Forum.objects.filter(pk=id).delete()
    messages.success(req, 'data telah di hapus.')
    return redirect('/forums/')

def detail_forum(req, id):
    forum = models.Forum.objects.filter(pk=id).first() 
    chat = models.Posting.objects.all()
    form_input = forms.PostingForm()

    if req.POST:
        form_input = forms.PostingForm(req.POST, req.FILES)
        if form_input.is_valid():
            form_input.instance.owner = req.user
            form_input.save()
            return redirect('/forums/detail')

    return render(req, 'forums/detail.html', {
        'chat': chat,
        'form': form_input,
        'data': forum,
    })


# def masuk_forum(req, id):
#     data = models.Komentar.objects.all()
#     input_comment = forms.CommentForm()
#     if req.POST:
#         masuk = forms.CommentForm()


