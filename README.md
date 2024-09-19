## Accuknox- Django Trainee Assignment 
## Topic: Django Signals
Here's my submission on Accuknox Django Trainee Assignment question 
## Question-1
By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

## Answer-1
By default, Django signals are executed synchronously. This means that when a signal is sent, the receiver function is executed immediately in the same thread as the sender. The process waits for the receiver function to complete before continuing.

Here Answer1.py simple Django example where we’ll prove that signals run synchronously:

I will create a model and connect a signal to it.

The signal receiver will introduce a delay using time.sleep().

I wll measure the time taken to create an object and confirm that the signal blocks the main thread.
