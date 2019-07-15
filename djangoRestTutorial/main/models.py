from django.db import models

# Create your models here.
class Study(models.Model):
    name = models.CharField(max_length=60, blank=True, default='Study')
    created = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=10)

    class Meta:
        ordering = ('created',)
