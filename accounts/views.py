from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User
from .forms import UserCreationForm, UserAccountForm
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

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
        return HttpResponseRedirect(reverse('account:display_account', ))
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



