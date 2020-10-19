"""
Implement queue operations enqueue, dequeue, isEmpty, size and front.
Queue should store integers.

Queue size is initialized to 0
>>> que = Q()
>>> que.size()
0
>>> que.empty()
True

Enqueuing increases size by one
>>> que.enqueue(1)
>>> que.size()
1
>>> que.empty()
False
>>> que.enqueue(2)
>>> que.size()
2

Elements are added to queue in order
>>> [k for k in que]
[1, 2]

Head returns value of first element in queue
>>> que.head()
1

Dequeue returns value from top
>>> que.dequeue()
1

and pops it from queue
>>> [k for k in que]
[2]

Dequeue removes element from queue and set head correctly to next element
>>> que.size()
1
>>> que.head()
2

Dequeue from empty Q raises IndexError
>>> que.dequeue()
2
>>> que.empty()
True
>>> que.dequeue()
Traceback (most recent call last):
    ...
IndexError: Cannot dequeue from empty queue
"""

from dataclasses import dataclass
from typing import Any, Generator, Type

@dataclass
class Q_Element:
    _value: Any = None
    _next = None

    def set_next(self, next_object) -> None:
        self._next = next_object

class Q:
    def __init__(self):
        self._size: int = 0
        self._head = None
        self._tail = None

    def size(self) -> int:
        return self._size

    def empty(self) -> bool:
        return self.size() <= 0
    
    def head(self) -> Any:
        return self._head._value

    def enqueue(self, value: Any) -> None:
        if self.empty():
            self._head = Q_Element(value)
            self._tail = self._head
        else:
            temp = Q_Element(value)
            self._tail.set_next(temp)
            self._tail = temp
        self._size += 1

    def dequeue(self) -> Any:
        if self.empty():
            raise IndexError('Cannot dequeue from empty queue')
        else:
            ret_val: Any = self._head._value
            self._head = self._head._next
            self._size -= 1
            return ret_val

    def values(self) -> Generator[Any, None, None]:
        current_element = self._head
        while current_element is not None:
            yield current_element._value
            current_element = current_element._next

    def __iter__(self):
        yield from self.values()

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True, exclude_empty=True)
