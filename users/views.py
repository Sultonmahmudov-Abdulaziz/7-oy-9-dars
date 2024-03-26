from django.shortcuts import render,redirect
from django.views import View
from .forms import RegisterForm, LoginForm, ProfileUpdateForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages 

class RegisterView(View):

    def get(self, request):

        form=RegisterForm()
        return render(request, template_name= 'users/register.html', context={'form': form})
    



    def post(self, request):
        form=RegisterForm(request.POST)

        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            return redirect('landing_page')


        return render(request, template_name= 'users/register.html', context={'form': form})
    


class LoginView(View):
    def get(self, request):
        form=LoginForm()
        return render(request, template_name= 'users/login.html', context={'form': form})
    


    def post(self, request):
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)  

                messages.success(request,"Siz muvafaqiyatli Login qildingiz")

                return redirect('landing_page') 
        
        return render(request, template_name= 'users/login.html', context={'form': form})
    


class LogoutView(LoginRequiredMixin,View):
    def get(self, request):

        logout(request) 

        messages.success(request,"Siz muvafaqiyatli Logout qildingiz")

        return redirect('landing_page')
    

class ProfileUpdateView(LoginRequiredMixin,View):

    def get(self, request):
        form = ProfileUpdateForm(instance=request.user)


        return render(request, template_name='users/profile.html', context={'form': form})
    
    def post(self, request):
        form = ProfileUpdateForm(instance=request.user, data=request.POST)


        if form.is_valid():
            form.save()
            messages.success(request,"Profile update qilindi")
            return redirect('places:list')
        
        return render(request, template_name='users/profile.html', context={'form': form})


    

       


