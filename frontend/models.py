from django.db import models

class logindb(models.Model):
    Username=models.CharField(max_length=50,null=True,blank=True)
    Email=models.EmailField(max_length=50,null=True,blank=True)
    Password=models.CharField(max_length=50,null=True,blank=True)

# New fields for password reset functionality
    password_reset_token = models.CharField(max_length=100, blank=True, null=True)
    token_expiration = models.DateTimeField(blank=True, null=True)

    def _str_(self):
        return self.Email



class contactdb(models.Model):
    Name=models.CharField(max_length=20,null=True,blank=True)
    Email=models.EmailField(max_length=20,null=True,blank=True)
    Place=models.CharField(max_length=20,null=True,blank=True)
    Message=models.CharField(max_length=400,null=True,blank=True)


class Service(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()


class BookingDB(models.Model):
    state = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    services = models.ManyToManyField(Service,)
    name = models.CharField(max_length=50, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    date = models.DateField()
    total = models.IntegerField(null=True, blank=True)
    razorpay_order_id = models.CharField(max_length=255, null=True, blank=True)  # New field for storing Razorpay order ID

