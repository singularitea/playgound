# creating data frame of big O notation and graphing
# O(1)
# O(logN)
# O(N)
# O(N^2)
# O(2^N)

import pandas as pd
import matplotlib.pyplot as plt
import math

number_of_rows = 10
O_1 = []
O_logn = []
O_n = []
O_n2 = []
O_2n = []

for n in range(1,number_of_rows+1):
    O_1.append(1)
    O_logn.append(math.log2(n))
    O_n.append(n)
    O_n2.append(n**2)
    O_2n.append(2**n)


df = pd.DataFrame(
    {'O(1)': O_1,
     'O(logN)': O_logn,
     'O_n': O_n,
     'O(N^2)':  O_n2,
     'O(2^N)': O_2n})

print(df)

df.plot()

plt.show()
