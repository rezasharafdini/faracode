from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, HttpResponse, redirect

from django.views.generic import TemplateView, FormView, View
from . import forms
from .models import Portfolio


class HomeView(View):
    def get(self, request):
        portfolio = Portfolio.objects.filter(is_publish=True)
        form = forms.SendEmailForm()

        return render(request, 'home/index.html', {'portfolio': portfolio, 'form': form})

    def post(self, request):
        form = forms.SendEmailForm()
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            send_mail(subject + '/' + name, message + '/' + email, 'email', ['email'], fail_silently=False)
            return redirect('home_app:home')
        messages.error(request, 'please enter correct information.')
        return render(request, 'home/index.html', {'form': form})
