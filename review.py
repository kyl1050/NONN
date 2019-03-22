import numpy as np

a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print (a)

bool_idx = a > 6
print (bool_idx)
print (a[bool_idx])