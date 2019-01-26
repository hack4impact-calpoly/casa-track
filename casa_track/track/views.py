from django.shortcuts import render

# Create your views here.
def index(request):
   print("PATH BELOW:")
   if request.path == "/test":
      return render(request, 'track/test.html')
   return render(request, 'track/index.html')