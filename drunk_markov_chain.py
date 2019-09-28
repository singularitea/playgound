# each step can chane position +/- 1, odds should be 0.5 for either case
from random import random
import matplotlib
import matplotlib.pyplot as plt

x = 0

print("Welcome to the drunk Markov chain \n")
print("Enter the amount of steps to take:")
steps = int(input())

def rand_int_pos_or_neg():
    num = random()
    if num < 0.5:
        return 1
    else:
        return -1

position = 0
ls = []
step_ls = []

for i in range(steps):
    position = position + rand_int_pos_or_neg()
    ls.append(position)
    step_ls.append(i)



# plotting
fig, ax = plt.subplots()
ax.plot(step_ls, ls)

ax.set(xlabel='steps', ylabel='position',
       title='Drunk Markov Chain')
ax.grid()

# fig.savefig("test.png")
plt.show()