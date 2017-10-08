#!/usr/bin/env python
# -*- coding: utf-8 -*-

from board import Board
from priority_queue import PriorityQueue
from math import inf

class Solver:
    """Class for solving the 8-puzzle."""
    
    def __init__(self, start):
        """Class is initialized with a starting game board."""
        
        self.start = start
        self.goal = self.getGoalState(start)
        
    def getGoalState(self, board):
        """Returns the goal state of the starting board."""
        
        n_zeros = board.tiles.count(0)
        return Board(list(range(1,(10-n_zeros)))+([0]*n_zeros))
        
    def getHeuristic(self, board):
        """Returns the heuristic cost for a state using the Hamming distance."""
        
        cost = 0
        for i in range(0, 9):
            if board.tiles[i] != self.goal.tiles[i]:
                cost += 1
        return cost
        
    def findInSet(self, board, DICT):
        """Finds whether the given configuration exists with a better f-score in
        the given dictionary (corresponding the set)."""
        
        try:
            if DICT[str(board.tiles)] <= board.f:
                return True
            else:
                DICT[str(board.tiles)] = board.f
                return False
        except KeyError:
            return False
            
    def rebuildPath(self, current):
        """Rebuilds the solution path using the reached goal state."""
        
        path = [current]
        while current.predecessor:
            path.append(current.predecessor)
            current = current.predecessor
        return path
        
    def checkSolution(self, best, current, expansions):
        """Checks whether the termination of the solution loop resulted in a 
        solved game."""
        
        if best < inf:
            path = self.rebuildPath(current)
            for state in reversed(path):
                print(state)
            return "Solution reachable in " + str(current.g) + " moves.\n" +\
                "Solution found with " + str(expansions) + " state expansions."
        else:
            return "Solution does not exist."
        
    def solve(self):
        """A* algorithm for solving the puzzle. Algorithm follows the structure
        presented in the lecture slides."""
        
        # Set costs for the starting state
        current = self.start
        current.g = 0
        current.h = self.getHeuristic(current)
        current.f = current.g + current.h
        
        # Initialize the OPEN and CLOSED sets
        OPEN = PriorityQueue()
        OPEN.add(current)
        OPENF = {} # f-value for the OPEN tiles
        
        CLOSED = set()
        CLOSEDF = {} # f-value for the CLOSED tiles
        
        # Current best f-value
        best = inf
        
        # A* algorithm
        while OPEN:          
            # Pop the state with the lowest f-value
            current = OPEN.pop()
            
            # Terminate algorithm if lowest f-value from OPEN is higher than 
            # current best
            if current.f >= best:
                return self.checkSolution(best, current, len(CLOSED))
            
            # Move current from OPEN to CLOSED
            CLOSED.add(current)
            CLOSEDF[str(current.tiles)] = current.f
            
            # Investigate the successor states
            successors = current.getSuccessors()
            for successor in successors:
                # Change A and B to change the algorithm operation
                # A = 1, B = 1 -> A*
                # A = 0, B = 1 -> GBF
                # A = 1, B > 1 -> WA*
                A = 1
                B = 1
                successor.g = current.g + 1
                successor.h = self.getHeuristic(successor)
                successor.f = A*successor.g + B*successor.h
                
                # Check if successor goal state better than current best
                if successor.tiles == self.goal.tiles:
                    best = min(best, successor.g)

                # If successor state can be found in OPEN or CLOSED with a
                # better f-value move to next successor 
                if self.findInSet(successor, OPENF):
                    continue
                    
                if self.findInSet(successor, CLOSEDF):
                    continue
                
                # Append valid successor to OPEN
                OPEN.add(successor)
                OPENF[str(successor.tiles)] = successor.f
                          
        return self.checkSolution(best, current, len(CLOSED))
