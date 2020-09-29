from __future__ import annotations
from abc import ABC, abstractmethod


class Context():

    def __init__(self, strategy: Strategy) -> None:

        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:

        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:

        self._strategy = strategy

    def do_act(self) -> None:

        result = self._strategy.act(2, 5)
        print(result)


class Strategy(ABC):

    @abstractmethod
    def act(self, a, b):
        pass


class StrategyAddition(Strategy):

    def act(self, a, b):
        return a + b


class StrategySubtraction(Strategy):

    def act(self, a, b):
        return a - b


class StrategyMult(Strategy):

    def act(self, a, b):
        return a * b


if __name__ == "__main__":
    context = Context(StrategyAddition())
    print("Сложение 2-х чисел: ", end="")
    context.do_act()

    context.strategy = StrategySubtraction()
    print("Вычитание 2-х чисел: ", end="")
    context.do_act()

    context.strategy = StrategyMult()
    print("Умножение 2-х чисел: ", end="")
    context.do_act()