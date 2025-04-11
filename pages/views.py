from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm

# Create your views here.
def testing_view(request):
    return render(request, "pages/test.html")

def home_view(request):
    return render(request, "pages/home.html")

def about_view(request):
    return render(request, "pages/about.html")

def login_view(request):
    return render(request, "pages/login.html")

def contact_view(request):
    if request.method == "POST":
        # validate and send email
        form = ContactForm(request.POST)
        if form.is_valid():
            print("valid data")

            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data ["message"]

            message_body = message_body = f"This is an email from your portfolio\nName:{name}\nEmail:{email}\nMessage:\n{message}"

            send_mail(
                "Email from Portfolio",
                message_body,
                email,
                ['samsontherealtor@gmail.com']
            )

        else:
            print("Invalid form data")
    
    else:
        #display the page
        form = ContactForm()

    return render(request,"pages/contact.html", {"form": form})