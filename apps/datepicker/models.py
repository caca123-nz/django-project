from django.db import models

# Create your models here

class DatePicker(models.Model):
    _from = models.DateField()
    _to = models.DateField()

    def __str__(self):
        return self._from
    

