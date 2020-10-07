from django.db import models
from django.utils import timezone
from django.conf import settings


# Create your models here.
class links(models.Model):
    url = models.URLField()
    description = models.TextField(blank=True)
    update_date = models.DateTimeField(default=timezone.now())
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True,on_delete=models.CASCADE)
    
class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    link = models.ForeignKey('links.links',related_name='votes',on_delete=models.CASCADE)

    
