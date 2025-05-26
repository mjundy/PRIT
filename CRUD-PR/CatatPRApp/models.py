from django.db import models
from django.utils.timezone import now

# Create your models here.
class StatusPR(models.Model): 
    status = models.CharField(max_length=255)
    def __str__(self):
        return self.status



class PR(models.Model): 
    tgl_pr = models.DateField(null=False, blank=False)
    partnumber = models.CharField(max_length=255, blank=True, unique=False)
    partname = models.CharField(max_length=100)
    qty = models.IntegerField()
    deskripsi = models.CharField(max_length=100, blank=True)
    status = models.ForeignKey(StatusPR, on_delete=models.CASCADE)
    tgl_terima = models.DateField(null=True, blank=True, unique=False)
    tgl_sent_to_purchase = models.DateField(null=True, blank=True)
    age = models.DateField(null=True, blank=True)
    
    class Meta:
        ordering = ['-tgl_pr']