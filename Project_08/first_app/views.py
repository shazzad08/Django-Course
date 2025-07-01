from django.shortcuts import render,redirect
from .forms import RegisterForm,ChangeUserData
from django .contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate, login,logout,update_session_auth_hash
# Create your views here.

def home(request):
     return render(request,'./home.html')


def signup(request):
    if not request.user.is_authenticated:
          if request.method =='POST':
               form = RegisterForm(request.POST)
               if form.is_valid():
                    messages.success(request,'Account Created Successfully')
                    form.save()
                    print(form.cleaned_data)
          else:
                    form = RegisterForm()

          return render(request,'signup.html',{'form':form})
    else:
         return redirect('profile')
    

def user_login(request):
     if not request.user.is_authenticated:
          if request.method == 'POST':
               form = AuthenticationForm(request=request,data=request.POST)
               if form.is_valid():
                    name = form.cleaned_data['username']
                    user_pass= form.cleaned_data['password']

                    user = authenticate(username = name, password = user_pass) #check krtesi user database a ase kina


                    if user is not None:
                         login(request,user)
                         return redirect('profile')
          else:
               form= AuthenticationForm()

          return render(request,'./login.html',{'form':form})
     else:
          return redirect('profile')
          


def profile(request):
     
     if  request.user.is_authenticated:
          if request.method =='POST':
               form = ChangeUserData(request.POST, instance = request.user)
               if form.is_valid():
                    messages.success(request,'Account Updated Successfully')
                    form.save()
                  
          else:
                    form = ChangeUserData(instance = request.user)

          return render(request,'./profile.html',{'form':form})
     else:
         return redirect('signup')


def user_logout(request):
     logout(request)
     return redirect('user_login')

def pass_change(request):
     if request.user.is_authenticated:
          if request.method == 'POST':
               form = PasswordChangeForm (user = request.user, data = request.POST) # old password require if i use PasswordChangeForm
               if form.is_valid():
                    form.save()
                    update_session_auth_hash(request, form.user) # password upddate krbe
                    return redirect('profile')
          else:
               form = PasswordChangeForm(user = request.user)
          return render(request,'./password_change.html',{'form':form})

def pass_change2(request):
     if request.user.is_authenticated:
          if request.method == 'POST':
               form = SetPasswordForm(user = request.user, data = request.POST) #old password  cara parword change krte SetPasswordForm use kri
               if form.is_valid():
                    form.save()
                    update_session_auth_hash(request, form.user) # password upddate krbe
                    return redirect('profile')
          else:
               form = SetPasswordForm(user = request.user)
          return render(request,'./password_change.html',{'form':form})

def change_user_data(request):
   
     if  request.user.is_authenticated:
          if request.method =='POST':
               form = ChangeUserData(request.POST, instance = request.user)
               if form.is_valid():
                    messages.success(request,'Account Updated Successfully')
                    form.save()
                  
          else:
                    form = ChangeUserData()

          return render(request,'./profile.html',{'form':form})
     else:
         return redirect('signup')