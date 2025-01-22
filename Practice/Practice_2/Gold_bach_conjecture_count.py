import math

def check_snt(n):
    if n < 2:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def _count_(n):
    snt = []
    for i in range(2, n + 1):
        if check_snt(i):
            snt.append(i)

    count = 0
    for i in range(len(snt)):
        for j in range(i, len(snt)):
            if snt[i] + snt[j] == n:
                count += 1
    return count

n = int(input())
count = _count_(n)

print(count)
