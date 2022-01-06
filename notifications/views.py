from django.shortcuts import render, redirect
from .models import Email
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import EmailUpdateForm, SendEmailForm
from django.contrib.auth.decorators import user_passes_test
from django.conf import settings
from django.core.mail import send_mail


def AddEmailFunc(request):
    if request.method == 'POST':
        form = EmailUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your email address has been added! ')
            return HttpResponseRedirect(request.path_info)
    else:
        form = EmailUpdateForm()
    return render(request, 'notifications/notifications.html', {'form': form})


def AdminNotify(request):
    if request.user.is_superuser:  # make sure that the person accessing this page is a superuser
        emails = Email.objects.all()
        if request.method == 'POST':
            form = SendEmailForm(request.POST)
            if form.is_valid():  # send emails
                recipient_list = [e.email for e in emails]
                subject = request.POST['subject']
                message = request.POST['message']
                email_from = settings.EMAIL_HOST_USER
                send_mail(subject, message, email_from, recipient_list)
                messages.success(request, 'Notifications sent succesfully!')
                return redirect("/admin/")
            else:
                return HttpResponseRedirect("Form is not valid")
        else:
            form = SendEmailForm(initial={'subject': "New Post on Eliyahu's Blog!",
                                          'message': """Eliyahu posted a new post: Most recent post title.
You can read it here: https://eliyahumasinter.com/posts/some post number."""})
            return render(request, 'notifications/adminnotify.html', {'form': form, 'emails': emails})

    else:
        return redirect("/admin/")
