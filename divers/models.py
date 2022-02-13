from django.db import models

# Create your models here.
class Site(models.Model):
    name = models.CharField(max_length=100)
    country= models.CharField(max_length=100)
    max_depth = models.IntegerField()
    site_type= models.CharField(max_length=100)
    marine_life=models.CharField(max_length=200)
    owner = models.ForeignKey(
        'users.User', related_name='sites', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Log(models.Model):
    site = models.ForeignKey(Site, on_delete= models.CASCADE, related_name='logs')
    visited = models.BooleanField()
    favorite = models.BooleanField()
    bucket_list = models.BooleanField()
    owner = models.ForeignKey(
        'users.User', related_name='logs', on_delete=models.CASCADE)

    def __str__(self):
        return self.owner