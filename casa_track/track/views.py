from django.shortcuts import render, redirect
from .forms import TrackingFormForm
from .models import TrackingForm
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden, HttpResponseNotAllowed

# Create your views here.
def home(request):
   if request.user.is_superuser:
        t_forms = TrackingForm.objects.all().order_by('-created_at')
        context = {
            't_forms': t_forms,
            'admin': True,
        }
        return render(request, 'track/user_admin.html', context)
   else:
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

def delete_form(request):
    if request.method == 'POST':
        item_id = int(request.POST.get('item_id'))
        item = TrackingForm.objects.get(id=item_id)
        if request.user.is_superuser:
            item.delete()
            return redirect('/')
        else:
            return HttpResponseForbidden()
    else:
        return HttpResponseNotAllowed(request)



