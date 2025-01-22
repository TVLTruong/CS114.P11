def move_and_cal(matrix):
    matrix2 = []
    
    for row in matrix:
        new_row = [_ for _ in row if _ != 0]

        i = 0
        while i < len(new_row) - 1:
            if new_row[i] == new_row[i + 1]:
                new_row[i] *= 2
                new_row.pop(i + 1)
            i += 1

        new_row += [0] * (4 - len(new_row))
        matrix2.append(new_row)

    return matrix2

def transpose(matrix):
    return [list(row) for row in zip(*matrix)]

matrix = [list(map(int, input().split())) for _ in range(4)]
s = input()

if s == 'L':
    result = move_and_cal(matrix)

elif s == 'R':
    _matrix = [row[::-1] for row in matrix]
    move = move_and_cal(_matrix)
    result = [row[::-1] for row in move]

elif s == 'U':
    transposed_matrix = transpose(matrix)
    move = move_and_cal(transposed_matrix)
    result = transpose(move)

elif s == 'D':
    transposed_matrix = transpose(matrix)
    _matrix = [row[::-1] for row in transposed_matrix]
    move = move_and_cal(_matrix)
    _matrix2 = [row[::-1] for row in move]
    result = transpose(_matrix2)

for row in result:
    print(' '.join(map(str, row)))

'''
chatgpt:
1. Hoán vị ma trận trong py gốc có lệnh nào hỗ trợ không? 
2. Lệnh biểu diễn nhanh ma trận theo dạng 
a b
c d
'''
