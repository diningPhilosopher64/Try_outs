from django.db import models

# Create your models here.



class Stock(models.Model):
    company_name = models.CharField(max_length=100, null=False,blank = False)
    stock_name = models.CharField(max_length=20, blank=False, null=False)
    description = models.TextField(blank= True, null= True)
    price = models.DecimalField(decimal_places=3, max_digits=100)
    headquarters = models.CharField(max_length=100, blank=True, null=False)
    url = models.CharField(max_length=100,blank = True)
    founded_on = models.CharField(max_length=100, null=False, blank=  True)
    founders = models.CharField(max_length=100,null=False,blank = True)
    ceo = models.CharField(max_length=100, null=False,blank  = True)


    