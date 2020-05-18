from django.contrib import admin
from .models import TrackingForm
from django.template.loader import render_to_string
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from .forms import TrackingFormForm
from .models import TrackingForm
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse,HttpResponseRedirect, HttpResponseNotFound, HttpResponseForbidden, HttpResponseNotAllowed
from datetime import datetime
from django.template.loader import render_to_string



# Register your models here.

class TrackingFormAdmin(admin.ModelAdmin):

   change_form_template = "track/custom_button.html"

   def response_change(self, request, obj):
      if "resend" in request.POST:
         # ADVOCATE EMAIL
         form = TrackingFormForm(request.POST)
         if form.is_valid():
            from_email = settings.EMAIL_HOST_USER
            advocate_email = obj.advocate_email
            html_message = render_to_string('track/email-output.html', {'form': form.cleaned_data})

            subject = "CASA - Tracking Form Receipt"

            email = EmailMessage(subject, html_message, from_email, [advocate_email])
            email.content_subtype = "html"
            email.send()
         else:
            print(form.errors)
      return super().response_change(request, obj)

admin.site.register(TrackingForm, TrackingFormAdmin)