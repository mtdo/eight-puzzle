#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random, time, sys, getopt
from board import Board
from solver import Solver

def main(argv):
    """
    Main function to solve 8-puzzles. The script can be run with the 
    following command line arguments:
        -h: help
        -r: random board configuration
        -i: input file with a board configurationi (/test)
    """
    # Get command line arguments
    try:
        opts, args = getopt.getopt(argv, "hri:")
    except getopt.GetoptError:
        print("main.py [-r] [-i=input_file]")
        sys.exit(1)
        
    # Solve the 8-puzzle with the given arguments
    for opt, arg in opts:
        # Help
        if opt == "-h":
            print("main.py [-r] [-i=input_file]")
            sys.exit()
            
        # Random
        elif opt == "-r":
            # Generate a random number of zeros
            n_zeros = random.randint(1,8)
    
            # Generate a random starting state using the given amount of zeros
            starting_state = list(range(1,(9-n_zeros+1)))+[0]*(n_zeros)
            random.shuffle(starting_state)
            
        # Input file
        elif opt == "-i":
            f = open(arg, "r")
            starting_state = eval(f.read())
            f.close()
        
        # Initialize board
        board = Board(starting_state)
        n_zeros = len(board.getEmptyCells())
        
        # Initialize solver
        solver = Solver(board)
        
        # Solve puzzle
        start_time = time.time()
        print(solver.solve())
        end_time = time.time()
        
        print("Elapsed time: " + str(round((end_time - start_time),4)) + "s.")
        print("Starting board had " + str(n_zeros) + " spaces.")

if __name__ == "__main__":
    main(sys.argv[1:])
