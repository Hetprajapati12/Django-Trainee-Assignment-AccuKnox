from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError

class TestModel(models.Model):
    name = models.CharField(max_length=100)

# This signal will be triggered after saving TestModel
@receiver(post_save, sender=TestModel)
def post_save_signal(sender, instance, **kwargs):
    print("Signal handler called!")
    # Let's trigger an exception to see if the transaction rolls back everything
    if instance.name == "rollback":
        print("Raising exception in signal handler to rollback transaction...")
        raise ValidationError("Forcing rollback!")

# Test this with a manual transaction block
def test_signal_and_transaction():
    try:
        with transaction.atomic():
            test_obj = TestModel.objects.create(name="rollback")
            # At this point, the post_save signal should be called.
            # The exception inside the signal should cause everything to rollback.
    except ValidationError as e:
        print(f"Caught exception: {e}")

    # Check if the object was saved in the database after the exception
    print("Number of TestModel objects in the database:", TestModel.objects.count())

