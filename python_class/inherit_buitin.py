from dataclasses import dataclass, field

import srt as srt


@dataclass(order=True)
class Human:
    name: str
    age: int = field(default=0)
    gender: srt = field(default="F")
    children: list[str] = field(default_factory=lambda: [], init=False, repr=False)


human = Human("Tola", 25, "F")
alien = Human("David", 28, "M")

# human.name = "Dorcas"
print(human < alien)
print(human)




from dataclasses import dataclass, field

import srt as srt


@dataclass(order=True)
class Human:
    sort_by: tuple[int, str] = field(init=False, repr=False)
    name: str
    age: int = field(default=0)
    gender: srt = field(default="F")
    children: list[str] = field(default_factory=lambda: [], init=False, repr=False)

    def __post_init__(self):
        self.sort_by = (self.age, self.name)


human = Human("Tola", 25, "F")
alien = Human("David", 28, "M")

human.name = "Dorcas"
print(human < alien)
print(human)




from dataclasses import dataclass, field

import srt as srt


@dataclass(order=True)
class Human:
    sort_by: tuple[int, str] = field(init=False, repr=False)
    name: str
    age: int = field(default=0)
    gender: srt = field(default="F")
    children: list[str] = field(default_factory=lambda: [], init=False, repr=False)

    def __post_init__(self):
        self.sort_by = (self.age, self.name)


human = Human("Tola", 25, "F")
alien = Human("David", 28, "M")

human.name = "Dorcas"
print(human < alien)
print(human)
x = sorted([alien, human])
print(x)
