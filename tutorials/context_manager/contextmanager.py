with open('context_manager/sample.txt', 'w') as file:
    file.write('something')

file = open('context_manager/sample.txt', 'w')

try:
    file.write('sometthing')
finally:
    file.close()
# Both are same. Contextmanager finish his job also with error at inside it.