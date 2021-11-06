from random import random
import numpy as np
import matplotlib.pyplot as plt

# Exercise Sheet 1 Daniel Banov
############################
# Exercise 1.1.
print("Exercise 1.1\n")

number_of_simulation = 5000000


def simulate_one_day():
    """
    Simulates a day of the bakery and returns the number of possibly sold pretzels
    """
    number_of_customers = int(random() * 9)
    number_of_sold_pretzels = 0
    # Simulate for every customer the number of possibly sold pretzels
    for _ in range(number_of_customers):
        number_of_sold_pretzels += int(random() * 3) + 1

    return number_of_sold_pretzels


# execution of simultations and storing them in the array simulation_results
simulation_results = []
for _ in range(number_of_simulation):
    simulation_results.append(simulate_one_day())

print(
    f"Average of possibly sold pretzels per day with {number_of_simulation} simulations:  {np.mean(simulation_results)}")

# calculating the profits if i pretzels are produced
profit_list = []
for i in range(25):
    ones = np.ones(len(simulation_results))
    average_profit = np.mean(0.3 * np.minimum(simulation_results, ones * i) - 0.2 * np.maximum(
        ones * i - simulation_results, ones * 0))
    profit_list.append(average_profit)

# printing
print(f"The number of produced pretzels with the highest average profit:  {profit_list.index(max(profit_list))}")

############################
# Exercise 1.2.
print("\n\nExercise 1.2\n")


def cond_prob(k, n):
    if n > k or k < 0 or n * 3 < k:
        return 0
    if n == k:
        return 1 / 3 ** k
    else:
        return 1 / 3 * sum([cond_prob(k - j, n - 1) for j in range(1, 4)])


def p_X(k):
    return 1 / 9 * sum([cond_prob(k, n) for n in range(9)])


P_X = [p_X(k) for k in range(25)]
c_d_f = [sum([P_X[i] for i in range(j + 1)]) for j in range(25)]
print(f"Cumulative distribution function: ")
for i in range(25):
    print(f"P(X≤{i}) = {c_d_f[i]}\n")


############################
# Exercise 2.


def lcg(x_0, a, c, m):
    l = [x_0]
    x = x_0
    while True:
        x = (a * x + c) % m
        if x == x_0:
            break
        l.append(x)
    return l


b = lcg(0, 133, 7, 432)
plt.scatter(b, b[1:] + [b[0]])
plt.savefig("1.png")
plt.clf()
b = lcg(1, 109, 5, 216)
plt.scatter(b, b[1:] + [b[0]])
plt.savefig("2.png")
plt.clf()
b = lcg(0, 4, 2, 243)
plt.scatter(b, b[1:] + [b[0]])
plt.savefig("3.png")
plt.clf()
b = lcg(1, 41, 11, 1000)
plt.scatter(b, b[1:] + [b[0]])
plt.savefig("4.png")
plt.clf()
############################
# Exercise 3.
print("\n\nExercise 3\n")

max_len = -1
index = -1
x = 4558
b = [x]

for _ in range(9999):
    x = x ** 2
    x = int(((x % 1000000) - x % 100) / 100)
    b.append(x)
starter = b[-1]
counter = 0

for i in range(9998, -1, -1):
    counter += 1
    if b[i] == starter:
        if max_len <= counter:
            index = starter
            max_len = counter
        break

plt.scatter(b, b[1:] + [b[0]])
plt.savefig("5.png")
print(index)
print(max_len)
