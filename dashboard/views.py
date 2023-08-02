from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import DriverForm
from .models import Driver
def index(request):
    return render(request, 'index.html')

def user_profile(request):
    return render(request, 'users-profile.html')

def pages_error_404(request):
    return render(request, 'partials/pages-error-404.html')

def pages_contact(request):
    return render(request, 'partials/pages-contact.html')

def pages_faq(request):
    return render(request, 'partials/pages-faq.html')

# driver_details
def driver_details(request):
    if request.method == 'POST':
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = DriverForm()
    return render(request, 'driver/driver_details.html', {'form': form})

def get_latest_driver_data():
    latest_driver = Driver.objects.last()
    print(latest_driver)

    if latest_driver:
        return {
            'driver_name': latest_driver.driver_name,
            # 'driver_email': latest_driver.driver_email,
            'driver_license_number': latest_driver.driver_license_number,
            'driver_contact_number': latest_driver.driver_contact_number,
            'driver_address': latest_driver.driver_address,
        }
    return {}
