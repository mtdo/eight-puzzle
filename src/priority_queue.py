#!/usr/bin/env python
# -*- coding: utf-8 -*-

import heapq

class PriorityQueue:
    """Priority queue class for the OPEN set of states."""
    
    def __init__(self):
        """Initialized as an empty list."""
        
        self.elements = []
        
    def add(self, board):
        """Add board to the priority queue (OPEN)."""
        
        heapq.heappush(self.elements, board)
        
    def pop(self):
        """Pop lowest f-value board from priority queue (OPEN)."""
        
        return heapq.heappop(self.elements)
        
    def __len__(self):
        """Returns the length of the elements in the priority queue."""
        
        return len(self.elements)

