# eight-puzzle #
The [8-puzzle](https://en.wikipedia.org/wiki/15_puzzle) is a sliding puzzle consisting of a game board of numbered tiles with one or more tiles missing. The objective is to order the tiles by sliding them to an empty board position. Herein, an 8-puzzle solver with different state-space search algorithms is implemented.

## Usage ##
The solver can be launched with a random initial board configuration:  
```sh
$ python3 src/main.py -r
```

Alternatively, a specific initial board configuration can be given as input with a text file:  
```sh
$ python3 src/main.py -i test/medium.txt
```

### Board state representation
The game board is represented as a list of 3 X 3 grid cells, indicating which tile (number of the tile) is in each board position. A zero is used to indicate an empty position in the game board. The list indices start from the top left of the game board moving first right and then down.  
E.g.:
```
1  2  3
4  5  6
7  8  
```
is represented as  
```
[1, 2, 3, 4, 5, 6, 7, 8, 0]
```

### Solver
Three different state-space search algorithms can be used by the solver class. These are selected using the `-a` command line argument when launching the solver. The implemented state-space search algorithms are:

| Argument      | Algorithm                 |
| ------------- | -------------             |
| `a`           | A* search (default)       |
| `wa`          | Weighted A* search        |
| `gbf`         | Greedy Best-First search  |

E.g.:  
```sh
$ python3 src/main.py -i test/medium.txt -a gbf
```

### Todos
- Implement solvers for additional [state-space search](https://en.wikipedia.org/wiki/State_space_search) algorithms
- Expand game board state representation to 15-puzzle boards (and beyond...)
