#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import inf

class Board:
    """Class for representing the game board (state) for the 8-puzzle game."""
    
    # Indices for cells and their neighbours
    neighbour_cells = {    
        '0':[1,3],
        '1':[2,4,0],
        '2':[5,1],
        '3':[4,6,0],
        '4':[5,7,3,1],
        '5':[8,4,2],
        '6':[7,3],
        '7':[8,6,4],
        '8':[7,5]
        }
        
    def __init__(self, tiles, predecessor=None):
        """Tiles are represented as a list of numbers from 1..N"""
        
        self.tiles = tiles
        self.predecessor = predecessor
        self.f = inf
        self.g = inf
        self.h = inf
        
    def __repr__(self):
        """Prints the board in nice format."""
        
        return "\n".join([
        str(self.tiles[0:3]),
        str(self.tiles[3:6]),
        str(self.tiles[6:9]),
        "\n",
        ]).replace("[","").replace("]","").replace(","," ")
        
    def __lt__(self, board):
        """Comparison operator for priority queue data structure."""
        
        return self.f < board.f
        
    def getEmptyCells(self):
        """Returns all the empty cells in the board."""
        
        return [i for i,x in enumerate(self.tiles) if x==0]
        
    def getSuccessors(self):
        """Returns all successor states of the current state."""
        
        empty_cells = self.getEmptyCells()
        neighbour_states = []
        
        for cell in empty_cells:
            neighbour_cells = self.neighbour_cells[str(cell)]
            for neighbour_cell in neighbour_cells:
                neighbour_state = self.tiles[:]
                neighbour_state[cell], neighbour_state[neighbour_cell] = \
                neighbour_state[neighbour_cell], neighbour_state[cell]
                if (neighbour_state != self.tiles) and ((Board(neighbour_state) \
                    not in neighbour_states)):
                    neighbour_states.append(Board(neighbour_state, self))
        return neighbour_states
