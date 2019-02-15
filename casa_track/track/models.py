from django.db import models
from django.contrib.auth.models import User

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
      (HEIDI, 'Vacation (paid)'),
      (GAIL, 'Unpaid Leave'),
      (KATIE, 'Katie'),
      (PETE, 'Pete'),
      (MELANIE, 'Melanie'),
      (NICOLE, 'Nicole'),
   ]
   owner = models.ForeignKey(
      User, on_delete=models.CASCADE, blank=True, null=True)
   supervisor = models.CharField(
      max_length=2, choices=SV_CHOICES, blank=False, null=False)
   child_name = models.CharField(max_length=256, blank=False)
   month_year = models.DateTimeField(blank=False, null=False)
   hours_spent = models.IntegerField(blank=False)
   hours_education = models.IntegerField(blank=False)
   hours_on_case = models.IntegerField(blank=False)
   continuing_edu = models.CharField(max_length=256, blank=False)
   miles_driven = models.FloatField(blank=False)
   face_advocate_sv_hours = models.IntegerField(blank=False)
   phone_advocate_sv = models.CharField(max_length=256, blank=False)
   other_volunteering = models.CharField(max_length=256, blank=False)
   objects = models.Manager()

   def __str__(self):
      return "TrackingForm: %s" % self.owner
