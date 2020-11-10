import sys

class Cell:
    parent: int
    value: int
    matrix: int
    def __init__(self, value: int, matrix:int):
        self.value = value
        self.parent = 3
        self.matrix = matrix
    
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

#TODO: FIX BACKTRACK FOR AFFINE
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
    idx = possible_ends.index(Cell(max_value, from_matrix['M']))
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

from_matrix = {'M': 0, 'I_x': 1, 'I_y': 2}
def semi_global_affine_gap_alignment(seq_a: str, seq_b: str, m: int, mm: int, gapo: int, gape: int):
    rows, cols = (len(seq_a)+1, len(seq_b)+1)
    matrix = [[Cell(0, from_matrix['M']) for j in range(rows)] for i in range(cols)]
    I_x = [[Cell(0, from_matrix['I_x']) for j in range(rows)] for i in range(cols)]
    I_y = [[Cell(0, from_matrix['I_y']) for j in range(rows)] for i in range(cols)]
    #This changes local to semi-global
    for i in range(1, cols):
        matrix[i][0].setvalue(0).parent = 1 #one cell up
        I_y[i][0].setvalue(0).parent = 1
    for j in range(1, rows):
        matrix[0][j].setvalue(0).parent = 2 #one cell left
        I_x[0][j].setvalue(0).parent = 2
    ##################################
    
    for i in range(1, rows):
        for j in range(1, cols):
            I_x_cells = {0: matrix[j][i-1],
                         1: I_x[j][i-1]}
            I_x_values = [I_x_cells[0] + gapo,
                          I_x_cells[1] + gape]
            result = min(I_x_values)
            I_x[j][i].setvalue(result).parent = I_x_values.index(result)

            I_y_cells = {0: matrix[j-1][i],
                         1: I_y[j-1][i]}
            I_y_values = [I_y_cells[0] + gapo,
                          I_y_cells[1] + gape]
            result = min(I_y_values)
            I_y[j][i].setvalue(result).parent = I_y_values.index(result)

            matrix_cells = {0: matrix[j-1][i-1],
                            1: I_x[j][i],
                            2: I_y[j][i]}
            matrix_values = [matrix_cells[0] + s(seq_a[i-1],seq_b[j-1], m, mm),
                             matrix_cells[1].value,
                             matrix_cells[2].value]
            result = min(matrix_values)
            matrix[j][i].setvalue(result).parent = matrix_values.index(result)
    
    score, alignment_a, alignment_b = backtrack(matrix, seq_a, seq_b)
    return score, alignment_a, alignment_b


input_sequence1 = sys.argv[1]
input_sequence2 = sys.argv[2]

score, alignment_a, alignment_b = semi_global_affine_gap_alignment(input_sequence1, input_sequence2, m=-1, mm=5, gapo=10, gape=1)
print(f"Score: {score}")
print(alignment_a)
print(alignment_b)