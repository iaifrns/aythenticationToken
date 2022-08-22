from django.db import models

class userModel(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=255)
    first_name = models.CharField(max_length=30) 
    last_name = models.CharField(max_length=30)

    def __self__(self):
        return self.username

class colorModel(models.Model):
    colorName= models.CharField(max_length=50)
    colorCode= models.CharField(max_length=50)

    def __self__(self):
        return self.colorCode

class objectModel(models.Model):
    objectName= models.CharField(max_length=255)
    image= models.CharField(max_length=255)

    def __self__(self):
        return self.image
# Create your models here.
