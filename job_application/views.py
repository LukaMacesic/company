from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage


def index(request):
    return render(request, "index.html",)


def services(requests):
    return render(requests, "services.html")

def about(requests):
    return render(requests, "about.html")


def contact(requests):
    if requests.method == "POST":
        form = ApplicationForm(requests.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            Form.objects.create(first_name=first_name, last_name=last_name,
                                email=email, message=message)

            message_body = f"Thank you for your submission {first_name}. " \
                           f"Here are your data: \n{first_name}\n{last_name}" \
                           f"Thank you"
            email_message = EmailMessage("Form submission confirmation",
                                         message_body, to=[email])
            email_message.send()

            messages.success(requests, "Form was submitted successfully")
    return render(requests, "contact.html")
