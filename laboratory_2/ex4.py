import numpy as np

r = [2, 2.5, 1, 1.2, 3.1, 0.5, 4, 4.4, 3, 2.9, 2.8, 1.9, 1.5, 1.4, 7, 3.8, 8]

P0 = 0.1
P = P0

print(f"Year 0: Population = {P}")

for year in range(len(r)):
    P = r[year] * P * (1 - P)
    print(f"Year {year+1}: r = {r[year]}, Population = {P}")
