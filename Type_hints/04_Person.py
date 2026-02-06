from __future__ import annotations
from dataclasses import dataclass, field


@dataclass
class Person:
    name: str
    age: int
    addresses: dict[int, Address] = field(default_factory=dict)

class Address:
    pass

p1 = Person('joao', 18)
print(p1)