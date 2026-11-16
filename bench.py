import ctypes
import timeit
import numpy as np

N = 10_000_000

lib = ctypes.CDLL("./libadd.so")
lib.add_array_ll.argtypes = [ctypes.POINTER(ctypes.c_longlong), ctypes.c_int]
lib.add_array_ll.restype = ctypes.c_longlong

py_list = list(range(N))
arr = np.arange(N, dtype=np.int64)
ptr = arr.ctypes.data_as(ctypes.POINTER(ctypes.c_longlong))

def python_sum():
    total = 0
    for x in py_list:
        total += x
    return total

def numpy_sum():
    return arr.sum()

def c_sum():
    return lib.add_array_ll(ptr, N)

print(python_sum(), numpy_sum(), c_sum())

def best_time(func):
    return min(timeit.repeat(func, number=1, repeat=5))

py = best_time(python_sum)
np_time = best_time(numpy_sum)
c = best_time(c_sum)

print(f"Python: {py:.4f}s")
print(f"NumPy:  {np_time:.4f}s ({py/np_time:.0f}x faster)")
print(f"C:      {c:.4f}s ({py/c:.0f}x faster)")
