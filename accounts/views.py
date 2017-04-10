from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.models import User
from .forms import UserCreationForm, UserAccountForm
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from social_django.models import UserSocialAuth
from django.core.exceptions import ObjectDoesNotExist

from .models import Account


class AccountView(LoginRequiredMixin, generic.DetailView):
    template_name = 'accounts/account.html'
    model = User()

    def get_object(self, queryset=None):
        return User


class AccountUpdate(LoginRequiredMixin, generic.UpdateView):
    fields = ['display_name']
    template_name_suffix = '_update_form'
    template_name = 'accounts/account_update_form.html'
    success_url = reverse_lazy('display_account')

    def get_object(self):
        return get_object_or_404(Account, user=self.request.user)


# Register User
def signup(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('display_account', ))
    if request.method == 'POST':
        uf = UserCreationForm(request.POST, prefix='user')
        uaf = UserAccountForm(request.POST, prefix='useraccount')
        if uf.is_valid() * uaf.is_valid():
            user = uf.save()
            useraccount = uaf.save(commit=False)
            useraccount.user = user
            uaf.save()
            return HttpResponseRedirect(reverse('display_account', ))
    else:
        uf = UserCreationForm(prefix='user')
        uaf = UserAccountForm(prefix='useraccount')
    return render(request, 'accounts/signup.html', {"userform": uf, "useraccountform": uaf})


@login_required
def settings(request):
    user = request.user

    try:
        github_login = user.social_auth.get(provider='github')
    except UserSocialAuth.DoesNotExist:
        github_login = None
    try:
        twitter_login = user.social_auth.get(provider='twitter')
    except UserSocialAuth.DoesNotExist:
        twitter_login = None
    try:
        facebook_login = user.social_auth.get(provider='facebook')
    except UserSocialAuth.DoesNotExist:
        facebook_login = None

    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

    return render(request, 'accounts/settings.html', {
        'github_login': github_login,
        'twitter_login': twitter_login,
        'facebook_login': facebook_login,
        'can_disconnect': can_disconnect
    })


@login_required
def password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'accounts/password.html', {'form': form})

