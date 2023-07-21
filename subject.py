from __future__ import annotations
from abc import abstractmethod, ABC
from typing import List
from random import randrange

class Subject(ABC):
    """
    Subject interface declares a set of methods for managing the subscribers
    """
    @abstractmethod
    def attach(self, observer : Observer) -> None:
        """
        Attach a observer to the subject
        """
        pass

    @abstractmethod
    def detach(self, observer : Observer) -> None:
        """
        Detach a observer from the subject
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all observers of an event
        """
        pass




class ConcreteSubject(Subject):
    # from observer import Observer
    _state : int = None

    _observers : List[Observer] = []

    def attach(self, observer : Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer : Observer) -> None:
        self._observers.remove(observer)
       
    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:

        print("Biz logic")
        self._state = randrange(1,10)

        print("Notify")
        self.notify()