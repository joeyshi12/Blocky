from model import Observer


class Subject:
    observers: list = []

    def add_observer(self, observer: Observer):
        self.observers.append(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update()
