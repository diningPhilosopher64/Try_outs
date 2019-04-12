from django.db import models
from django.db.models.signals import post_save
from iex import Stock as Stock_iex




# Create your models here.



class Stock(models.Model):   
    
    # Present 
    stock_name = models.CharField(max_length=20, blank=False, null=False)


    # Get from iex
    #name_of_company = Stock(stock_name).company()['companyName']
    company_name = models.CharField(max_length=100,blank = True)
    
    # Company information
    stock_data = models.TextField(blank=True,null=False)

    #Company Description
    description = models.TextField(blank= True, null= True)   
    
    # Get from iex. Not required here
    # price = models.DecimalField(decimal_places=3, max_digits=100)

    #Checks if downloaded from wiki
    is_downloaded = models.BooleanField(default=False)


    def save(self, *args, **kwargs):
       
        self.company_name = Stock_iex(self.stock_name).company()['companyName']        
        super().save(*args, **kwargs)  # Call the "real" save() method.












    # Will be grabbed from Wiki and stored in 1 place.
    # headquarters = models.CharField(max_length=100, blank=True, null=False)
    # url = models.CharField(max_length=100,blank = True)
    # founded_on = models.CharField(max_length=100, null=False, blank=  True)
    # founders = models.CharField(max_length=100,null=False,blank = True)
    # ceo = models.CharField(max_length=100, null=False,blank  = True)


    