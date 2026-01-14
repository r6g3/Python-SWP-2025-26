from __future__ import annotations

from gender import Gender


class Person:
    def __init__(self, first_name: str, last_name: str, gender: Gender) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
