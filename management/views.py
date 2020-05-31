from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserUpdateForm, ProfileUdateForm, ApplicationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import User

from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

from .models import *


# Create your views here.
def index(request):
    
    return render(request, 'management/index.html', {})

@login_required(login_url='login')
def loginHome(request):
    
       return render(request, 'management/home.html', {})


@login_required(login_url='login')
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUdateForm(instance=request.user.profile)
        
    context  = {
        'u_form': u_form,
        'p_form': p_form
    }
    
    return render(request, 'management/profile.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Staff'])
def apply(request):

    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        form.instance.author = request.user
        if form.is_valid():
            
            form.save()
            
            
            messages.success(request, 'Your request has been submitted!')
            return redirect('apply')
    else:
        form = ApplicationForm()
        
    context = {
        'form': form
    }
    return render(request, 'management/apply.html', context)



def approval(request):
    leave = LeaveDetail.objects.all()
    
    context = {
        'leave': leave
    }
    return render(request, 'management/approve.html', context)


def approve(request, pk):
    leave = LeaveDetail.objects.get(pk=pk)
    usersEmail = leave.author.email
    template = render_to_string('management/email_template.html', {'name': leave.author.first_name})
    send_mail(
        "Approved",
        template,
        settings.EMAIL_HOST_USER,
        [usersEmail],
        fail_silently=False
    )
    leave.delete()
    return redirect('approve')

    context = {
        'leave': leave
    }
    return render(request, 'management/approve.html', context)


def decline(request, pk):
    leave = LeaveDetail.objects.get(pk=pk)
    usersEmail = leave.author.email
    template = render_to_string('management/email_template.html', {'name': leave.author.first_name})
    send_mail(
        "Declined",
        template,
        settings.EMAIL_HOST_USER,
        [usersEmail],
        fail_silently=False
    )
    leave.delete()
    return redirect('approve')
    
    context = {
        'leave': leave
    }
    return render(request, 'management/approve.html', context)