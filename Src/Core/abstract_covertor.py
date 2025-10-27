from abc import ABC, abstractmethod

class abstract_covertor(ABC):

    @abstractmethod
    def Convert(self, obj) -> dict:
        """
        Конвертирует любой объект в словарь ключ: значение.
        """
        pass
