from django.db import models
from django.utils.timezone import now

# Create your models here.
class StatusPR(models.Model): 
    status = models.CharField(max_length=255)
    def __str__(self):
        return self.status

class JenisPart(models.Model): 
    jenis_part = models.CharField(max_length=255)
    def __str__(self):
        return self.jenis_part


class PR(models.Model): 
    tgl_pr = models.DateField(null=False, blank=False)
    partnumber = models.CharField(max_length=255, blank=True, unique=False)
    partname = models.CharField(max_length=100)
    jenis_part = models.ForeignKey(JenisPart, on_delete=models.CASCADE, null=False, blank=False)
    qty = models.IntegerField()
    uom = models.CharField(max_length=50, blank=True)
    deskripsi = models.CharField(max_length=100, blank=True)
    status = models.ForeignKey(StatusPR, on_delete=models.CASCADE, null=False, blank=False)
    tgl_terima = models.DateField(null=True, blank=True, unique=False)
    tgl_sent_to_purchase = models.DateField(null=True, blank=True)
    tgl_cancel = models.DateField(null=True, blank=True)
    age = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.partnumber} - {self.partname}"
    
    class Meta:
        ordering = ['-tgl_pr']