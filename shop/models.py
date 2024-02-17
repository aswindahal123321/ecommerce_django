from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    image = models.ImageField(upload_to='shop/images/', default="")
    price = models.IntegerField(default=0)
    product_desc = models.CharField(max_length=300)
    date_pub = models.DateField()


    def __str__(self):
            return self.product_name
        


class Contact(models.Model):
    email = models.CharField(max_length=50)
    message = models.CharField(max_length=50)
    
    def __str__(self):
        return self.email
    
    
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=50, default="")
    zip = models.CharField(max_length=50)
    orderItems = models.CharField(max_length=5000)
    
        
    def __str__(self):
        return ("OrderID #" +  str(self.order_id))