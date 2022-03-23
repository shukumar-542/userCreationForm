from email import message
from django.shortcuts import render,HttpResponseRedirect
from .forms import editAdminForm, signUpForm,editUserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.models import User

# Create your views here.
def home(request):
      return render(request, 'enroll/home.html')
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
            if request.method == 'POST':
                  if request.user.is_superuser == True:
                        fm = editAdminForm(request.POST, instance= request.user)
                        users = User.objects.all()
                  else:
                        fm= editUserForm(request.POST,instance=request.user)
                        users =None
                  if fm.is_valid():
                        messages.success(request, 'your account has been updated')
                        fm.save()
            else:
                  if request.user.is_superuser == True:
                        fm = editAdminForm(instance =request.user)
                        users = User.objects.all()
                  else:
                        fm= editUserForm(instance=request.user)
                        users =None
            return render(request,'enroll/profile.html',{'name':request.user,'form':fm, 'users':users})
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


def userdetail(request,id):
      if request.user.is_authenticated:
            pi= User.objects.get(pk=id)
            fm = editAdminForm(instance=pi)
            
            return render(request, 'enroll/userdetail.html',{'form':fm})
      else:
            return HttpResponseRedirect('/login/')