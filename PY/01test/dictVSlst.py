import numpy as np
import sys

a = [1,2,3,4]
b = ['a', 'b', 'c', 'd']
c = [1., 2., 3., 4.,]
d = [True, True, False, True]

print(sys.getsizeof(a))
print(sys.getsizeof(b))
print(sys.getsizeof(c))
print(sys.getsizeof(d))

a = np.array(a)
b = np.array(b)
c = np.array(c)
d = np.array(d)

print()
print(sys.getsizeof(a))
print(sys.getsizeof(b))
print(sys.getsizeof(c))
print(sys.getsizeof(d))


da = {
    (2,3): False,
    (2,4): False,
    (2,5): True,
    (2,6): True
}
print()
print(sys.getsizeof(da))