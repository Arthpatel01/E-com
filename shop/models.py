from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='shop/images', default="")
    
    

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50, default="")
    help1 = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_date = models.CharField(max_length=50)
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    prod_id = models.CharField(max_length=100)
    prod_name = models.CharField(max_length=200)
    prod_price = models.CharField(max_length=50)
    quantity = models.IntegerField(default=1)
    total_price = models.CharField(max_length=50, default="")
    

    def __str__(self):
        return self.name
