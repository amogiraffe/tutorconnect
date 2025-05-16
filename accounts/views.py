from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/signup.html'
    
    def form_valid(self, form):
        user = form.save()
        messages.success(
            self.request,
            f'Account created for {user.username}! Please log in.'
        )
        return redirect('login')
    
    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"{field}: {error}")
        return super().form_invalid(form)