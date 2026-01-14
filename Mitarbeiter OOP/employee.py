from __future__ import annotations

from typing import Optional

from gender import Gender
from person import Person


class Employee(Person):
    def __init__(
        self,
        first_name: str,
        last_name: str,
        gender: Gender,
        department: "Department | None" = None,
    ) -> None:
        super().__init__(first_name, last_name, gender)
        self.department: "Department | None" = None

        if department is not None:
            department.add_employee(self)


class DepartmentHead(Employee):
    def __init__(
        self,
        first_name: str,
        last_name: str,
        gender: Gender,
        department: "Department | None" = None,
    ) -> None:
        super().__init__(first_name, last_name, gender)

        if department is not None:
            department.set_manager(self)
