from django.shortcuts import render,redirect
from accounts.forms import (
                            RegistrationForm,
                            EditProfileForm,
                            )
# from django.urls import reverse
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.

def home_view(request):
    print(request)
    args = {'name':request.user }
    return render(request, 'accounts/home.html',args)

def login(request):
    args = { }
    return render(request, 'accounts/login.html',args)

def profile(request):
    args={'name':request.user}
    return render(request, 'accounts/profile.html',args)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            # return redirect(reverse('accounts:home'))
            return render(request, 'accounts/home.html')
        else:
            return render(request,'<h1> Form Invalid</h1>')
    else:
        form = RegistrationForm()
        args = {'form':form}
        return render(request, 'accounts/register.html',args)

def profile_edit(request):
    if request.method=='POST':
        form=EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/accounts/profile')
    else:
        print("Its a Get")
        form=EditProfileForm(instance=request.user)
        print(form)
        args={'form':form}
        return render(request, 'accounts/edit-profile.html',args)

def change_password(request):
    if request.method == 'POST':
        form=PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('/accounts/profile')
        else:
            return redirect('/accounts/change-password')
    else:
        form=PasswordChangeForm(user=request.user)
        #Important point to be noted look at above line its not
        #instance=request.user but user=request.user different from other user
        #defined forms.
        args={'form':form}
        return render(request, 'accounts/change-password.html',args)
