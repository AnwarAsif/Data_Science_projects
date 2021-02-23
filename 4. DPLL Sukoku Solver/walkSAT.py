import sys
import random
import json
import timeit
from ast import literal_eval

class WalkSAT:
    defined = 0     #contains whether or not file has reached p
    clauses = []    #the actual clauses parsed out
    numVar = 0      #number of variables
    numClause = 0   #number of clauses
    T = []          #truth statement
    literals = {}   #where each literal is located, by clause
    p = .2          #temporary test, is assigned later by argument
    timeLimit = 10000000000 #changed later by argument
    falseClauses = [] #list of all clauses not satisfied by T
    numSatisfiedLitsPerClause = {} #verbatim from slides
    start = 0       #start time
    stop = 0        #stop time
    flips = 0       #number of flips made

