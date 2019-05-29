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
      (CELENA, 'Celena Zupko'),
      (HEIDI, 'Heidi Turbow'),
      (GAIL, 'Gail Wechsler'),
      (KATIE, 'Katie Robinson'),
      (PETE, 'Pete Skarda'),
      (MELANIE, 'Melanie Barket'),
      (NICOLE, 'Nicole Perotti'),
   ]
   owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
   advocate = models.CharField(max_length=256, blank=False)
   supervisor = models.CharField(max_length=256, choices=SV_CHOICES, blank=False, null=False)
   child_name = models.CharField(max_length=256, blank=False)
   month = models.CharField(max_length=256, blank=False) # doesn't like being a DateTimeField
   hours_spent = models.PositiveSmallIntegerField(blank=False)
   hours_education = models.PositiveSmallIntegerField(blank=False)
   hours_on_case = models.PositiveSmallIntegerField(blank=False)
   continuing_edu = models.CharField(max_length=256, blank=False)
   miles_driven = models.PositiveSmallIntegerField(blank=False)
   # yes/no field
   face_advocate_sv_hours = models.CharField(max_length=256, blank=False)
   #yes/no field
   phone_advocate_sv = models.CharField(max_length=256, blank=False)
   casa_volunteering = models.CharField(max_length=256, blank=False, default=djnow)
   other_volunteering = models.CharField(max_length=256, blank=False)
   
   esignature = models.TextField(blank=True)

   signature_date = models.DateTimeField(default=djnow)
   created_at = models.DateTimeField(default=djnow)
   objects = models.Manager()

   def __str__(self):
      return self.child_name
