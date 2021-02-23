import numpy as np
from tabulate import tabulate

def load_KB(rule_path):
    f = open(rule_path, 'r')
    lines = f.readlines()
    in_data = []
    for line in lines:
        in_data.append(line.strip().split('0')[0])
    f.close()
    # Insert all the clauses in the knowledge base
    KB = [[int(n) for n in line.split()] for line in in_data if line[0] not in ('c', 'p')]

    return KB

def load_puzzle(puzzle_path):
    f = open(puzzle_path, 'r')
    lines = f.readlines()
    puzzles = []
    for line in lines:
        puzzles.append(line.strip().split('n')[0])
    f.close()

    return puzzles

def cnf_conversion(puzzle, dim):
    premises = []
    row = 1
    col = 1
    for i in range(len(puzzle)):
        if col == dim + 1: 
            col = 1
            row += 1  
        result = ''
        if puzzle[i] != '.':
            value = puzzle[i]
            result = result + str(row)+str(col)+str(value)
            premises.append([int(result)])
        col += 1

    return premises

def extractDigits(lst): 
    res = [] 
    for el in lst: 
        res.append([el]) 
      
    return(res) 

def display_sudoku(premises, puzzle_size, soled=False):

    sudoku = []
    size = puzzle_size
    for i in range(size):
        for j in range(size):
            sudoku.append('.')
    sudoku = np.array(sudoku).reshape(size,size)
    for i in range(len(premises)):
        val = str(premises[i])
        m = int(val[1]) -1
        n = int(val[2]) -1
        sudoku[m][n] = val[3]

    print(tabulate(sudoku))

if __name__ == "__main__":
    pass 