from django.db import models

class cups(models.Model):
    name = models.CharField(max_length=32)
    intensity = models.IntegerField()
    description = models.TextField()
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __unicode__(self):
        return self.name + " " + format(self.cost)
    
class customer(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField()

class order(models.Model):
    customer = models.ForeignKey(customer)
    order_date = models.DateTimeField()
    
class order_items(models.Model):
    order = models.ForeignKey(order)
    cups = models.ForeignKey(cups)
