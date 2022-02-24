from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.views import login_required
from .forms import UserRegistrationForm,UserUpdateForm,ProfileUpdateForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f"Your Account has been create! You are now able to Log In!")
            return redirect('user-login')
    else:
        form = UserRegistrationForm()
    return render(request,'user/register.html',{'form':form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, 
                                        instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,"Your Account updated Successfully!")
            return redirect('user-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request,'user/profile.html',context)

