from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=120)
    Account_Balance = models.DecimalField(default=0.00,max_digits=100,decimal_places=2)
    
    
    def __unicode__(self):
        return self.name
        
        
        
    def __str__(self):
        
        return self.name
    
    
    