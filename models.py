# myapp/models.py

import threading
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Define a simple model
class MyModel(models.Model):
    name = models.CharField(max_length=100)

# Define the receiver for the post_save signal
@receiver(post_save, sender=MyModel)
def my_model_saved_handler(sender, instance, **kwargs):
    print(f"Signal Handler Thread ID: {threading.get_ident()}")

