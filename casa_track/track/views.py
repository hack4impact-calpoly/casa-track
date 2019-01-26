from django.shortcuts import render

# Create your views here.
def home(request):
   return render(request, 'track/home.html')

def tracking(request):
    return render(request, 'track/tracking.html')