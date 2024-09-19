# Django Shell or View
import threading
from myapp.models import MyModel

print(f"Caller Thread ID: {threading.get_ident()}")  # Prints caller thread ID

# Create an instance of MyModel which triggers the post_save signal
MyModel.objects.create(name="Test Model")
