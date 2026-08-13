# Game of Life refactoring kata in Python

[![CI](https://github.com/Coding-Cuddles/game-of-life-refactoring-python-kata/actions/workflows/main.yml/badge.svg)](https://github.com/Coding-Cuddles/game-of-life-refactoring-python-kata/actions/workflows/main.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Refactor Conway's Game of Life toward the Liskov Substitution Principle
without changing its behavior. Setup is complete when all five starter tests
pass.

## Overview

This kata complements [Clean Code: SOLID, Ep. 11 - Liskov Substitution Principle](https://cleancoders.com/episode/clean-code-episode-11-p1).

This repository contains two exercises designed to improve your skills in
code refactoring, with a focus on the Liskov Substitution Principle (LSP).

## Instructions

### Exercise 1

The Game of Life is a cellular automaton devised by the British mathematician
John Horton Conway in 1970. The game is a zero-player game, meaning that its
evolution is determined by its initial state, requiring no further input.

You have a code base that simulates the Game of Life, but it does not adhere to
the LSP. Your task is to refactor the code to align with the LSP. This means,
among other things, that you should be able to replace any instance of a parent
class with an instance of one of its child classes without altering the
correctness of the program.

**Instructions:**

1. Review the current code base and identify parts that violate the LSP.
2. Refactor the violating code to align with the LSP.
3. Make sure all the tests still pass after your refactoring.

Be sure to run the tests before and after your refactoring to make sure you
haven't changed the game's behavior.

### Exercise 2

For those who complete the refactoring in the first part of the class, a second
exercise is available. Your task is to extend the original code with new types
of cells.

Here are the new cell types to implement:

1. **Immortal Cell**: This cell type never dies. Once born, it stays alive
   through all the subsequent generations.
2. **Reproductive Cell**: This cell type reproduces faster than a normal cell.
   It can make a new cell in the neighborhood with two or three neighbors
   instead of exactly three.
3. **Lazy Cell**: This cell type requires more neighbors to survive. It stays
   alive only if it has exactly three neighbors.

Setup is complete when the existing test suite passes.

## Prerequisites

Required:

- [Git](https://git-scm.com/downloads)
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

Optional:

- [GNU Make](https://www.gnu.org/software/make/), for shorter commands. Every required task also
  has a direct `uv` command.

You do not need to install Python or pytest separately. `uv` installs a compatible Python version
and the locked project dependencies when needed.

## Set up the kata

1. Clone the repository:

   ```console
   git clone https://github.com/Coding-Cuddles/game-of-life-refactoring-python-kata.git
   ```

2. Enter the repository directory:

   ```console
   cd game-of-life-refactoring-python-kata
   ```

3. Run the existing tests. Use Make when it is installed:

   ```console
   make test
   ```

   Otherwise, run pytest through `uv` directly:

   ```console
   uv run pytest
   ```

   The first run may install Python and the project dependencies. Setup is complete when pytest
   reports `5 passed`.

   If the command fails with `uv: command not found`, install
   [uv](https://docs.astral.sh/uv/getting-started/installation/) and repeat this step.

## Work on the kata

Start in `game.py`. The existing behavior is covered by `test_game.py`.

Run the tests after each change. Use Make when it is installed:

```console
make test
```

Otherwise, run pytest through `uv` directly:

```console
uv run pytest
```

Continue when the test run passes.

## Make command reference

Make is optional. Run `make` or `make help` to list these commands in the terminal.

| Command             | Result                                  |
| ------------------- | --------------------------------------- |
| `make all`          | Run the test suite                      |
| `make help`         | Show the command reference              |
| `make test`         | Run the test suite                      |
| `make format`       | Format tracked Python files             |
| `make format-check` | Check formatting without changing files |
| `make clean`        | Remove generated caches                 |
