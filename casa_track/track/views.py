from django.shortcuts import render, redirect
from .forms import TrackingFormForm
from .models import TrackingForm
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden, HttpResponseNotAllowed
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
# Create your views here.


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

"""
   Uses Django emailing service: https://docs.djangoproject.com/en/2.1/topics/email/
"""
def tracking(request):
    if request.method == "POST":
        form = TrackingFormForm(request.POST)
        if form.is_valid():
            form.save()
            supervisor = form.cleaned_data['supervisor']
            super_email = map_to_supervisor(supervisor)
            advocate = form.cleaned_data['advocate']
            subject = "New tracking form from " + advocate
            from_email = settings.EMAIL_HOST_USER
            message = form.cleaned_data['supervisor']
            html_message = get_html_message(form)
            try:
                send_mail(subject, message, from_email, [super_email], html_message=html_message, fail_silently=False)
            except:
                return HttpResponse("Didn't work.")
            return redirect('/')
        else:
            print(form.errors)
    else:
        form = TrackingFormForm()
    return render(request, 'track/tracking.html', {'form': form})

"""
    <h2 class="h2-home">Tracking Form</h2>
            <h3 class="label-control">Supervisor</h3>
            <p name='supervisor' class="form-control" id="exampleFormControlSelect1">{{ t_form.supervisor }}</p>
            <h3 class="label-control">Child's Name</h3>
            <p name='child_name' class="form-control" value="">{{ t_form.child_name }}</p>
            <h3 class="label-control">Month, Year</h3>
            <p name='month' class="form-control" id='month'>{{ t_form.month }}</p>
            <h3 class="label-control">How many hours did you spend with your CASA child/ren this month?</h3>
            <p name='hours_spent' class="form-control" value="">{{ t_form.hours_spent }}</p>
            <h3 class="label-control">How many hours did you spend on this child/ren's education this month?</h3>
            <p name='hours_education' class="form-control" id="hours_education" value="">{{ t_form.hours_education }}</p>
            <h3 class="label-control">How many additional hours did you spend on your case this month?</h3>
            <p name='hours_on_case' class="form-control" id="hours_on_case" value="">{{ t_form.continuing_edu }}</p>
            <h3 class="label-control">What continuing education did you do this month?</h3>
            <p name='continuing_edu' class="form-control" id="continuing_edu" value="">{{ t_form.miles_driven }}</p>
        <div class="form-group">
            <h3 class="label-control">How many miles did you drive for CASA activities this month?</h3>
            <p name='miles_driven' class="form-control" id="miles_driven" value="">{{ t_form.face_advocate_sv_hours }}</p>
            <h3 class="label-control">Did you have a face-to-face meeting with your Advocate Supervisor this month?
                (State in hours)</h3>
            <p name='face_advocate_sv_hours' class="form-control" id="face_advocate_sv_hours" value="">{{ t_form.phone_advocate_sv }}</p>
            <h3 class="label-control">Did you have phone or email contact with your Advocate Supervisor this month?
            <p name='phone_advocate_sv' class="form-control" id="phone_advocate_sv" value="">{{ t_form.other_volunteering }}</p>
            <h3 class="label-control">Other volunteering for CASA this month?</h3>
            <p name='other_volunteering' class="form-control" id="other_volunteering" value="">{{ t_form.created_at }}</p>
    <div class="col-12">
        <div class="form-group">
            <h3 class="label-control">Signature</h3>
            {{ form.signature }}
"""

def get_html_message(form): # all form data passed
    return """<head>
            <style>
                p {
                    color: black;
                    font-weight: bold;
                }
                span {
                    color: black;
                    font-weight: normal;
                }
            </style>
        </head>
        <body>
        <h3>Form from CASA Track</h3>
        <p>Supervisor: <span>""" + dict(form.fields['supervisor'].choices)[form.cleaned_data['supervisor']] + """</span></p>
        <p>Your Name: """ + form.cleaned_data['advocate'] + """</p>
        <p>Child's Name: """ + form.cleaned_data['child_name'] + """</p>
        <p>Month, Year: """ + form.cleaned_data['month'] + """</p>
        <p>Hours Spent: """ + form.cleaned_data['hours_education'] + """</p>
        <p>Additional Hours Spent on Case: """ + form.cleaned_data['hours_on_case'] + """</p>
        <p>Continuing Education: """ + form.cleaned_data['continuing_edu'] + """</p>
        <p>Miles Driven: """ + form.cleaned_data['miles_driven'] + """</p>
        <p>Face-to-face Hours: """ + form.cleaned_data['face_advocate_sv_hours'] + """</p>
        <p>Phone: """ + form.cleaned_data['phone_advocate_sv'] + """</p>
        <p>Other volunteering: """ + form.cleaned_data['other_volunteering'] + """</p>
        </body>"""

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
