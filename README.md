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

To demonstrate this, I provided a code snippet that shows the thread identity of the caller and the signal handler. The thread ID will be the same, proving that signals run in the same thread.

Let's define a signal in [models.py](https://github.com/Hetprajapati12/Django-Trainee-Assignment-AccuKnox/blob/main/models.py) and connect a signal handler that logs the current thread ID.

In a Django view [view.py](https://github.com/Hetprajapati12/Django-Trainee-Assignment-AccuKnox/blob/main/view.py), create an instance of MyModel and observe the thread ID of both the caller and the signal handler.

When you run the code (for example, in the Django shell), the output will look something like ![dash board snap](https://github.com/Hetprajapati12/Django-Trainee-Assignment-AccuKnox/blob/main/Answer%20of%20question%202.png)

As you can see, both the caller and the signal handler share the same thread ID (14048 in this example), confirming that Django signals run in the same thread as the caller.

## Question-3
By default do django signals run in the same database transaction as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

## Answer-3
Yes, by default, Django signals run in the same database transaction as the caller. This means that if a database operation (such as a model save) triggers a signal, and either the signal or the caller raises an exception, the entire transaction will be rolled back.

Django signals that are triggered after database operations, like post_save or post_delete, will only be executed after the transaction is successfully committed.

To demonstrate this, here is a simple example:

[models1.py](https://github.com/Hetprajapati12/Django-Trainee-Assignment-AccuKnox/blob/main/models1.py): We defined a simple model and a signal that is triggered on post_save. The signal will modify the database again, and we raised an exception in the signal handler to see if the entire transaction rolls back.

Now, we will test this using Django's shell. When we try to create an instance of MyModel, the signal will trigger and raise an exception. we expect the entire transaction to roll back, meaning that no changes will be saved to the database.

The post_save signal is triggered when MyModel.objects.create(name="Original Name") is called.

Inside the signal handler, the instance's name is modified and saved again, but an exception is raised afterward.

Since the signal and the original save operation are in the same database transaction, the exception will cause the entire transaction to roll back.

As a result, the newly created MyModel instance will not be saved to the database.

The exception message will be printed, and no objects will be found in the database due to the rollback.

## Topic: Custom Classes in Python

Description: You are tasked with creating a Rectangle class with the following requirements:

1.An instance of the Rectangle class requires length:int and width:int to be initialized.
2.We can iterate over an instance of the Rectangle class 
3.When an instance of the Rectangle class is iterated over, we first get its length in the format: {'length': <VALUE_OF_LENGTH>} followed by the width {width: <VALUE_OF_WIDTH>}

## Answer

Here I have created Rectangle class with the above requirements in [main.py](https://github.com/Hetprajapati12/Django-Trainee-Assignment-AccuKnox/blob/main/main.py) and the output also attached here.

![answer](https://github.com/Hetprajapati12/Django-Trainee-Assignment-AccuKnox/blob/main/answer.png)
