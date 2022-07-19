def add(a, b, queue=None):
    """Pass in queue only when running unit tests"""
    if queue is not None:
        queue.put(a + b)
    return a + b


def subtract(queue, a, b):
    queue.put(a - b)


def divide(queue, a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    queue.put(a / b)


def multiply(queue, a, b):
    queue.put(a * b)
