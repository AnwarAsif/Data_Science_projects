import numpy as np
import os 
import sys 
from tabulate import tabulate
from utility import * 
from dpll import  dpll
from tqdm import tqdm
import timeit
import cProfile

def solve_sudoku(knowledge_base, puzzle, method='dpll', puzzle_display='off', dim=9):
    
    # Convert puzzles to CNF 
    premises = cnf_conversion(puzzle,dim)
    #print("premises", premises)

    # Add premises to the knowledgebase 
    CNF = knowledge_base + premises #+ [[101,101]]

    # Resolve sudoku
    if method == 'dpll':
        solution = dpll(CNF,[])
        if solution:
            solution = np.array(solution)
            solution = solution[solution > 0]
            # fix output format for displaying the result in console 
            solution = extractDigits(solution)
            #print('satisfied')
        else:
            print('s UNSATISFIABLE')

    if puzzle_display == 'on' and solution:
        puzzle_size = dim 
        print('Puzzle: ')
        display_sudoku(premises, puzzle_size)
        print('Solved:')
        display_sudoku(solution, puzzle_size)


if __name__ == "__main__":

    # clear console 
    #clear = lambda: os.system('clear') #on Linux System
    #clear()
    
    # set current folder as the work folder 
    print(os.path.dirname(os.path.realpath(__file__)))
    
    # Load knowledge base 
    loc = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    rule_file = '/test sudokus/sudoku-rules.txt'
    rule_path = loc+rule_file
    knowledge_base = load_KB(rule_path)
    print('Total number of clauses in KB:', len(knowledge_base))
    print('first clause:', knowledge_base[0])

    #Import puzzles  
    puzzle_file = '/test sudokus/1000 sudokus.txt'
    puzzle_path = loc+puzzle_file
    puzzles = load_puzzle(puzzle_path)
    print('First puzzle: ', puzzles[0])


    # Algorithm Selection: dpll, 
    # Select puzzle display 
    method = 'dpll'
    puzzle_display = 'of'
    puzzle_dim = 9

    # Solve each puzzle with given rule and method
    # puzzle = puzzles[34]
    # print(puzzle)
    start = timeit.default_timer()
    print(start)
    # for puzzle in tqdm(puzzles[100]): 
    #     solve_sudoku(knowledge_base, puzzle, puzzle_display=puzzle_display, dim=puzzle_dim)
    cProfile.run("[solve_sudoku(knowledge_base, puzzle, puzzle_display=puzzle_display, dim=puzzle_dim) for puzzle in puzzles[10]]")
    stop = timeit.default_timer()
    
    total_time  = (stop - start)
    print('Time: ', total_time)  
    