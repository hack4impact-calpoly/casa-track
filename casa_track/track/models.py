from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now as djnow


# Create your models here.

class TrackingForm(models.Model):
   CELENA = 'C'
   HEIDI = 'H'
   GAIL = 'G'
   KATIE = 'K'
   PETE = 'P'
   MELANIE = 'M'
   NICOLE = 'N'
   SV_CHOICES = [
      (CELENA, 'Celena'),
      (HEIDI, 'Heidi'),
      (GAIL, 'Gail'),
      (KATIE, 'Katie'),
      (PETE, 'Pete'),
      (MELANIE, 'Melanie'),
      (NICOLE, 'Nicole'),
   ]
   owner = models.ForeignKey(
      User, on_delete=models.CASCADE, blank=True, null=True)
   supervisor = models.CharField(
      max_length=1, choices=SV_CHOICES, blank=False, null=False)
   child_name = models.CharField(max_length=256, blank=False)
   month = models.CharField(max_length=256, blank=False)
   hours_spent = models.CharField(max_length=256, blank=False)
   hours_education = models.CharField(max_length=256, blank=False)
   hours_on_case = models.CharField(max_length=256, blank=False)
   continuing_edu = models.CharField(max_length=256, blank=False)
   miles_driven = models.CharField(max_length=256, blank=False)
   face_advocate_sv_hours = models.CharField(max_length=256, blank=False)
   phone_advocate_sv = models.CharField(max_length=256, blank=False)
   other_volunteering = models.CharField(max_length=256, blank=False)
   created_at = models.DateTimeField(default=djnow)
   objects = models.Manager()

   def __str__(self):
      return self.child_name
