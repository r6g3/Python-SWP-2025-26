def main ():
    names = ["Anna", "Bernd", "Claudia", "Dirk", "Eva"]
    ages = [23, 17, 34, 15, 29]
    scores = [88, 92, 75, 64, 91]

    #Erzeuge aus diesen Listen eine gefilterte Liste von Personen, die folgende Bedingungen erfüllt:
    #Alter ≥ 18 und Score ≥ 80
    # müssen verwendet werden:
    # zip – kombiniere die drei Listen so, dass jeder Eintrag ein Tupel (name, age, score) ist.
    # filter + lambda – filtere alle Personen heraus, die beide Bedingungen erfüllen.
    # map + lambda – forme jedes Tupel in ein Dictionary der Form
    # {"name": ..., "age": ..., "score": ...} um.
    # {"name": "Anna", "age": 23, "score": 88}

    combined = zip(names, ages, scores)
    filtered = filter(lambda person: person[1] >= 18 and person[2] >= 80, combined)
    result = dict(map(lambda person: {"name": person[0], "age": person[1], "score": person[2]}, filtered))
    
    print(result)            

if __name__ == "__main__":
    main()