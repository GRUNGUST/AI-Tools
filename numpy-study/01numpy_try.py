import numpy as np
import time

t0 = time.time()
l = list(range(100))
for _ in range(1000):
    l = list(map(lambda i: i + 1, l))

t1 = time.time()

a = np.array(l)
for _ in range(1000):
    a += 1

print('Python list with the map spend {:.3f}s'.format(t1 - t0))
print('Numpy array spend {:.3f}s'.format(time.time() - t1))
