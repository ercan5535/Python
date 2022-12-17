class ManagedFile:
    def __init__(self, filename):
        self.filename = filename
        print('init')

    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        print('exit')
        # return True, if return True, doesnt raise an error on main
with ManagedFile('context_manager/sample.txt') as file:
    print('do some stuf...')
    file.write('something')
    # file.somethod() # to create an error
print('continuing..')
"""
init
enter
do some stuf...
exit
Traceback (most recent call last):
  File "c:\\Users\\ercan\\OneDrive\\Masaüstü\\cs50\\Python exercises\\context_manager\\contextmng_wclass.py", line 19, in <module>
    file.somethod() # to create an error
    ^^^^^^^^^^^^^
AttributeError: '_io.TextIOWrapper' object has no attribute 'somethod'
"""
# so it closed file and raise error


class ManagedFile2:
    def __init__(self, filename):
        self.filename = filename
        print('init')

    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print("exception has been handled")
        print('exc:', exc_type, exc_value)
        print('exit')
        return True
with ManagedFile2('context_manager/sample.txt') as file:
    print('do some stuf...')
    file.write('something')
    file.somethod() # to create an error
print('continuing..')
"""
init
enter
do some stuf...
exception has been handled
exc: <class 'AttributeError'> '_io.TextIOWrapper' object has no attribute 'somethod'
exit
continuing..
 """