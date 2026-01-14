from __future__ import annotations

from company import Company
from department import Department
from employee import DepartmentHead, Employee
from gender import Gender


def build_sample_company() -> Company:
    """Erzeugt ein Beispiel-Firmenobjekt mit Abteilungen und Mitarbeitern."""

    company = Company("Beispielfirma GmbH")

    it = Department("IT")
    hr = Department("HR")
    sales = Department("Vertrieb")

    company.add_department(it)
    company.add_department(hr)
    company.add_department(sales)

    DepartmentHead("Anna", "Müller", Gender.FEMALE, it)
    DepartmentHead("Peter", "Maier", Gender.MALE, hr)
    DepartmentHead("Julia", "Schmidt", Gender.FEMALE, sales)

    Employee("Markus", "Klein", Gender.MALE, it)
    Employee("Sabine", "Huber", Gender.FEMALE, it)
    Employee("Thomas", "Gruber", Gender.MALE, hr)
    Employee("Maria", "Fischer", Gender.FEMALE, sales)
    Employee("Lukas", "Weber", Gender.MALE, sales)

    return company


def main() -> None:
    company = build_sample_company()

    print(f"Firma: {company.name}")
    print(f"Anzahl Abteilungen: {company.department_count()}")
    print(f"Anzahl Mitarbeiter (inkl. Abteilungsleiter): {company.employee_count()}")
    print(f"Anzahl Abteilungsleiter: {company.department_head_count()}")

    largest_department = company.largest_department()
    if largest_department is not None:
        print(
            "Größte Abteilung: "
            f"{largest_department.name} mit {largest_department.headcount()} Mitarbeitern"
        )

    female_percent, male_percent = company.gender_distribution()
    print(f"Frauenanteil: {female_percent:.1f}%")
    print(f"Männeranteil: {male_percent:.1f}%")


if __name__ == "__main__":
    main()