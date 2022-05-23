release_dates = [1897, 1998, 2000, 1948, 1962, 1950, 1975, 1960, 2017, 1937, 1968, 1996, 1944, 1891, 1995, 1948, 2011, 1965, 1891, 1978]

import numpy as np
def min_max_normalize(lst):
  normalized =[]
  minimum = min(lst)
  maximum = max(lst)
  normalized = [(val-minimum)/(maximum-minimum) for val in lst]
  return normalized


print(min_max_normalize(release_dates))
