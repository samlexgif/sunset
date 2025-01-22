from django.shortcuts import render, get_object_or_404, redirect # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from .models import BloodSugarReading, nutritonalfacts, EducationalResource
from .forms import BloodSugarReadingForm

@login_required
def dashboard(request):
    readings = BloodSugarReading.objects.filter(user=request.user)
    meal_plans = nutritonalfacts.objects.filter(user=request.user)
    resources = EducationalResource.objects.all()
    return render(request, 'dashboard.html', {'readings': readings, 'meal_plans': meal_plans, 'resources': resources})

@login_required
def add_reading(request):
    if request.method == 'POST':
        form = BloodSugarReadingForm(request.POST)
        if form.is_valid():
            reading = form.save(commit=False)
            reading.user = request.user
            reading.save()
            return redirect('dashboard')
    else:
        form = BloodSugarReadingForm()
    return render(request, 'add_reading.html', {'form': form})

@login_required
def Nutrionalfacts(request):
    nutrition = nutritonalfacts.objects.all()
    return render(request, 'add_meal_plan.html', {'nutrition': nutrition})


def resource_list(request):
    resources = EducationalResource.objects.all()
    return render(request, 'resource_list.html', {'resources': resources})

def resource_detail(request, resource_id):
    resource = get_object_or_404(EducationalResource, id=resource_id)
    return render(request, 'resource_detail.html', {'resource': resource})
