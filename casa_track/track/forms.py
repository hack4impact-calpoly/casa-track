from django import forms
from .models import TrackingForm   

class TrackingFormForm(forms.ModelForm):
   class Meta:
      model = TrackingForm
      fields = ('supervisor','child_name','month', 'hours_spent','hours_education',
                  'hours_on_case','continuing_edu','miles_driven','face_advocate_sv_hours',
                  'phone_advocate_sv','other_volunteering')