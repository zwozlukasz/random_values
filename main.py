# generate random float values

import random

random_value = random.random() * 5
print(f"Float random value between 0 - 5 is: {random_value:.3f}")

random_value = random.random() * 7
print(f"Float random value between 0 - 7 is: {random_value:.3f}")

random_value = random.random() * 10
print(f"Float random value b etween 0 - 10 is: {random_value:.3f}")

random_value = random.randrange(1, 100, 3)
print(f"Int randrange(1, 100, 3) is: {random_value}")

random_value = random.randint(1, 100)
print(f"Int randint() from 1 to 100 is: {random_value}")

rand_list = [random.randrange(0, 100, 1) for _ in range(20)]
print(f"List of random values: {rand_list}")

state = random.getstate()
random_value_1 = random.random()
# random.seed(10)
# state_2 = random.getstate()
# random_value_2 = random.random()
# print(f"value_1: {random_value_1:.3f} value_2: {random_value_2:.3f}")
# print(f"Python state: {state}, state 2: {state_2}")

random_value = random.uniform(10,100)
print(f"Float random.uniform(10,100) is: {random_value:.2f}")

random.shuffle(rand_list)
print(f"shuffle: {rand_list}")





