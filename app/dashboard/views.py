from django.shortcuts import render
import json

# Create your views here.
def get_user(request):
    token=request.session.get("user")

    return render(request,"dashboard.html",{"sub":token["userinfo"]["sub"]})