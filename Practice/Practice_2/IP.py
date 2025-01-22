def check(octet):
    if len(octet) > 1 and octet[0] == '0':
        return False
    return 0 <= int(octet) <= 255

s = input()
ips = []
        
for i in range(1, min(4, len(s) - 2)):
    for j in range(i + 1, min(i + 4, len(s) - 1)):
        for t in range(j + 1, min(j + 4, len(s))):
            A = s[:i]
            B = s[i:j]
            C = s[j:t]
            D = s[t:]
            
            if check(A) and check(B) and check(C) and check(D):
                ips.append(f"{A}.{B}.{C}.{D}")

for ip in ips:
    print(ip)
