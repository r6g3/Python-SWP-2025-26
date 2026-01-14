from __future__ import annotations

from typing import List, Optional

from employee import Employee, DepartmentHead


class Department:
    def __init__(self, name: str) -> None:
        self.name = name
        self._employees: List[Employee] = []
        self._manager: Optional[DepartmentHead] = None

    def add_employee(self, employee: Employee) -> None:
        if employee not in self._employees:
            self._employees.append(employee)
            employee.department = self

    def set_manager(self, manager: DepartmentHead) -> None:
        if self._manager is not None and self._manager is not manager:
            raise ValueError("Diese Abteilung hat bereits einen Abteilungsleiter.")

        self._manager = manager
        if manager not in self._employees:
            self._employees.append(manager)
        manager.department = self

    @property
    def manager(self) -> Optional[DepartmentHead]:
        return self._manager

    @property
    def employees(self) -> List[Employee]:
        return list(self._employees)

    def headcount(self) -> int:
        return len(self._employees)
