import ctypes

lib = ctypes.CDLL("./libadd.so")
arr = (ctypes.c_int * 5)(1, 2, 3, 4, 5)
print(lib.add_array(arr, 5))
