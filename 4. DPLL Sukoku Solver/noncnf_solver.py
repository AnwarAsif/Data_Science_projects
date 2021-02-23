import pyautogui as pag
import numpy as np
from tabulate import tabulate


def findNextCellToFill(sudoku, dim=9):
    for x in range(dim):
        for y in range(dim):
            if sudoku[x][y] == 0:
                return x, y
    return -1, -1


def isValid(sudoku, i, j, e,dim=9):
    rowOk = all([e != sudoku[i][x] for x in range(dim)])
    if rowOk:
        columnOk = all([e != sudoku[x][j] for x in range(dim)])
        if columnOk:
            secTopX, secTopY = 3*(i//3), 3*(j//3)
            for x in range(secTopX, secTopX+3):
                for y in range(secTopY, secTopY+3):
                    if sudoku[x][y] == e:
                        return False
            return True
    return False


def solveSudoku(sudoku, i=0, j=0, dim=9):
    global backtracks
    i, j = findNextCellToFill(sudoku, dim)
    if i == -1:
        return True

    for e in range(1, 10):
        if isValid(sudoku, i, j, e, dim):
            sudoku[i][j] = e
            if solveSudoku(sudoku, i, j, dim):
                return True
            sudoku[i][j] = 0
    return False


def oldFashioned(puzzle, dim, puzzle_display):
    sudoku = []
    for i in range(0,len(puzzle)):
        if puzzle[i] == '.':
            sudoku.append(0)
        elif puzzle[i] != '.':
            sudoku.append(int(puzzle[i]))
    sudoku = [sudoku[i:i + dim] for i in range(0, len(sudoku), dim)]
    puzzle_s = sudoku.copy()
    solveSudoku(sudoku, dim)
    if puzzle_display == 'on':
        show(puzzle_s, sudoku)
    return sudoku

def show(sudoku1, sudoku2):
    print('\n Puzzle: ')
    print(tabulate(sudoku1))
    print('\n Solved :')
    print(tabulate(sudoku1))