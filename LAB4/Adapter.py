from abc import ABC, abstractmethod
import unittest
from unittest.mock import MagicMock

# Тест для Адаптера
class TestAdapter(unittest.TestCase):
    def test_payment_adapter(self):
        # Создаем Mock-объект для стороннего сервиса
        third_party_service_mock = MagicMock()
        third_party_service_mock.process_payment.return_value = "Mocked payment processed successfully"

        # Используем Mock-объект в адаптере
        adapter = PaymentAdapter(third_party_service_mock)

        # Проверяем, что метод адаптера вызывает метод Mock-объекта
        result = adapter.process_payment()
        self.assertEqual(result, "Adapter: Mocked payment processed successfully")
        third_party_service_mock.process_payment.assert_called_once()


# Существующий класс стороннего сервиса для обработки платежей
class ThirdPartyPaymentService:
    def process_payment(self):
        return "Payment processed successfully by third-party service"

# Целевой интерфейс нашей системы платежей
class PaymentSystem(ABC):
    @abstractmethod
    def process_payment(self):
        pass

# Адаптер для интеграции стороннего сервиса с нашей системой
class PaymentAdapter(PaymentSystem):
    def __init__(self, third_party_service):
        self.third_party_service = third_party_service

    def process_payment(self):
        return f"Adapter: {self.third_party_service.process_payment()}"

# Использование
third_party_service = ThirdPartyPaymentService()
payment_adapter = PaymentAdapter(third_party_service)

result = payment_adapter.process_payment()
print(result)

unittest
