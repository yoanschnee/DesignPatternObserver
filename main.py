from observer import ConcreteObserverA, ConcreteObserverB
from subject import ConcreteSubject


if __name__ == "__main__":
    subject = ConcreteSubject()

    obs1 = ConcreteObserverA()
    obs2 = ConcreteObserverB()
    subject.attach(obs1)
    subject.attach(obs2)

    subject.some_business_logic()


    subject.notify()
    print("")
    print("-------------------")
    print("")
    subject.some_business_logic()
    subject.notify()
