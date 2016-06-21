from django.shortcuts import render
from django.http import Http404

from .models import User


def index(request):
    userDB = User.objects.all()
    return render(request, 'users/index.html', {
        'user': userDB,
    })


def user_detail(request, id):
    try:
        userDB = User.objects.get(id=id)
    except User.DoesNotExist:
        raise Http404('No such user.')
    return render(request, 'users/user_detail.html', {
        'user': userDB,
    })
