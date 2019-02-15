from django.shortcuts import render, redirect
from .forms import TrackingFormForm

# Create your views here.
def home(request):
   return render(request, 'track/home.html')

def tracking(request):
   if request.method == "POST":
      form = TrackingFormForm(request.POST)
      if form.is_valid():
         tf = form.save(commit=False)
         tf.owner = request.user
         tf.save()
         return redirect('/')
   else:
      form = TrackingFormForm()
   return render(request, 'track/tracking.html', {'form': form})