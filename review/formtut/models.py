from django.db import models

class Person(models.Model):

    name = models.CharField(max_length=200)
    birth_date = models.DateField()
    birth_place = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name