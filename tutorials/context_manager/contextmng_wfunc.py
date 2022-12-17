from contextlib import contextmanager

# without @contextmanager, TypeError: 'generator' object does not support the context manager protocol
@contextmanager
def open_managed_file(filename):
    f = open(filename, 'w')
    try:
        yield f
    finally:
        f.close()

with open_managed_file('context_manager/sample.txt') as f:
    f.write('something..')