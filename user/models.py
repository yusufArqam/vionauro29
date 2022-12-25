from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Biodata(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    alamat = models.TextField()
    telp = models.CharField(max_length=14)

    def _str_(self):
        return "{} - {}".format(self.user, self.telp)