import sys
import time

cur = time.time()

def check(num):
    num_str = ''.join(map(str, num))
    return num_str == num_str[::-1]

def add(num):
    num_1 = num[::-1]
    result = []
    y = 0

    for _ in range(len(num_1)):
      x = (num_1[_] + num[_] + y) % 10
      y = (num_1[_] + num[_] + y) // 10
      result.append(x)

    if y > 0:
      result.append(y)

    return result[::-1]

num = list(map(int, input()))
steps = []

if check(num):
    result = False

else:
  i = 0
  while(i < 10001):      

      num = add(num)
      steps.append(num)

      if len(num) == 15000:
          result = True
          break

      if check(num):
          result = False
          break
      
      i += 1

  if i == 10001:
    result = True

if result:
    print("YES")
    print(len(steps)) 
    print(''.join(map(str, num)))
else:
    print("NO")
    sys.stdout.write('\n'.join(map(str, steps)))

cur_ = time.time()
print(cur_ - cur)