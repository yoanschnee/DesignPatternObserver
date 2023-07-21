from __future__ import annotations
from abc import abstractmethod, ABC
from typing import List
from subject import Subject


class Observer(ABC):
    @abstractmethod
    def update(self, subject : Subject):
        pass

class ConcreteObserverA(Observer):

    def update(self, subject : Subject):
        if subject._state < 3:
            print("ConcreteObserverA: Reacted to the event")
        else:
            print("ConcreteObserverA: Did not react to the event")

class ConcreteObserverB(Observer):

    def update(self, subject : Subject):
        if subject._state >= 3:
            print("ConcreteObserverB: Reacted to the event")
        else:
            print("ConcreteObserverB: Did not react to the event")

    


