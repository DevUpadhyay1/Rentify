from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from accounts.forms import UserRegisterForm
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.contrib.auth import logout
from table.models import *
from django.conf import settings
from django.template import RequestContext
# from django.contrib.auth.models import User,auth
from django.http import HttpResponseRedirect

User = settings.AUTH_USER_MODEL

# Create your views here.
def register_view(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
                new_user = form.save()
                email = form.cleaned_data.get("email")
                messages.success(request,f"Hey {email}, your account created successfully")
                new_user = authenticate(email=form.cleaned_data['email'],
                                        password=form.cleaned_data['password1']
                )
                login(request,new_user)
                return redirect("Index")
    else:
        form = UserRegisterForm()
    
    context = {
        'form':form,
    }

    return render(request,'sign-up.html',context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect("Index")
     
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # try:
        #     user = User.objects.get(email=email)
        # except:
        #     messages.warning(request,f"User with {email} does not exist")
          
        user = authenticate(request, email=email,password=password)
            
        if user is not None:
            login(request,user)
            messages.success(request,"You are logged in")
            return redirect("Index")
        else:
            messages.warning(request,f"User does not exist,Create an account.")

    context= {}
    return render(request,"sign-in.html",context)

def logout_view(request):
    logout(request)
    messages.success(request,"You Logged Out")
    return redirect("Index")

