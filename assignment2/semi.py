import sys

class Cell:
    parent: int
    value: int
    def __init__(self, value: int):
        self.value = value
        self.parent = 3
    
    def setvalue(self, value: int):
        self.value = value
        return self

    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return str(self.value)

    def __add__(self, r: int):
        return self.value + r
    
    def __sub__(self, r: int):
        return self.value - r
    
    def __eq__(self, other):
        return self.value == other.value

def s(x_i, y_i, m, mm):
    if x_i == y_i:
        return m
    else:
        return mm

def backtrack(matrix, seq_a, seq_b):
    #This changes semi-global to local
    possible_ends = []
    for elem in matrix[-1]:
        possible_ends.append(elem)
    for i in range(len(matrix)-1):
        possible_ends.append(matrix[i][-1])
    possible_values = []
    for elem in possible_ends:
        possible_values.append(elem.value)
    max_value = min(possible_values)
    idx = possible_ends.index(Cell(max_value))
    max_end = possible_ends[idx]
    position = (0, 0)
    if idx > len(matrix[0]) - 1:
        idx = idx - len(matrix[0])
        position = (idx, len(matrix[0])-1)
    else:
        position = (len(matrix)-1, idx)
    ##################################
    #This changes local to global
    last_position = (len(matrix)-1, len(matrix[0])-1)
    last_end = matrix[last_position[0]][last_position[1]]
    if position[0] < last_position[0]:
        last_end.parent = 1
    if position[1] < last_position[1]:
        last_end.parent = 2
    for i in range(len(matrix[-1])-1):
        elem = matrix[-1][i]
        if elem != max_end:
            elem.parent = 2
    for i in range(len(matrix)-1):
        elem = matrix[i][-1]
        if elem != max_end:
            elem.parent = 1
    ##################################
    current_end = last_end
    position = last_position
    alignment_a = ''
    alignment_b = ''
    while(current_end.parent != 3):
        if current_end.parent == 0:
            alignment_a += seq_a[position[1]-1]
            alignment_b += seq_b[position[0]-1]
            position = (position[0]-1,position[1]-1)
        elif current_end.parent == 1:
            alignment_a += '-'
            alignment_b += seq_b[position[0]-1]
            position = (position[0]-1,position[1])
        elif current_end.parent == 2:
            alignment_a += seq_a[position[1]-1]
            alignment_b += '-'
            position = (position[0],position[1]-1)
        
        current_end = matrix[position[0]][position[1]]
        
    return max_end.value, alignment_a[::-1], alignment_b[::-1]

def semi_global_alignment(seq_a: str, seq_b: str, m: int, mm: int, gap: int):
    rows, cols = (len(seq_a)+1, len(seq_b)+1)
    matrix = [[Cell(0) for j in range(rows)] for i in range(cols)]
    #This changes local to semi-global
    for i in range(1, cols):
        matrix[i][0].setvalue(0).parent = 1
    for j in range(1, rows):
        matrix[0][j].setvalue(0).parent = 2
    ##################################
    
    for i in range(1, rows):
        for j in range(1, cols):
            cells = {0: matrix[j-1][i-1],
                     1: matrix[j-1][i],
                     2: matrix[j][i-1]}
            values = [cells[0] + s(seq_a[i-1],seq_b[j-1], m, mm),
                      cells[1] + gap,
                      cells[2] + gap]
            result = min(values)
            matrix[j][i].setvalue(result).parent = values.index(result)
    
    score, alignment_a, alignment_b = backtrack(matrix, seq_a, seq_b)
    return score, alignment_a, alignment_b


input_sequence1 = sys.argv[1]
input_sequence2 = sys.argv[2]

score, alignment_a, alignment_b = semi_global_alignment(input_sequence1, input_sequence2, m=-1, mm=1, gap=2)
print(f"Score: {score}")
print(alignment_a)
print(alignment_b)