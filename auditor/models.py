from django.db import models

# Create your models here.
class IseDevce(models.Model):
    host_name = models.CharField(max_length=200)
    device_ise_id = models.IntegerField
    description = models.CharField(max_length=255)
    device_group_id = models.IntegerField
    location_group_id = models.IntegerField
    created_at = models.DateField()
    updated_at = models.DateField()

class IseDeviceGroup(models.Model):
    device_group_name = models.CharField(max_length=255)
    device_group_type = models.CharField(max_length=255)
    device_group_ise_id = models.CharField(max_length=255)
    created_at = models.DateField()
    updated_at = models.DateField()