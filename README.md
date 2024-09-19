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

## Question-2
Do django signals run in the same thread as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

## Answer-2
Yes, Django signals run in the same thread as the caller by default. Signals in Django are synchronous, meaning that the signal is processed in the same thread as the code that triggered the signal.

To demonstrate this, I will provide a code snippet that shows the thread identity of the caller and the signal handler. The thread ID will be the same, proving that signals run in the same thread.

Let's define a signal in models.py and connect a signal handler that logs the current thread ID.

In a Django shell or view, create an instance of MyModel and observe the thread ID of both the caller and the signal handler.

When you run the code (for example, in the Django shell), the output will look something like ![dash board snap](https://github.com/Hetprajapati12/Django-Trainee-Assignment-AccuKnox/blob/main/Answer%20of%20question%202.png)

As you can see, both the caller and the signal handler share the same thread ID (14048 in this example), confirming that Django signals run in the same thread as the caller.

