from __future__ import unicode_literals
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from accounts.forms import (
	RegistrationForm,
	EditProfileForm,
)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.contrib.auth import update_session_auth_hash,authenticate,login
from django.http import HttpResponse
from accounts.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from django.urls import reverse
# Create your views here.


def register(request):
	form=RegistrationForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		username = request.POST.get('username')
		password = request.POST.get('password1')
		user = authenticate(
			request = request,
			username = username,
			password = password
		)
		login(request,user)
		return redirect(reverse('home:home'))
	args={'form':form}
	return render(request,'accounts/reg_form.html',args)

#@login_required
def view_profile(request, pk=None):
	storage= messages.get_messages(request)
	if pk:
		user = User.objects.get(pk=pk)
	else:
		user= request.user

	args={'user': user, 'message': storage}
	return render(request, 'accounts/profile.html', args)

#@login_required
def edit_profile(request):
	if request.method=='POST':
		form = EditProfileForm(request.POST, instance=request.user)

		if form.is_valid():
			form.save()
			return redirect(reverse('accounts:view_profile' ))

	else:
		form = EditProfileForm(instance=request.user)
		args = {'form': form}
		return render(request,'accounts/edit_profile.html', args)

#@login_required
def change_password(request):
	if request.method=='POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)

		if form.is_valid():
			form.save()
			messages.success(request, 'Your new password has been saved.')
			update_session_auth_hash(request, form.user)
			return redirect(reverse('accounts:view_profile' ))

	else:
		form = PasswordChangeForm(user=request.user)
	args = {'form': form}
	return render(request,'accounts/change_password.html', args)


