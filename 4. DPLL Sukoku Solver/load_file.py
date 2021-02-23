import os
# set current folder as the work folder 

def load_file(hard='easy'):
    # Define root folder
    loc = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))) 
    if hard == 'easy': 
        # Load knowledge base 
        rule_file = '/test sudokus/sudoku-rules-4x4.txt'
        rule_path = loc+rule_file

        #Import puzzles  
        puzzle_file = '/test sudokus/4x4.txt'
        puzzle_path = loc+puzzle_file 
        dim = 4 
        return rule_path, puzzle_path, dim
    elif hard == 'medium': 
        # Load knowledge base 
        rule_file = '/test sudokus/sudoku-rules.txt'
        rule_path = loc+rule_file

        #Import puzzles  
        puzzle_file = '/test sudokus/1000 sudokus.txt'
        puzzle_path = loc+puzzle_file
        dim =9 
        return rule_path, puzzle_path, dim
    elif hard == 'hard': 
        # Load knowledge base 
        rule_file = '/test sudokus/sudoku-rules.txt'
        rule_path = loc+rule_file

        #Import puzzles  
        puzzle_file = '/test sudokus/damnhard.sdk.txt'
        puzzle_path = loc+puzzle_file
        dim = 9
        return rule_path, puzzle_path, dim
    elif hard == 'hardest': 
        # Load knowledge base 
        rule_file = '/test sudokus/sudoku-rules-16x16.txt'
        rule_path = loc+rule_file

        #Import puzzles  
        puzzle_file = '/test sudokus/16x16.txt'
        puzzle_path = loc+puzzle_file
        dim = 9
        return rule_path, puzzle_path, dim