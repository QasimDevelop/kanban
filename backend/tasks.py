from celery import shared_task
from time import sleep
@shared_task

def example_task(x,y):
    """
    An example task that adds two numbers.
    """
    sleep(4)
    return x + y 

@shared_task
def example_task_with_error(x, y):  
    """
    An example task that raises an error.
    """
    sleep(4)
    if x < y:
        raise ValueError("x must be greater than or equal to y")
    return x - y    
