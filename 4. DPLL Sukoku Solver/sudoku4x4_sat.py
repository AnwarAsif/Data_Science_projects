import numpy as np
import sys
import os
from tabulate import tabulate

# KNOWLEDGE BASE 
# Importing Sudoku rules from file 
loc = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
filepath = '/test sudokus/sudoku-rules-4x4.txt'
path = loc+filepath

f = open(path, 'r')
lines = f.readlines()
in_data = []
for line in lines:
    in_data.append(line.strip().split('0')[0])
f.close()

# Insert all the clauses in the knowledge base
KB = [[int(n) for n in line.split()] for line in in_data if line[0] not in ('c', 'p')]
#print('Total number of clauses in KB:', len(KB))
#print('first clause:', KB[0])


# PREMISES 
# Import Sudokus 
filepath = '/test sudokus/4x4.txt'
path = loc+filepath
f = open(path, 'r')
lines = f.readlines()
sudoku4x4 = []
for line in lines:
  sudoku4x4.append(line.strip().split('n')[0])
f.close()
#print(sudoku4x4[:5])

# Converting 1st puzzle to CNF

col = 1
row = 1
premises = []
for i in range(len(sudoku4x4[0])):
  if col == 5: 
    col = 1
    row += 1  
  result = ''
  if sudoku4x4[0][i] != '.':
    value = sudoku4x4[0][i]
    result = result + str(row)+str(col)+str(value)
    premises.append([int(result)])
  col += 1

sudoku = []
for i in range(4):
  for j in range(4):
    sudoku.append('.')
sudoku = np.array(sudoku).reshape(4,4)
for i in range(len(premises)):
  val = str(premises[i])
  m = int(val[1]) -1
  n = int(val[2]) -1
  sudoku[m][n] = val[3]

print(tabulate(sudoku))

# Preparing Final CNF by combining KB and Premises 
CNF = KB + premises

def backtrack(clauses, literal):
    modified = []
    for clause in clauses:
        if literal in clause: continue
        if -literal in clause:
            c = [x for x in clause if x != -literal]
            if len(c) == 0: return -1
            modified.append(c)
        else:
            modified.append(clause)
    return modified

def get_counter(formula):
    counter = {}
    for clause in formula:
        for literal in clause:
            if literal in counter:
                counter[literal] += 1
            else:
                counter[literal] = 1
    return counter


def pure_literal(clauses):

    counter = get_counter(clauses)
    literals = []
    pure_literals = [ x for x,y in counter.items() if -x not in counter]

    for literal in pure_literals: 
        clauses = backtrack(clauses, literal)

    literals += pure_literals

    return clauses, literals

def unit_propagation(clauses):
    assignment = []
    unit_clauses = [c for c in clauses if len(c) == 1]
    while len(unit_clauses) > 0:
        unit = unit_clauses[0]
        clauses = backtrack(clauses, unit[0])
        assignment += [unit[0]]
        if clauses == -1:
            return -1, []
        if not clauses:
            return clauses, assignment
        unit_clauses = [c for c in clauses if len(c) == 1]
    return clauses, assignment


def variable_selection(clauses):
    counter = get_counter(clauses)

    try:
        choice = random.choice(counter)
    except:
        choice = 1

    print(choice)
    return choice

def dpll(clauses, model):
    clauses, pure_literals = pure_literal(clauses)
    clauses, unit_literals = unit_propagation(clauses)
    literals = pure_literals + unit_literals
    if clauses == - 1:
        return []
    if not clauses:
        return literals

    variable = variable_selection(clauses)
    solution = dpll(backtrack(clauses, variable), literals + [variable])

    if not solution:
        solution = dpll(backtrack(clauses, -variable), literals + [-variable])
    return solution


def main():
    cnf = [[-1, -3, -4], [2, 3, -4], [1, -2, 4], [1, 3, 4], [-1, 2, -3],[-5,2],[10]]
    solution = dpll(CNF,[])

    if solution:
      print('Satisfiable')   
      #print(len(final))
      for i in range(len(final)):
        val = str(final[i])
        m = int(val[0]) -1
        n = int(val[1]) -1
        sudoku[m][n] = val[2]
      
      print(tabulate(sudoku))

    else:
        print ('s UNSATISFIABLE')

if __name__ == "__main__":
    main()

