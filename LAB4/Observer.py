from abc import ABC, abstractmethod
import unittest
from unittest.mock import Mock

# Тест для Наблюдателя
class TestObserver(unittest.TestCase):
    def test_shopping_cart_observers(self):
        cart = ShoppingCart()

        # Создаем Mock-объекты для наблюдателей
        observer1 = Mock()
        observer2 = Mock()

        # Добавляем Mock-объекты в корзину покупок в качестве наблюдателей
        cart.add_observer(observer1)
        cart.add_observer(observer2)

        # Добавляем товар в корзину и проверяем, что уведомления отправлены каждому наблюдателю
        cart.add_item("Shoes")
        observer1.update.assert_called_once_with("Item added: Shoes")
        observer2.update.assert_called_once_with("Item added: Shoes")

        # Удаляем товар и проверяем, что уведомления отправлены каждому наблюдателю
        cart.remove_item("Shoes")
        observer1.update.assert_called_with("Item removed: Shoes")
        observer2.update.assert_called_with("Item removed: Shoes")
# Наблюдатель
class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass

# Субъект - Корзина покупок
class ShoppingCart:
    def __init__(self):
        self._observers = []
        self._items = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)

    def add_item(self, item):
        self._items.append(item)
        self.notify_observers(f"Item added: {item}")

    def remove_item(self, item):
        if item in self._items:
            self._items.remove(item)
            self.notify_observers(f"Item removed: {item}")

    def display_items(self):
        return self._items

# Конкретный наблюдатель - Клиент магазина
class Customer(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} received message: {message}")

# Использование
cart = ShoppingCart()

customer1 = Customer("Alice")
customer2 = Customer("Bob")

cart.add_observer(customer1)
cart.add_observer(customer2)

cart.add_item("Laptop")
cart.add_item("Headphones")

cart.remove_item("Laptop")

unittest
