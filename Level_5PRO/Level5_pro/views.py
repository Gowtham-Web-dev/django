from django.shortcuts import render
from Level5_pro.forms import userDetailinfo,PrfileINfo
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse


def index(request):
    return render(request,"basci.html")
@login_required
def login_out(request):
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))

def register(request):
    reg = False
    if request.method == "POST":
        profile_form = PrfileINfo(data=request.POST)
        user_form = userDetailinfo(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            print(user)
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            reg = True
        else:
            print(profile_form.errors, user_form.errors)
    else:
        profile_form = PrfileINfo()
        user_form = userDetailinfo()
    return render(request, "register.html", {"profile_form": profile_form, "user_form": user_form, "register": reg})
def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(password)

        user = authenticate(username=username,password=password)
        print(user)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("NO user")
        else:
             print("wrong user")
       
    else:
        return render(request,'login.html',{})