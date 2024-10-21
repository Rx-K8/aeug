from abc import ABC, abstractmethod


class SearcherBase(ABC):
    @abstractmethod
    def search(self, query):
        raise NotImplementedError
