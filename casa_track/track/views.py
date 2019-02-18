from django.shortcuts import render, redirect
from .forms import TrackingFormForm
from .models import TrackingForm

# Create your views here.
def home(request):
   return render(request, 'track/home.html')

def tracking(request):
   if request.method == "POST":
      form = TrackingFormForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('/')
      else:
         print(form.errors)
   else:
      form = TrackingFormForm()
   return render(request, 'track/tracking.html', {'form': form})