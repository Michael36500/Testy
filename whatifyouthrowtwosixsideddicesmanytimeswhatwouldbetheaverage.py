from tqdm import tqdm
import random 
from matplotlib import pyplot as plt

rng = 100000

rn = []

avg = []
sum = 0

for loop in tqdm(range(rng)):
    loop += 1
    nums = []
    for _ in range(6):
        nums.append(random.randint(1,6))
        
    num = max(nums)
    sum += num
    rn.append(num)
    avg.append(sum/loop)

plt.plot(range(0,rng), avg)
plt.show()

print(sum/loop)
