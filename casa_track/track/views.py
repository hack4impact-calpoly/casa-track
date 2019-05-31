from django.shortcuts import render, redirect
from .forms import TrackingFormForm
from .models import TrackingForm
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden, HttpResponseNotAllowed
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError, EmailMessage

from weasyprint import HTML
from django.template.loader import render_to_string
from datetime import datetime


def home(request):
    if request.user.is_superuser:
        t_forms = TrackingForm.objects.all().order_by('-created_at')
        context = {
            't_forms': t_forms,
            'admin': True,
        }
        return render(request, 'track/user_admin.html', context)
    else:
        return render(request, 'track/home.html')


""" Uses Django emailing service: https://docs.djangoproject.com/en/2.1/topics/email/ """


def tracking(request):
    if request.method == "POST":
        form = TrackingFormForm(request.POST)
        if form.is_valid():
            form.save()
            

            supervisor = form.cleaned_data['supervisor']
            super_email = map_to_supervisor(supervisor)
            advocate = form.cleaned_data['advocate']
            subject = "[CASA Track] New Tracking Form from " + advocate
            from_email = settings.EMAIL_HOST_USER

            form.cleaned_data['supervisor'] = dict(form.fields['supervisor'].choices)[supervisor]
            form.cleaned_data['signature_date'] = form.cleaned_data['signature_date'].strftime("%d %b %Y")
            html_message = render_to_string('track/email-output.html', {'form': form.cleaned_data})

            email = EmailMessage(subject, html_message,
                                 from_email, [super_email])
            pdf_generation(request, form.cleaned_data)
            email.attach_file('report.pdf')
            email.content_subtype = "html"
            email.send()

            return redirect('/') # TODO send user to a "submitted" page
        else:
            print(form.errors)
    else:
        form = TrackingFormForm()
    return render(request, 'track/tracking.html', {'form': form})


def pdf_generation(request, form_info):
    html_string = render_to_string('track/pdf-output.html', {'form': form_info})
    HTML(string=html_string, base_url=request.build_absolute_uri()).write_pdf(target='report.pdf')


def map_to_supervisor(supervisor_char):
    if supervisor_char == 'C':
        return 'h4icptest@gmail.com'
    if supervisor_char == 'H':
        return 'h4icptest@gmail.com'
    if supervisor_char == 'G':
        return 'h4icptest@gmail.com'
    if supervisor_char == 'K':
        return 'h4icptest@gmail.com'
    if supervisor_char == 'P':
        return 'h4icptest@gmail.com'
    if supervisor_char == 'M':
        return 'h4icptest@gmail.com'
    if supervisor_char == 'N':
        return 'h4icptest@gmail.com'


def delete_form(request):
    if request.method == 'POST':
        item_id = int(request.POST.get('item_id'))
        item = TrackingForm.objects.get(id=item_id)
        if request.user.is_superuser:
            item.delete()
            return redirect('/')
        else:
            print("fail")
            return HttpResponseForbidden()
    else:
        return HttpResponseNotAllowed(request)
