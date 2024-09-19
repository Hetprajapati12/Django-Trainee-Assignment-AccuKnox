# myapp/models.py

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class MyModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=MyModel)
def my_model_post_save(sender, instance, **kwargs):
    print("Signal triggered - modifying instance")
    
    # Modify the instance after saving
    instance.name = "Modified in Signal"
    instance.save()

    # Raising an exception to test transaction rollback
    raise Exception("Signal Error - Rollback Transaction")
