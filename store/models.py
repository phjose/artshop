from django.db import models
from django.contrib.auth.models import User


class Artist(models.Model):
    user = models.OneToOneField(User, blank=True, on_delete=models.CASCADE)
    bio = models.TextField(max_length=1000, blank=True, null=True)
    inst_url = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='uploads/artist/', blank=True, null=True)

    def __str__(self):
        return self.user.username


class Support(models.Model):
    name = models.CharField(max_length=100, default='', blank=True, null=True)

    def __str__(self):
        return self.name


class Technique(models.Model):
    name = models.CharField(max_length=100, default='', blank=True, null=True)

    def __str__(self):
        return self.name


class Painting(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300, default='', blank=True, null=True)
    pub_date = models.DateField()
    support = models.ForeignKey(Support, on_delete=models.CASCADE, default=1)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, default=1)
    technique = models.ForeignKey(Technique, on_delete=models.CASCADE, default=1)
    pheight = models.DecimalField(max_digits=10, decimal_places=2)
    pwidth = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/painting/')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    available = models.BooleanField(default=True)
    image2 = models.ImageField(upload_to='uploads/painting/', blank=True, null=True)
    image3 = models.ImageField(upload_to='uploads/painting/', blank=True, null=True)
    image4 = models.ImageField(upload_to='uploads/painting/', blank=True, null=True)

    class Meta:
        ordering = ('-pub_date', )

    def __str__(self):
        return self.name
