from datetime import datetime

from random import choice, seed


class TimeUTC:
    def __get__(self, instance, owner_class):
        return datetime.utcnow().isoformat()


class Logger:
    current_time = TimeUTC()


class Choice:
    def __init__(self, choises):
        self.choises = choises

    def __get__(self, instance, owner_class):
        return choice(self.choises)


class Deck:
    suit = suit = Choice(['s', 'h', 'c', 'd'])

    card = Choice(tuple('23456789TJQKA'))


if __name__ == '__main__':

    d = Deck()
    seed(0)

    for _ in range(10):
        print(f'{d.card}{d.suit}')
