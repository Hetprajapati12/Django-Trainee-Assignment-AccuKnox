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

When I run Answer1.py code, the output should be attached screenshot clearly demonstrate that the signal is executed synchronously. The signal processing with the 5-second delay(16:46:05 to 16:46:10) completes before the main process (create_model_instance) finishes. This proves that Django signals, by default, are executed synchronously. If they were asynchronous, the model instance creation would complete before the signal processing.

## Question-2
Do django signals run in the same thread as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

## Answer-2
Yes, Django signals run in the same thread as the caller by default. Signals in Django are synchronous, meaning that the signal is processed in the same thread as the code that triggered the signal.

To demonstrate this, I provided a code snippet that shows the thread identity of the caller and the signal handler. The thread ID will be the same, proving that signals run in the same thread.

Let's define a signal in [models.py](https://github.com/Hetprajapati12/Django-Trainee-Assignment-AccuKnox/blob/main/models.py) and connect a signal handler that logs the current thread ID.

In a Django view [view.py](https://github.com/Hetprajapati12/Django-Trainee-Assignment-AccuKnox/blob/main/view.py), create an instance of MyModel and observe the thread ID of both the caller and the signal handler.

When I run the code (for example, in the Django shell), the output will look something like ![dash board snap](https://github.com/Hetprajapati12/Django-Trainee-Assignment-AccuKnox/blob/main/Answer%20of%20question%202.png)

As you can see, both the caller and the signal handler share the same thread ID (14048 in this example), confirming that Django signals run in the same thread as the caller.

## Question-3
By default do django signals run in the same database transaction as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

## Answer-3
Yes, by default, Django signals run in the same database transaction as the caller. To demonstrate this, we can use a combination of a model, a signal, and database transaction behavior. When the signal is triggered during a model save, if the transaction is rolled back, the signal handler’s actions are also rolled back, indicating that both share the same transaction.

Here is a simple example:

[models1.py](https://github.com/Hetprajapati12/Django-Trainee-Assignment-AccuKnox/blob/main/models1.py): 


Model Definition: I create a simple model TestModel with a single field name.

Signal Definition: A post_save signal is connected to the TestModel model. When the model is saved, the signal will print a message and, if the name is "rollback", it will raise a ValidationError.

Transaction Block: Inside the test_signal_and_transaction function, I create a new TestModel instance in a manual transaction block (transaction.atomic()), which ensures everything happens within a single transaction.

Triggering Rollback: When "rollback" is passed as the name, the signal handler raises a ValidationError, which rolls back the transaction.

Proof of Rollback: After the exception is raised, I check whether the object was actually saved to the database. If it wasn't saved, it proves that the signal and the caller are part of the same transaction.

![dash board snap](https://github.com/Hetprajapati12/Django-Trainee-Assignment-AccuKnox/blob/main/Answer%20of%20question%203.png)


The output shows that the object was not saved in the database (the count is 0), confirming that the signal ran within the same transaction as the caller. When the transaction was rolled back, both the model save and the signal handler's actions were rolled back together, proving that they share the same database transaction.


## Topic: Custom Classes in Python

Description: You are tasked with creating a Rectangle class with the following requirements:

1.An instance of the Rectangle class requires length:int and width:int to be initialized.

2.We can iterate over an instance of the Rectangle class 

3.When an instance of the Rectangle class is iterated over, we first get its length in the format: {'length': <VALUE_OF_LENGTH>} followed by the width {width: <VALUE_OF_WIDTH>}

## Answer

Here I have created Rectangle class with the above requirements in [main.py](https://github.com/Hetprajapati12/Django-Trainee-Assignment-AccuKnox/blob/main/main.py) and the output also attached here.

![answer](https://github.com/Hetprajapati12/Django-Trainee-Assignment-AccuKnox/blob/main/answer.png)
