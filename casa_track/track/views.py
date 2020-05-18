from django.shortcuts import render, redirect,get_object_or_404
from .forms import TrackingFormForm, PartialTrackingFormForm
from .models import TrackingForm
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden, HttpResponseNotAllowed
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError, EmailMessage

from weasyprint import HTML
from django.template.loader import render_to_string

from datetime import datetime

from django.contrib.auth.models import User


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
    users = User.objects.all()
    if request.method == "POST":
        form = TrackingFormForm(request.POST)
        if form.is_valid():
            obj = form.save()
            print(obj.id)
            super_email = map_to_supervisor(form.cleaned_data['supervisor'])
            from_email = settings.EMAIL_HOST_USER
            advocate = form.cleaned_data['advocate']
            form.cleaned_data['signature_date'] = form.cleaned_data['signature_date'].strftime("%d %b %Y")

            # SUPERVISOR EMAIL
            subject = "[ACTION NEEDED: CASA Track] New Tracking Form from " + advocate + ", please finish signing"

            email = EmailMessage(subject, 'A new tracking form has been received. FINISH SIGNING HERE: https://casa-track.herokuapp.com/supervisor_confirm/' + str(obj.id),
                                 from_email, [super_email])
            pdf_generation(request, form.cleaned_data)
            email.attach_file('report.pdf')
            email.send()

            # ADVOCATE EMAIL
            advocate_email = form.cleaned_data['advocate_email']
            html_message = render_to_string('track/email-output.html', {'form': form.cleaned_data})

            subject = "CASA - Tracking Form Receipt"

            email = EmailMessage(subject, html_message, from_email, [advocate_email])
            email.content_subtype = "html"
            email.send()

            return redirect('success/')
        else:
            print(form.errors)
    else:
        form = TrackingFormForm()
    return render(request, 'track/tracking.html', {
        'form': form, 
        'users': users,
        })


def pdf_generation(request, form_info):
    html_string = render_to_string('track/pdf-output.html', {'form': form_info})
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    html.write_pdf(target='report.pdf')


def map_to_supervisor(supervisor_username):
    users = User.objects.all()
    for user in users:
        if str(user) == str(supervisor_username):
            return user.email


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

def success(request):
    print("YAY")
    return render(request, 'track/success.html')

def supervisor_success(request):
    print("YAY")
    return render(request, 'track/supervisor-success.html')

# PDF after supervisor signature
def pdf_generation_supervisor(request, form_info, t_form_info):
    html_string = render_to_string('track/pdf-output.html', {
        'form': form_info,
        't_form': t_form_info,
    })
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    html.write_pdf(target='report.pdf')

def supervisor_confirm(request, pk):
    current_tf = get_object_or_404(TrackingForm, pk=pk)
    if request.method == "POST":
        form = TrackingFormForm(instance=current_tf)
        t_form = PartialTrackingFormForm(request.POST, instance=current_tf)
        t_form.save()
        print('success')
        super_email = map_to_supervisor(current_tf.supervisor)
        print(super_email)
        from_email = settings.EMAIL_HOST_USER
        advocate = current_tf.advocate
        current_tf.signature_date = current_tf.signature_date.strftime("%d %b %Y")
        t_form.cleaned_data['supervisor_signature_date'] = t_form.cleaned_data['supervisor_signature_date'].strftime("%d %b %Y")
    
        # SUPERVISOR EMAIL
        subject = "[CASA Track] Supervisor Signature Confirmation for " + advocate

        email = EmailMessage(subject, 'Tracking form successfully signed by supervisor.',
                                from_email, [super_email])
        pdf_generation_supervisor(request, current_tf, t_form.cleaned_data)
        email.attach_file('report.pdf')
        email.send()
        return redirect('/supervisor-success')
    else:
        form = TrackingFormForm(instance=current_tf)
        t_form = PartialTrackingFormForm(instance=current_tf)
    
    context = {
        't_form:' : t_form,
        'tf': current_tf,
    }
    return render(request, 'track/supervisor-sign.html', context)

