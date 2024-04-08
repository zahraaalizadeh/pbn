from abc import ABC, abstractmethod


# Since Python doesn't enforce interfaces, we can use an abstract class
# to achieve a similar result.
class IComparable(ABC):
    @abstractmethod
    def compareTo(self, other):
        pass


class IHashable(ABC):
    @abstractmethod
    def getKey(self) -> str:
        pass


# Python allows a class to inherit from multiple abstract classes.
class IHeapItem(IComparable, IHashable):
    pass


# For the IMap, Python's dict type inherently provides the functionality,
# so we might not need a direct translation.
