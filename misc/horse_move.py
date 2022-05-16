letters = {k: v for k, v in zip('abcdefgh', range(1, 9))}

possible_moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                  (2, -1), (2, 1), (1, -2), (1, 2)]


queue = set()


def is_legal_move(cell, move: tuple) -> bool:
    if (cell[0] + move[0] in range(1, 9)) and (cell[1] + move[1] in range(1, 9)):
        return True
    return False


def add_cells(cell: tuple, other: tuple) -> tuple:
    return (cell[0] + other[0], cell[1] + other[1])


def possible_cells(cell) -> list:
    return [add_cells(cell, item) for item in possible_moves if is_legal_move(cell, item)]


i = 1


def start_moving(queue: set, destination: str):
    global i
    t_destination = (int(destination[1]), letters[destination[0]])
    if i == 1:
        q = set()
        q.add((int(queue[1]), letters[queue[0]]))
    q = queue
    tmp_queue = set(q)
    for item in tmp_queue:
        if destination not in possible_cells(item):
            q.remove(item)
            q.update(possible_cells(item))
        else:

            return i
    i += 1
    start_moving(q, destination)
    return i


print(letters)
starting_point = set()
starting_point.add((1, 1))
print(start_moving('a1', 'b3'))
