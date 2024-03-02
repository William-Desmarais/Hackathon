from django.shortcuts import render
import json
from dashboard.models import EasyUser

# Create your views here.
def get_user(request):
    token=request.session.get("user")

    user_exists = EasyUser.objects.filter(name=token["userinfo"]["sub"]).exists()
    if(user_exists):
        user = EasyUser.objects.get(name=token["userinfo"]["sub"])
    else:
        user = EasyUser(name=token["userinfo"]["sub"], friends='Jane Doe, Mark Smith')
        user.save()
    
    return render(request,"dashboard.html",{"sub":token["userinfo"]["sub"],"friends":user.friends})