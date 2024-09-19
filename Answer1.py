import time
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime

# Define a simple model
class MyModel(models.Model):
    name = models.CharField(max_length=100)

# Define the receiver for the post_save signal
@receiver(post_save, sender=MyModel)
def my_signal_receiver(sender, instance, **kwargs):
    print(f"Signal received at: {datetime.now()}")
    time.sleep(5)  # Introduce a 5-second delay
    print(f"Signal processing complete at: {datetime.now()}")

# To prove that the signal is synchronous, we measure the time before and after saving the model instance
def create_model_instance():
    print(f"Creating model instance at: {datetime.now()}")
    MyModel.objects.create(name="Test Model")
    print(f"Model instance created at: {datetime.now()}")

# Run this function in your Django shell or view
create_model_instance()
