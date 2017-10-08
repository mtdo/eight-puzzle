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
        -i: input file with a board configuration [input_file.txt]
        -a: solving algorithm [a, wa, gbf] (A*, Weighted A*, Greedy Best-First)
    Example:
        python3 main.py -i ../test/medium.txt -a a
    """
    # Get command line arguments
    try:
        opts, args = getopt.getopt(argv, "hri:a:")
    except getopt.GetoptError:
        print("main.py [-r] [-i=input_file] [-a=algorithm]")
        sys.exit(1)
        
    # Solve the 8-puzzle with the given arguments
    # Solving algorithm default arguments
    A = 1
    B = 1
    for opt, arg in opts:
        # Help
        if opt == "-h":
            print("main.py [-r] [-i=input_file] [-a=algorithm]")
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
            
        # Algorithm
        elif opt == "-a":
            if arg == "a":
                A = 1
                B = 1
            elif arg == "wa":
                A = 1
                B = 2 # B > 1, can be adjusted!
            elif arg == "gbf":
                A = 0
                B = 1
            else:
                print("Not a valid algorithm.")
                sys.exit(1)
        
    # Initialize board
    board = Board(starting_state)
    n_zeros = len(board.getEmptyCells())
    
    # Initialize solver
    solver = Solver(board, A = A, B = B)
    
    # Solve puzzle
    start_time = time.time()
    print(solver.solve())
    end_time = time.time()
    
    print("Elapsed time: " + str(round((end_time - start_time),4)) + "s.")
    print("Starting board had " + str(n_zeros) + " spaces.")

if __name__ == "__main__":
    main(sys.argv[1:])

