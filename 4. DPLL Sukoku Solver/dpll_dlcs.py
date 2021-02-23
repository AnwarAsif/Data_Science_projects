import numpy as np
import random
from utility import *
import operator

def backtrack(clauses, literal):
    # Remove the clauses with pure literal
    updated_clauses = []
    for clause in clauses:
        if literal in clause: continue
        if -literal in clause:
            new_clause = [x for x in clause if x != -literal]
            if len(new_clause) == 0: return -1
            updated_clauses.append(new_clause)
        else:
            updated_clauses.append(clause)
    return updated_clauses

def find_literals(clauses):
    counter = {}
    for clause in clauses:
        #print(clause)
        for literal in clause:
            if literal in counter:
                counter[literal] += 1
            else:
                counter[literal] = 1
    return counter


def pure_literal(clauses):
    literals_count = find_literals(clauses)
    literals = []
    pure_literals = []
    for literal, times in literals_count.items():
        if -literal not in literals_count: pure_literals.append(literal)  
    for literal in pure_literals: 
        clauses = backtrack(clauses, literal)
    literals += pure_literals

    return clauses, literals

def unit_literal(clauses):
    literals = []
    unit_clauses = [clause for clause in clauses if len(clause) == 1]
    while len(unit_clauses) > 0:
        unit = unit_clauses[0]
        clauses = backtrack(clauses, unit[0])
        literals += [unit[0]]
        if clauses == -1:
            return -1, []
        if not clauses:
            return clauses, literals
        unit_clauses = [clause for clause in clauses if len(clause) == 1]
    return clauses, literals


def variable_selection(clauses):
    counter = find_literals(clauses)
    try:
        choice, _ = random.choice(list(counter.items()))
    except:
        choice = 1

    return choice


#dynamic largest sum
def dlcs(clauses):
    try:    
        literals_count = find_literals(clauses)
        dlcs = 0
        for literal in literals_count.keys():
            if (literals_count[literal] + literals_count[literal * -1] > dlcs):
                dlcs = literal
        if (literals_count[dlcs] >= literals_count[dlcs * -1] ):
            dlcs = dlcs
        elif (literals_count[dlcs] == literals_count[dlcs * -1] ):
            dlcs = random.choice([dlcs, (dlcs * -1)])
        else: 
            dlcs = dlcs*-1
            
        return dlcs  
    except Exception as inst:
        
        print(type(inst))
        variable_selection(clauses)

def dpll_dlcs(clauses, givenliteral):
    
    clauses, pure_literals = pure_literal(clauses)
    clauses, unit_literals = unit_literal(clauses)
    literals = pure_literals + unit_literals + givenliteral
    
    if clauses == - 1:
        return []
    if not clauses:
        return literals

    variable = dlcs(clauses)
    new_literals = literals + [variable]
    new_clauses = backtrack(clauses, variable) 
    solution = dpll_dlcs(new_clauses, new_literals)
    
    if not solution:
        new_literals = literals + [-variable]
        new_clauses = backtrack(clauses, -variable) 
        solution = dpll_dlcs(new_clauses, new_literals)
    
    return solution