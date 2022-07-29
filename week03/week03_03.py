from abc import ABC, abstractmethod


# class Engine:
#     pass


class ObservableEngine(Engine):
    def __init__(self):
        self.subscribes = set()

    def subscribe(self, subscriber):
        self.subscribes.add(subscriber)

    def unsubscribe(self, subscriber):
        if subscriber in self.subscribes:
            self.subscribes.remove(subscriber)

    def notify(self, message):
        for subscriber in self.subscribes:
            subscriber.update(message)


class AbstractObserver(ABC):
    @abstractmethod
    def update(self, message):
        pass


class ShortNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = set()

    def update(self, message):
        self.achievements.add(message["title"])


class FullNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = list()

    def update(self, message):
        if message not in self.achievements:
            self.achievements.append(message)


# notifier1 = ShortNotificationPrinter()
# printer1 = FullNotificationPrinter()
#
# manager = ObservableEngine()
#
# manager.subscribe(notifier1)
# manager.subscribe(printer1)
#
# manager.notify({"title": "Покоритель", "text": "Дается при выполнении всех заданий в игре"})
