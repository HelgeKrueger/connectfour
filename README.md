# Connect Four

Implementation of connect four and agents playing it to illutrate
Monte Carlo Tree Search and other algorithms. This implementation
works with `python3` with `numpy` and `scipy` packages installed.
By running
```
python main.py
```
one can start playing against a Monte Carlo Tree Search algorithm.

## Agents

Agents are an abstraction on how to play the game. The available
implementations are contained in the `agents` package. The implementations
all inherit from the base class `Agent`, which tells one to define a `move`
method, which gets a connect four game as argument.

## The game

The mechanics of the connect four game are explained in the notebook `notebooks/game.ipynb`.
In this folder other notebooks providing useful information are provided.