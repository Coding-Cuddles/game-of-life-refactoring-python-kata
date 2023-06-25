import pytest
from game import Game


def test_under_population():
    game = Game([
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ])
    game.iterate()

    assert game.grid == [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]


def test_two_or_three_neighbors_live_on():
    game = Game([
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
    ])
    game.iterate()

    assert game.grid == [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
    ]


def test_over_population():
    game = Game([
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
    ])
    game.iterate()

    assert game.grid == [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]


def test_reproduction():
    game = Game([
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
    ])
    game.iterate()

    assert game.grid == [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
    ]
