from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now as djnow


# Create your models here.

class TrackingForm(models.Model):
   owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
   advocate = models.CharField(max_length=256, blank=False)
   advocate_email = models.EmailField(max_length=254, blank=False)
   supervisor = models.CharField(max_length=256, blank=False, null=False)
   child_name = models.CharField(max_length=256, blank=False)
   month = models.CharField(max_length=256, blank=False) # doesn't like being a DateTimeField
   hours_spent = models.FloatField(blank=False)
   hours_education = models.FloatField(blank=False)
   hours_on_case = models.FloatField(blank=False)
   # the voice
   the_voice = models.CharField(max_length=256, blank=False, null=False)
   continuing_edu = models.CharField(max_length=256, blank=False)
   miles_driven = models.FloatField(blank=False)
   # yes/no field
   face_advocate_sv_hours = models.CharField(max_length=256, blank=False, null=False)
   #yes/no field
   phone_advocate_sv = models.CharField(max_length=256, blank=False, null=False)
   casa_volunteering = models.CharField(max_length=256, blank=False, default=djnow)
   other_volunteering = models.CharField(max_length=256, blank=False)
   
   esignature = models.TextField(blank=True)

   signature_date = models.DateTimeField(default=djnow, blank=True)
   created_at = models.DateTimeField(default=djnow)
   objects = models.Manager()

   def __str__(self):
      return self.child_name
