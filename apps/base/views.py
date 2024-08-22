from django.shortcuts import render, redirect
from .models import *
from apps.telegram_bot.views import get_text

# Create your views here.
def index(request):
    return render(request, "base/index.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        number = request.POST.get('number')
        email = request.POST.get('email')
        cause = request.POST.get('cause')
        message = request.POST.get('message')
        Application.objects.create(name=name, number=number, email=email, cause=cause, message=message )
        get_text(f"""Поступила новая заявка
                 
                от пользователя: {name}
                {number}
                {email}
                {cause}
                {message}
""")
        return redirect("contact")
    return render(request, "base/contact.html")
