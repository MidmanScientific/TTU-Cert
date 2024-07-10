from django.db import models

# Create your models here.
class myData(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)



class CompanyRequest(models.Model):
    company_name = models.CharField(max_length=255)
    email = models.EmailField()
    contact = models.CharField(max_length=20)
    location = models.CharField(max_length=255)
    post_office = models.CharField(max_length=255)
    status = models.CharField(max_length=20, default='pending')

    def __str__(self):
        return self.company_name

class AutomaticLogin (models.Model):
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    
    