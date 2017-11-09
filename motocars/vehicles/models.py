from django.db import models

# Create your models here.

class VehicleType(models.Model):
    CHOICES = (
    (u'1', u'Auto'),
    (u'2', u'Moto'),
    )

    vehicle_type = CharField(max_length=1, choices=CHOICES)

class Make(models.Model):
    name = models.CharField(max_length=20)
    upper = models.ForeignKey('VehicleType')

     def __str__(self):              # __unicode__ on Python 2
        return self.name

    class Meta:
        ordering = ('name',)

class SubMake(models.Model):
    name = models.CharField(max_length=20)
    upper = models.ForeignKey('Make')

     def __str__(self):              # __unicode__ on Python 2
        return self.name

    class Meta:
        ordering = ('name',)

class SubSubMake(models.Model):
    name = models.CharField(max_length=20)
    upper = models.ForeignKey('SubMake')

     def __str__(self):              # __unicode__ on Python 2
        return self.name

    class Meta:
        ordering = ('name',)

class Year(models.Model):
    upper = models.ForeignKey('SubSubMake')
    name = models.Integer

    def __str__(self):              # __unicode__ on Python 2
       return self.name

   class Meta:
       ordering = ('name',)


class Vehicale(models.Model):
    vehicletype = models.ForeignKey('VehicleType')
    make  = models.ForeignKey('Make', max_length=20)
    sub_make = models.ForeignKey(max_length=20)
    sub_sub_make = models.ForeignKey(max_length=20)
    owner = models.ForeignKey(max_length=20)
    year = models.DateField()
    description = models.TextField(max_length=400)
    likes = models.PositiveSmallIntegerField()
    followers = models.ManyToManyField('Friends')
