import sys

online_players = set()
output = []

input_data = sys.stdin.read().strip().splitlines()

for line in input_data:
    if line == '0':
        break

    a, b = map(int, line.split())
    
    if a == 1:
        online_players.add(b)
    elif a == 3:
        online_players.discard(b)  
    elif a == 2:
        output.append('1\n' if b in online_players else '0\n')

for result in output:
    print(result)

