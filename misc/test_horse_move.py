import pytest
from horse_move import Horse


def test_is_legal_move():
    test_horse = Horse((1, 1))
    assert test_horse.is_legal_move((-2, -1)) == False
    assert test_horse.is_legal_move((2, -1)) == False
    assert test_horse.is_legal_move((-1, -2)) == False
    assert test_horse.is_legal_move((2, 1)) == True
    test_horse = Horse((5, 1))
    assert test_horse.is_legal_move((-2, 1)) == True
    assert test_horse.is_legal_move((-1, 2)) == True
    assert test_horse.is_legal_move((2, 1)) == True
    assert test_horse.is_legal_move((1, -2)) == False
    test_horse = Horse((1, 4))
    assert test_horse.is_legal_move((2, -1)) == True


def test_legal_moves():

    test_horse = Horse((1, 1))

    assert test_horse.legal_moves == sorted([(2, 1), (1, 2)])

    test_horse = Horse((1, 4))

    assert test_horse.legal_moves == sorted(
        [(1, -2), (1, 2), (2, 1), (2, -1)])

    test_horse = Horse((4, 4))

    assert test_horse.legal_moves == sorted(Horse.possible_moves)


def test_move():

    test_horse = Horse((1, 1))

    test_horse.make_move((2, 1))

    assert test_horse.position == (3, 2)

    test_horse = Horse((1, 1))

    test_horse.make_move((-2, 1))

    assert test_horse.position == (1, 1)


def test_find_path():
    test_horse = Horse((1, 1))

    test_horse.find_path((3, 2)) == 'Found'
