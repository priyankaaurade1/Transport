from django.db import models

# Create your models here.
class Driver(models.Model):
    driver_name = models.CharField(max_length=100)
    driver_license_number = models.CharField(max_length=20)
    driver_contact_number = models.CharField(max_length=15)
    driver_address = models.CharField(max_length=15)
    def __str__(self):
        return f'{self.driver_name}-{self.driver_license_number}' 
