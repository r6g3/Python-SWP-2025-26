# Übungsaufgaben für Comprehensions
# List-, Set- und Dict-Comprehensions mit verschiedenen Bedingungen

"""
LIST COMPREHENSION SYNTAX:

1. Grundform (ohne Bedingung):
   [expression for item in iterable]
   Beispiel: [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

2. Mit if-Bedingung (Filter):
   [expression for item in iterable if condition]
   Beispiel: [x**2 for x in range(10) if x % 2 == 0]  # [0, 4, 16, 36, 64]

3. Mit if-else (Conditional Expression):
   [expression_if_true if condition else expression_if_false for item in iterable]
   Beispiel: [x**2 if x % 2 == 0 else x*3 for x in range(5)]  # [0, 3, 4, 9, 16]

Merke:
- Bei if-else steht die Bedingung VOR dem 'for'
- Bei if (Filter) steht die Bedingung NACH dem 'for'
- if-else ändert den Wert, if filtert Elemente heraus
"""

def comprehension_exercises():
    print("=== COMPREHENSION ÜBUNGEN ===\n")
    
    # Beispieldaten für die Übungen
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    words = ["python", "java", "javascript", "go", "rust", "c++", "swift"]
    people = [
        {"name": "Anna", "age": 25, "city": "Wien"},
        {"name": "Bob", "age": 17, "city": "Graz"},
        {"name": "Clara", "age": 30, "city": "Wien"},
        {"name": "David", "age": 16, "city": "Linz"},
        {"name": "Eva", "age": 22, "city": "Salzburg"}
    ]
    
    print("--- AUFGABE 1: LIST COMPREHENSIONS ---")
    print("a) Ohne Bedingung: Quadriere alle Zahlen von 1-10")
    # TODO: Erstelle eine List Comprehension für [1², 2², 3², ..., 10²]
    squares = [val**2 for val in numbers]
    print(squares)

    print("\nb) Mit if: Nur gerade Zahlen quadrieren")
    # TODO: Quadriere nur die geraden Zahlen
    even_squares = [x**2 for x in numbers if x % 2 == 0]  # HIER DEINE LÖSUNG
    print(even_squares)
    
    print("\nc) Mit if-else: Quadriere gerade Zahlen, ungerade Zahlen * 3")
    # TODO: Gerade Zahlen quadrieren, ungerade * 3
    mixed_operation = [x**2 if x % 2 == 0 else x*3 for x in numbers]  # HIER DEINE LÖSUNG
    print(f"Gemischte Operation: {mixed_operation}")
    
    print("\n--- AUFGABE 2: SET COMPREHENSIONS ---")
    print("a) Ohne Bedingung: Länge aller Wörter")
    # TODO: Set mit den Längen aller Programmiersprachen
    word_lengths = {len(word) for word in words}  # HIER DEINE LÖSUNG
    print(f"Wortlängen: {word_lengths}")
    
    print("\nb) Mit if: Nur Wörter mit mehr als 4 Buchstaben (Längen)")
    # TODO: Längen nur von Wörtern mit mehr als 4 Buchstaben
    long_word_lengths = {len(word) for word in words if len(word)> 4}
    print(f"Lange Wortlängen: {long_word_lengths}")
    
    print("\nc) Mit if-else: Erste 3 Buchstaben wenn kurz, letzten 3 wenn lang")
    # TODO: Erste 3 Buchstaben wenn ≤ 5 Zeichen, sonst letzte 3
    word_parts = {word[:3] if len(word) <= 5 else word[-3:] for word in words}  # HIER DEINE LÖSUNG
    print(f"Wortteile: {word_parts}")
    
    print("\n--- AUFGABE 3: DICT COMPREHENSIONS ---")
    print("a) Ohne Bedingung: Name -> Alter für alle Personen")
    # TODO: Dictionary {name: age} für alle Personen
    name_age = {person['name']: person['age'] for person in people} # HIER DEINE LÖSUNG
    print(f"Name-Alter: {name_age}")
    
    print("\nb) Mit if: Nur erwachsene Personen (≥18) Name -> Stadt")
    # TODO: Dictionary {name: city} nur für Personen ≥ 18 Jahre
    adults_city = {person['name']: person['city'] for person in people if person["age"] >= 18}  # HIER DEINE LÖSUNG
    print(f"Erwachsene-Stadt: {adults_city}")
    
    print("\nc) Mit if-else: Name -> 'adult' oder 'minor'")
    # TODO: {name: 'adult' if age >= 18 else 'minor'}
    age_category = {person["name"]: "adult" if person["age"] >= 18 else "minor" for person in people}  # HIER DEINE LÖSUNG
    print(f"Alterskategorie: {age_category}")
    
    print("\n--- BONUS AUFGABEN (schwieriger) ---")
    print("BONUS 1: Verschachtelte List Comprehension")
    # TODO: Liste aller Buchstaben aus allen Wörtern (ohne Duplikate)
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # TODO: Alle Zahlen aus der Matrix in einer Liste
    flattened = []  # HIER DEINE LÖSUNG
    print(f"Flache Liste: {flattened}")
    
    print("\nBONUS 2: Komplexe Dict Comprehension")
    # TODO: Stadt -> Liste aller Personen aus dieser Stadt
    city_people = {}  # HIER DEINE LÖSUNG
    print(f"Stadt-Personen: {city_people}")

def show_solutions():
    """Hier sind die Lösungen - erst versuchen, dann schauen!"""
    print("\n=== LÖSUNGEN ===")
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    words = ["python", "java", "javascript", "go", "rust", "c++", "swift"]
    people = [
        {"name": "Anna", "age": 25, "city": "Wien"},
        {"name": "Bob", "age": 17, "city": "Graz"},
        {"name": "Clara", "age": 30, "city": "Wien"},
        {"name": "David", "age": 16, "city": "Linz"},
        {"name": "Eva", "age": 22, "city": "Salzburg"}
    ]
    
    print("LIST COMPREHENSIONS:")
    print(f"a) Quadrate: {[x**2 for x in numbers]}")
    print(f"b) Gerade Quadrate: {[x**2 for x in numbers if x % 2 == 0]}")
    print(f"c) Gemischt: {[x**2 if x % 2 == 0 else x*3 for x in numbers]}")
    
    print("\nSET COMPREHENSIONS:")
    print(f"a) Wortlängen: {{len(word) for word in words}}")
    print(f"b) Lange Wortlängen: {{len(word) for word in words if len(word) > 4}}")
    print(f"c) Wortteile: {{word[:3] if len(word) <= 5 else word[-3:] for word in words}}")
    
    print("\nDICT COMPREHENSIONS:")
    name_age_solution = {person['name']: person['age'] for person in people}
    adults_city_solution = {person['name']: person['city'] for person in people if person['age'] >= 18}
    age_category_solution = {person['name']: ('adult' if person['age'] >= 18 else 'minor') for person in people}
    
    print(f"a) Name-Alter: {name_age_solution}")
    print(f"b) Erwachsene-Stadt: {adults_city_solution}")
    print(f"c) Alterskategorie: {age_category_solution}")

def main():
    comprehension_exercises()
    
    # Uncomment the next line to see solutions
    # show_solutions()

if __name__ == "__main__":
    main()