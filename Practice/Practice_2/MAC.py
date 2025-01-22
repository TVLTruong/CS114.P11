def is_hex_char(c):
    return c.isdigit() or (c in 'ABCDEF')

def check_mac(mac):
    if len(mac) != 17:
        return False
    for i in range(17):
        if i % 3 == 2:
            if mac[i] != '-':
                return False
        else:
            if not is_hex_char(mac[i]):
                return False
    return True

check = []
a = input()
while a != '.':
    if not check_mac(a):
        check.append('false')
    else:
        check.append('true')
    a = input()

for i in check:
    print(i)