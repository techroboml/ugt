from django.db import models

# Create your models here.
class JuniorRound(models.Model):

    class_names = (
        ('Eight','Eight'),
        ('Nine','Nine'),
        ('Ten','Ten'),
    )

    full_name = models.CharField(max_length=100,null=False,blank=False)
    fathers_name = models.CharField(max_length=100,null=False,blank=False)
    address = models.CharField(null=False,blank=False,max_length=150)
    class_name = models.CharField(max_length=30,null=False,blank=False,choices=class_names)
    school_name = models.CharField(max_length=30,null=False,blank=False)
    mobile_number = models.CharField(max_length=20,null=False,blank=False,unique=True)
    email = models.EmailField(null=True,blank=True)
    image = models.ImageField(upload_to='junior_photos')
    payment_status = models.CharField(max_length=30,null=True,blank=True)

    def __str__(self):
        return self.full_name + self.mobile_number
