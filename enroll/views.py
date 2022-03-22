from django.shortcuts import redirect, render,HttpResponseRedirect
from .forms import signUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash

# Create your views here.
def signup(request):
      if request.method == 'POST':
            fm = signUpForm(request.POST)
            if fm.is_valid():
                  fm.save()
                  messages.success(request,'Your Account has been created')

      else:
            fm =signUpForm()
      return render(request,'enroll/reg.html',{'form':fm})


def signin(request):
      if not request.user.is_authenticated:
            if request.method == 'POST':
                  fm = AuthenticationForm(request=request, data =request.POST)
                  if fm.is_valid():
                        uname = fm.cleaned_data['username']
                        upass = fm.cleaned_data['password']
                        user = authenticate(username=uname, password =upass)
                        if user is not None:
                              login(request,user)
                              messages.success(request,'successfully loged in')
                              return HttpResponseRedirect('/profile/')
            else:
                  fm = AuthenticationForm()
            return render (request, 'enroll/login.html',{'form':fm})
      else:
            return HttpResponseRedirect('/profile/')


def profile(request):
      if request.user.is_authenticated:
            return render(request,'enroll/profile.html',{'name':request.user})
      else:
            return HttpResponseRedirect('/login/')

def logout_user(request):
      logout(request)
      return HttpResponseRedirect('/login/')


def change_password(request):
      if request.user.is_authenticated:
            if request.method == 'POST':
                  fm = PasswordChangeForm(user=request.user, data=request.POST)
                  if fm.is_valid():
                        fm.save()
                        update_session_auth_hash(request,fm.user)
                        return HttpResponseRedirect('/profile/')
            else:
                  fm =PasswordChangeForm(user= request.user)
            
            return render(request,'enroll/changepassword.html',{'form':fm})
      else:
            return HttpResponseRedirect('/login/')