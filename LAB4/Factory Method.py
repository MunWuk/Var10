from abc import ABC, abstractmethod
import unittest

# Тест для Фабричного метода
class TestFactoryMethod(unittest.TestCase):
    def test_book_creation(self):
        creator = BookStore()
        product = creator.create_product()
        self.assertIsInstance(product, Book)
        self.assertEqual(product.display_info(), "Book: The Great Gatsby by F. Scott Fitzgerald")


# Продукт - Товар в интернет-магазине
class Product(ABC):
    @abstractmethod
    def display_info(self):
        pass

# Конкретный продукт - Книга
class Book(Product):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        return f"Book: {self.title} by {self.author}"

# Конкретный продукт - Электронное устройство
class ElectronicDevice(Product):
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand

    def display_info(self):
        return f"Electronic Device: {self.brand} {self.name}"

# Создатель - Интернет-магазин
class OnlineStore(ABC):
    @abstractmethod
    def create_product(self):
        pass

    def sell_product(self):
        product = self.create_product()
        result = f"Online Store sold: {product.display_info()}"
        return result

# Конкретный создатель - Интернет-магазин книг
class BookStore(OnlineStore):
    def create_product(self):
        return Book("The Great Gatsby", "F. Scott Fitzgerald")

# Конкретный создатель - Интернет-магазин электронных устройств
class ElectronicsStore(OnlineStore):
    def create_product(self):
        return ElectronicDevice("Smartphone", "Samsung")

# Использование
book_store = BookStore()
book_result = book_store.sell_product()
print(book_result)

electronics_store = ElectronicsStore()
electronics_result = electronics_store.sell_product()
print(electronics_result)

unittest
