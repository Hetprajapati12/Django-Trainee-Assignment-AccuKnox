## Accuknox- Django Trainee Assignment 
## Topic: Django Signals
Here's my submission on Accuknox Django Trainee Assignment question 
## Question-1
By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

## Answer-1
By default, Django signals are executed synchronously. This means that when a signal is sent, the receiver function is executed immediately in the same thread as the sender. The process waits for the receiver function to complete before continuing.

![dashboard snap](https://github.com/Hetprajapati12/Django-Trainee-Assignment-AccuKnox/blob/main/Answer%20of%20question%201.png)

Here [Answer1.py](https://github.com/Hetprajapati12/Django-Trainee-Assignment-AccuKnox/blob/main/Answer1.py) is the simple code snippet. It will prove that signals run synchronously:

First of all, I will create a model and connect a signal to it.

The signal receiver will introduce a delay using time.sleep().

I will measure the time taken to create an object and confirm that the signal blocks the main thread.

When you run Answer1.py code, the output should be attached screenshot clearly demonstrate that the signal is executed synchronously. The signal processing with the 5-second delay(16:46:05 to 16:46:10) completes before the main process (create_model_instance) finishes. This proves that Django signals, by default, are executed synchronously. If they were asynchronous, the model instance creation would complete before the signal processing.
