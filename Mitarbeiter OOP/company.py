from __future__ import annotations

from typing import List, Tuple

from department import Department
from employee import Employee
from gender import Gender


class Company:
    def __init__(self, name: str) -> None:
        self.name = name
        self._departments: List[Department] = []

    def add_department(self, department: Department) -> None:
        if department not in self._departments:
            self._departments.append(department)

    @property
    def departments(self) -> List[Department]:
        return list(self._departments)

    def _all_employees(self) -> List[Employee]:
        employees: List[Employee] = []
        seen_ids = set()

        for department in self._departments:
            for employee in department.employees:
                if id(employee) not in seen_ids:
                    seen_ids.add(id(employee))
                    employees.append(employee)

        return employees

    def employee_count(self) -> int:
        return len(self._all_employees())

    def department_head_count(self) -> int:
        count = 0
        for department in self._departments:
            if department.manager is not None:
                count += 1
        return count

    def department_count(self) -> int:
        return len(self._departments)

    def largest_department(self) -> Department | None:
        if not self._departments:
            return None
        return max(self._departments, key=lambda d: d.headcount())

    def gender_distribution(self) -> Tuple[float, float]:
        employees = self._all_employees()
        if not employees:
            return 0.0, 0.0

        male_count = sum(1 for e in employees if e.gender == Gender.MALE)
        female_count = sum(1 for e in employees if e.gender == Gender.FEMALE)
        total = len(employees)

        female_percent = (female_count / total) * 100
        male_percent = (male_count / total) * 100
        return female_percent, male_percent
