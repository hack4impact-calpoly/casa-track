from django.shortcuts import render

# Create your views here.
def index(request):
   return render(request, 'track/index.html')

def tracking(request):
    return render(request, 'track/tracking.html')