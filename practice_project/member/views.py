from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render

User = get_user_model()

def member_profile(request, member_pk):
    user = User.objects.get(pk=member_pk)
    context = {
        'username':user.username
    }
    return render(request, 'member/profile.html', context)