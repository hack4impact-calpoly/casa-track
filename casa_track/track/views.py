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
         tf = form.save(commit=False)
         return redirect('/')
   else:
      form = TrackingFormForm()
      print("Here")
   return render(request, 'track/tracking.html', {'form': form})