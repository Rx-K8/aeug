from abc import ABC, abstractmethod


class BaseSearcher(ABC):
    @abstractmethod
    def search(self, query):
        raise NotImplementedError
