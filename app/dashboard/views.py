from django.shortcuts import render,redirect
import json
from django.http import HttpResponse
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

def add_friend(request):
    if request.method == 'POST':
        user_sub = request.session.get("user")["userinfo"]["sub"]
        new_friend = request.POST.get("friendName")

        # Retrieve the user
        user = EasyUser.objects.get(name=user_sub)
        
        # Assuming friends are stored as a JSON-encoded list
        friends_list = user.friends.split(',')
        if new_friend not in friends_list:
            user.friends += f",{new_friend}"
            user.save()

        return redirect('/dashboard/user/')

    else:
        # If not a POST request, just show the form or redirect as needed
        return HttpResponse("Method not allowed", status=405)