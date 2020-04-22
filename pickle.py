import pickle
d = {'An arbitrary': 'Python Object'}
d_pickled = pickle.dumps(d)
print(d_pickled)
'''\x80\x03}q\x00X\x0c\x00\x00\x00An arbitraryq\x01X\r\x00\x00\x00Python Objectq\x02s.'''
#cleard_unpickled = pickle.loads(d_pickled)
#d_unpickled
'''{'An arbitrary': 'Python Object'}'''
