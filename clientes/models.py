from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    rfid = models.IntegerField(null=True,blank=True)
    deficiency_type = models.CharField(null=True,blank=True,max_length=20)
    photo = models.ImageField(upload_to='clients_photos', null=True, blank= True)

    def __str__(self):
        return self.first_name

