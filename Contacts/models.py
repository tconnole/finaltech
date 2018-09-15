from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=40)
    email = models.CharField(max_length=40)

    def _sts_(self):
        return self.first_name
