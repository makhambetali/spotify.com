from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from .forms import NewUserForm
from django.contrib.auth.views import LoginView
from django.contrib import messages
    

error_messages = {
}

@csrf_exempt
def register_request(request):
    error_messages = {}
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')  
        for i in form.errors:
            error_messages[i] = form.errors[i]
                
       
    form = NewUserForm()
    return render(request, 'users/register.html', {'form':form,'error_messages':error_messages})


class CustomLoginView(LoginView):
    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)

    def get_success_url(self):
        return '/'  