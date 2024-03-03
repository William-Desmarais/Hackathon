from django.shortcuts import render,redirect
import json
from django.http import HttpResponse
from dashboard.models import EasyUser
import re
from django.http import HttpResponseRedirect

# Create your views here.
def get_user(request):
    token=request.session.get("user")

    user_exists = EasyUser.objects.filter(name=token["userinfo"]["sub"]).exists()
    if(user_exists):
        user = EasyUser.objects.get(name=token["userinfo"]["sub"])
        user.real_name=token["userinfo"]["nickname"]
        user.email=token["userinfo"]["email"]
        user.save()
    else:
        user = EasyUser(name=token["userinfo"]["sub"], friends='',real_name=token["userinfo"]["nickname"],email=token["userinfo"]["email"])
        user.save()

    users = EasyUser.objects.all()

    friends_list = [friend.strip() for friend in user.friends.split(',')]
    
    friends_objects = []

    if user.goal_score > 0:
        progress = int((user.score / user.goal_score) * 100)
    else:
        progress = 0  # or some default value

    # Iterate over each name in the friends_list
    for name in friends_list:
        # Use filter to find users with a name that matches (case-insensitive)
        matched_users = EasyUser.objects.filter(name__iexact=name)
        # Extend the friends_objects list with the matched users
        friends_objects.extend(matched_users)
    
    return render(request,"mainpage.html",{"sub":token["userinfo"]["sub"],"friends":friends_objects,"score":user.score,"goal_score":user.goal_score,"users":users,"progress":progress})

'''
def add_friend(request):
    if request.method == 'POST':
        user_sub = request.session.get("user")["userinfo"]["sub"]
        new_friend = request.POST.get("friendName")

        # Retrieve the user
        user = EasyUser.objects.get(name=user_sub)
        
        # Assuming friends are stored as a JSON-encoded list
        #friends_list = user.friends.split(',')
        friends_list = [friend.strip() for friend in user.friends.split(',')]
        
        if new_friend not in friends_list:
            #user.friends += f",{new_friend}"
            friends_list.append(new_friend)  # Remove the friend's name from the list
            user.friends = ','.join(friends_list)  # Join the list back into a string
            user.save()

        return redirect('/dashboard/user/')

    else:
        # If not a POST request, just show the form or redirect as needed
        return HttpResponse("Method not allowed", status=405)
    
def del_friend(request):
    if request.method == 'POST':
        user_sub = request.session.get("user")["userinfo"]["sub"]
        new_friend = request.POST.get("friendName")

        # Retrieve the user
        user = EasyUser.objects.get(name=user_sub)
        
        # Assuming friends are stored as a JSON-encoded list
        friends_list = user.friends.split(',')
        if new_friend in friends_list:
            friends_list.remove(new_friend)  # Remove the friend's name from the list
            user.friends = ','.join(friends_list)  # Join the list back into a string
            user.save()
        else:
            return HttpResponse("Friend name don't exist", status=405)

        return redirect('/dashboard/user/')

    else:
        # If not a POST request, just show the form or redirect as needed
        return HttpResponse("Method not allowed", status=405)
'''    
def add_points(request):
    if request.method == 'POST':
        user_sub = request.session.get("user")["userinfo"]["sub"]

        score = request.POST.get("score")

        # Retrieve the user
        user = EasyUser.objects.get(name=user_sub)
        
        user.score+=int(score)
        user.save()
        
        return redirect('/dashboard/user/')

    else:
        # If not a POST request, just show the form or redirect as needed
        return HttpResponse("Method not allowed", status=405)
    
def clear_points(request):
    if request.method == 'POST':
        user_sub = request.session.get("user")["userinfo"]["sub"]

        # Retrieve the user
        user = EasyUser.objects.get(name=user_sub)
        
        user.score=0
        user.save()
        
        return redirect('/dashboard/user/')

    else:
        # If not a POST request, just show the form or redirect as needed
        return HttpResponse("Method not allowed", status=405)
    
def set_goal(request):
    if request.method == 'POST':
        user_sub = request.session.get("user")["userinfo"]["sub"]
        goal = request.POST.get("goal")

        # Retrieve the user
        user = EasyUser.objects.get(name=user_sub)
        
        user.goal_score=goal
        user.save()
        
        return redirect('/dashboard/user/')

    else:
        # If not a POST request, just show the form or redirect as needed
        return HttpResponse("Method not allowed", status=405)
    


def add_friend(request):
    if request.method == 'POST':
        user_sub = request.session.get("user")["userinfo"]["sub"]
        user_name = request.POST.get("user_name")

        # Retrieve the user
        user = EasyUser.objects.get(name=user_sub)
        
        friends_list = [friend.strip() for friend in user.friends.split(',')]
        
        if user_name not in friends_list:
            #user.friends += f",{new_friend}"
            friends_list.append(user_name)  # Remove the friend's name from the list
            user.friends = ','.join(friends_list)  # Join the list back into a string
            user.save()
        previous_url = request.META.get('HTTP_REFERER', '/')
        return HttpResponseRedirect(previous_url)
        #return redirect('/dashboard/user/')

    else:
        # If not a POST request, just show the form or redirect as needed
        return HttpResponse("Method not allowed", status=405)
    
def del_friend(request):
    if request.method == 'POST':
        user_sub = request.session.get("user")["userinfo"]["sub"]
        user_name = request.POST.get("user_name")

        # Retrieve the user
        user = EasyUser.objects.get(name=user_sub)
        
        friends_list = [friend.strip() for friend in user.friends.split(',')]
        
        if user_name in friends_list:
            #user.friends += f",{new_friend}"
            friends_list.remove(user_name)  # Remove the friend's name from the list
            user.friends = ','.join(friends_list)  # Join the list back into a string
            user.save()
        else:
            return HttpResponse("This should not happen, but Friend name don't exist, friendname: "+user_name, status=405)
        previous_url = request.META.get('HTTP_REFERER', '/')
        return HttpResponseRedirect(previous_url)
        #return redirect('/dashboard/user/')

    else:
        # If not a POST request, just show the form or redirect as needed
        return HttpResponse("Method not allowed", status=405)
    
def about(request):
    return render(request,"ourTeam.html")

def setting(request):
    token=request.session.get("user")

    user_exists = EasyUser.objects.filter(name=token["userinfo"]["sub"]).exists()
    if(user_exists):
        user = EasyUser.objects.get(name=token["userinfo"]["sub"])

    return render(request,"settings page.html",{"user":user})

def friend(request):
    token=request.session.get("user")

    user_exists = EasyUser.objects.filter(name=token["userinfo"]["sub"]).exists()
    if(user_exists):
        user = EasyUser.objects.get(name=token["userinfo"]["sub"])

    users = EasyUser.objects.all()

    friends_list = [friend.strip() for friend in user.friends.split(',')]
    
    friends_objects = []

    left_users=[]

    # Iterate over each name in the friends_list
    for name in friends_list:
        # Use filter to find users with a name that matches (case-insensitive)
        matched_users = EasyUser.objects.filter(name__iexact=name)
        # Extend the friends_objects list with the matched users
        friends_objects.extend(matched_users)
        
    for user in users:
        if (user not in friends_objects):
            left_users.append(user)
    return render(request,"ManageFriend.html",{"user":user,"friends":friends_objects,"users":left_users})