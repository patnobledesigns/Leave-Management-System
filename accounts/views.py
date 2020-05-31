from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from management.decorators import unauthenticated_user, allowed_users, admin_only
from management.forms import Userprofileform, CreateUserForm

# Create your views here.
def loginPage(request):
    # login Validation
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username Or Password is Incorrect')

    
    return render(request, 'accounts/login.html')


def logoutpage(request):
    logout(request)
    return redirect('homepage')


@allowed_users(allowed_roles=['Manager'])
def registerpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:    
        if request.method == 'POST':
            c_form = CreateUserForm(request.POST)
            p_form = Userprofileform(request.POST, request.FILES)
            
            if c_form.is_valid() and p_form.is_valid():
                user = c_form.save()
                
                profile = p_form.save(commit=False)
                profile.user = user
                
                p_form.save()
                
                username = c_form.cleaned_data.get('username')
                messages.success(request, f'Account was created for {username}')
                return redirect('home')
        else:
            c_form = CreateUserForm()
            p_form = Userprofileform()

        context={
            'c_form': c_form,
            'p_form': p_form,
        }
        return render(request, 'accounts/signup.html', context)
