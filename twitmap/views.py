from django.shortcuts import render

from .forms import SignUpForm
from django.contrib.auth.decorators import login_required


def login(request):
    return render(request, "registration/sign_up_login.html")


@login_required
def home(request):

    title = "Username: %s" % str(request.user)

    #add a form
    form = SignUpForm(request.POST or None)

    context = {
        "title": title,
        "form": form
    }

    if form.is_valid():
        #form.save()
        instance = form.save(commit=False)

        full_name = form.cleaned_data.get('full_name')
        if not full_name:
            full_name = 'New full name'

        instance.full_name = full_name
        #if not instance.full_name:
        #    instance.full_name = 'Mark'
        instance.save()
        context = {
            "title": "Thank you"
        }

    return render(request, "home.html", context)
