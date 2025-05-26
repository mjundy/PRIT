from django.db import models

# Create your models here.
class Mesin(models.Model):
	code_machine = models.CharField(max_length=255, null=True)
	no_machine = models.CharField(max_length=255, unique=True)
	description = models.TextField()
	is_active = models.BooleanField(default=True) # Status mesin
