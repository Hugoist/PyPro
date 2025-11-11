from django.contrib import messages
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import UserProfile
from .forms import RegistrationForm, UserProfileForm, CustomPasswordChangeForm


def register_view(request):
    """Register a new user"""
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            messages.success(request, 'Реєстрація успішна')
            return redirect('profile', username=user.username)
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def edit_profile_view(request, username):
    """Edit profile page"""
    profile = get_object_or_404(UserProfile, user__username=username)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Профіль оновлено")
            return redirect('profile', username=username)
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'edit_profile.html', {'form': form})

@login_required
def change_password_view(request, username):
    """Change password view"""
    profile = get_object_or_404(UserProfile, user__username=username)
    user = profile.user

    if request.method == 'POST':
        form = CustomPasswordChangeForm(user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Пароль змінено")
            return redirect('profile', username=username)
    else:
        form = CustomPasswordChangeForm(user)
    return render(request, 'change_password.html', {'form': form})

@login_required
def profile_view(request, username):
    user = get_object_or_404(UserProfile, user__username=username)
    # profile = user.profile
    return render(request, 'profile.html', {'profile': user})