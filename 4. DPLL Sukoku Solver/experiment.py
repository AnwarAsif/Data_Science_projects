import numpy as np
import os 
import sys 
from tabulate import tabulate
from utility import * 
from dpll import  dpll
from dpll_dlcs import dpll_dlcs
from dpll_moms import dpll_moms
from dpll_jw import dpll_jw
from dpll_dlis import dpll_dlis
from noncnf_solver import oldFashioned
from load_file import load_file
from tqdm import tqdm
import timeit
import pandas as pd
import random
from datetime import datetime



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
            solution = extractDigits(solution)
        else:
            print('s UNSATISFIABLE')
    elif method == 'dpll_dlcs':
        solution = dpll_dlcs(CNF, [])
        if solution:
            solution = np.array(solution)
            solution = solution[solution > 0]
            solution = extractDigits(solution)
        else:
            print('s UNSATISFIABLE')
    
    elif method == 'dpll_dlis':
        solution = dpll_dlis(CNF, [])
        if solution:
            solution = np.array(solution)
            solution = solution[solution > 0]
            solution = extractDigits(solution)
        else:
            print('s UNSATISFIABLE')
    elif method == 'dpll_moms':
        solution = dpll_moms(CNF, [])
        if solution:
            solution = np.array(solution)
            solution = solution[solution > 0]
            solution = extractDigits(solution)
        else:
            print('s UNSATISFIABLE')
    elif method == 'dpll_jw':
        solution = dpll_jw(CNF, [])
        if solution:
            solution = np.array(solution)
            solution = solution[solution > 0]
            solution = extractDigits(solution)
        else:
            print('s UNSATISFIABLE')
    elif method == 'nocnf':
        solution = oldFashioned(puzzle, dim, puzzle_display)
        if solution:
            solution = np.array(solution)
            solution = solution[solution > 0]
            solution = extractDigits(solution)
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
    clear = lambda: os.system('clear') #on Linux System
    clear()
    
    # Algorithm Selection: dpll, dpll_dlcs, dpll_moms
    # Select puzzle display 
    # Select hardness of the puzzle 
    #methods= ['dpll','dpll_dlcs','dpll_jw','dpll_dlis','dpll_moms','nocnf']
    methods= ['dpll','dpll_dlcs']
    puzzle_display = 'off'
    hardness =['easy','medium','hard']
    batch = 10

    results = pd.DataFrame(columns=['method','hardness','resolvetime', 'batch'])
    method_result = pd.DataFrame(columns=['method', 'hardness', 'methodtime', 'batch'])

    for i in range(batch):
        print('Batch no:',i+1)
        for hard in hardness:
            rule_path, puzzle_path, puzzle_dim = load_file(hard)
            knowledge_base = load_KB(rule_path)
            puzzles = load_puzzle(puzzle_path)
            selected_puzzles = random.choices(puzzles,k=30)
            for method in methods:
                print('Hardness:', hard)
                print('Method:', method)
                start = timeit.default_timer()
                for puzzle in tqdm(selected_puzzles): 
                    puzzle_start = timeit.default_timer()
                    solve_sudoku(knowledge_base, puzzle, method=method , dim=puzzle_dim, puzzle_display=puzzle_display)
                    puzzle_end = timeit.default_timer()
                    puzzle_time = puzzle_end - puzzle_start
                    results = results.append({'method': method,'hardness':hard,'resolvetime':puzzle_time, 'batch': i+1}, ignore_index=True)
                stop = timeit.default_timer()
                total_time  = (stop - start)
                print('Time: ', total_time) 
                method_result = method_result.append({'method': method,'hardness':hard,'methodtime':total_time, 'batch': i+1}, ignore_index=True)

print(results)
print(method_result)
results.to_csv(datetime.now().strftime('result_%H_%M_%d_%m_%Y.csv'), index=False)
method_result.to_csv(datetime.now().strftime('method_result_%H_%M_%d_%m_%Y.csv'), index=False)

    