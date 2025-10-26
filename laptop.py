# from dataclasses import dataclass
# from enum import Enum
# from typing import List, Dict, Tuple


# class OperatingSystem(Enum):
#     MACOS = "macOS"
#     ARCH = "Arch Linux"
#     UBUNTU = "Ubuntu"
# @dataclass(frozen=True)

# class Person:
#     name: str
#     age: int
#     preferred_operating_system: tuple[OperatingSystem, ...]

# @dataclass(frozen=True)
# class Laptop:
#     id: int
#     manufacturer: str
#     model: str
#     screen_size_in_inches: float
#     operating_system: OperatingSystem

# def allocate_laptops(people: List[Person], laptops: List[Laptop]) -> Dict[Person, Laptop]:
#     sadness_list: List[Tuple[int, Person, Laptop]] = []
#     for person in people:
#         for laptop in laptops:
#             if laptop.operating_system in person.preferred_operating_system:
#                 sadness = person.preferred_operating_system.index(laptop.operating_system)
#             else:
#                 sadness = 100
#             sadness_list.append((sadness, person, laptop))

#     sadness_list.sort(key=lambda x: x[0])
#     allocations: Dict[Person, Laptop] = {}
#     allocated_laptops = set()

#     for sadness, person, laptop in sadness_list:
#         if person not in allocations and laptop.id not in allocated_laptops:
#             allocations[person] = laptop
#             allocated_laptops.add(laptop.id)

#     return allocations





# # sample
# people = [
#     Person("Imran", 22, (OperatingSystem.UBUNTU, OperatingSystem.ARCH, OperatingSystem.MACOS)),
#     Person("Eliza", 34, (OperatingSystem.ARCH, OperatingSystem.UBUNTU)),
# ]
# laptops = [
#     Laptop(1, "Dell", "XPS 13", 13, OperatingSystem.ARCH),
#     Laptop(2, "Apple", "MacBook", 13, OperatingSystem.MACOS),
#     Laptop(3, "Dell", "XPS 15", 15, OperatingSystem.UBUNTU),
# ]
# allocations = allocate_laptops(people, laptops)
# for person, laptop in allocations.items():
#     print(f"{person.name} gets {laptop.manufacturer} {laptop.model} ({laptop.operating_system.value})")

import sys
from dataclasses import dataclass
from enum import Enum
from typing import List
from collections import Counter


class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"

    @classmethod
    def from_string(cls, s: str):
        for os in cls:
            if os.value.lower() == s.lower():
                return os
        raise ValueError(f"Unsupported operating system: {s}")


@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_system: OperatingSystem


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem


def find_possible_laptops(laptops: List[Laptop], person: Person) -> List[Laptop]:
    return [laptop for laptop in laptops if laptop.operating_system == person.preferred_operating_system]


def main():
    # Existing inventory
    laptops = [
        Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
        Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
        Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
        Laptop(id=4, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
    ]

    # Read and validate user input
    try:
        name = input("Enter your name: ").strip()
        if not name:
            raise ValueError("Name cannot be empty.")

        age_input = input("Enter your age: ").strip()
        age = int(age_input)
        if age <= 0:
            raise ValueError("Age must be a positive integer.")

        print("Available operating systems:")
        for os in OperatingSystem:
            print(f"- {os.value}")
        os_input = input("Enter your preferred operating system: ").strip()
        preferred_os = OperatingSystem.from_string(os_input)

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    # Create the person
    person = Person(name=name, age=age, preferred_operating_system=preferred_os)

    # Check availability
    possible_laptops = find_possible_laptops(laptops, person)
    print(f"\nThere are {len(possible_laptops)} laptops available with {preferred_os.value}.")

    # Count OS distribution
    os_counts = Counter(laptop.operating_system for laptop in laptops)
    most_common_os, most_common_count = os_counts.most_common(1)[0]

    if most_common_os != preferred_os and most_common_count > len(possible_laptops):
        print(f"Note: There are more laptops available with {most_common_os.value} ({most_common_count} total).")
        print(f"If you're willing to accept {most_common_os.value}, you're more likely to get a laptop.")


if __name__ == "__main__":
    main()