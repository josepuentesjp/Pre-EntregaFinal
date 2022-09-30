from django.db import models

# Create your models here.

class category(models.Model):

    domain_name = models.CharField(max_length=40)
    owner = models.CharField(max_length=40)
    attribute_quantity = models.IntegerField()

class task(models.Model):

    task_name = models.CharField(max_length= 20)
    task_deadline = models.DateField()
    task_owner = models.CharField(max_length= 40)

class worker(models.Model):

    worker_name = models.CharField(max_length= 40)
    worker_domain = models.CharField(max_length=40)
    worker_email = models.EmailField()
    worker_phone_number = models.PositiveIntegerField()
