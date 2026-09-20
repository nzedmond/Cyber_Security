import time
from sympy.ntheory import factorint

# small n (n = p*q, where p and q are primes)
n_small = 253 # 11*23
start = time.time()
factorint(n_small)
print(f"Time to factor {n_small}: {time.time() - start:.6f} seconds")

# Medium n
n_medium = 988027 # 941*1051
start = time.time()
factorint(n_medium)
print(f"Time to factor {n_medium}: {time.time() - start:.6f} seconds")

# Large n
n_large = 2147483647
start = time.time()
factorint(n_large)
print(f"Time to facto {n_large}: {time.time() - start:.6f} seconds")