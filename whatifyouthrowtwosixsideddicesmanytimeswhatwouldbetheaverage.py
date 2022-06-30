from tqdm import tqdm
import random 
from matplotlib import pyplot as plt

rng = 1000000

rn = []

avg = []
sum = 0

for loop in tqdm(range(rng)):
    loop += 1
    num1 = random.randint(1,6)
    num2 = random.randint(1,6)
    if num1 > num2:
        sum += num1
        num = num1
    else:
        sum += num2
        num = num2

    rn.append(num)
    avg.append(sum/loop)

plt.plot(range(0,rng), avg)
plt.show()

print(sum/loop)