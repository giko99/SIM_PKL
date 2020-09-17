from django.shortcuts import render
from django.contrib.auth import get_user_model

def index(req):

    User = get_user_model()
    return render(req, 'home/index.html', {
        'd': User,
    })

