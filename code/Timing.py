from contextlib import contextmanager

@contextmanager
def timer(message):
    "Context manager that reports the time taken by a block of code."
    print("[*]", message)
    start = time.time()
    yield
    print("[#] finished in {:.3f} seconds".format(time.time() - start))
    
# Use in a `with` statement
