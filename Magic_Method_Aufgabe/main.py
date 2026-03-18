class auto:
    def __init__(self, ps):
        self.ps = ps
    
    def __add__(self):
        if not isinstance(other, auto):
            raise TypeError(f"Cannot add auto with {type(other).__name__}")
        return auto(self.ps + other.ps)
    
    def __sub__(self, other):
        if not isinstance(other, auto):
            raise TypeError(f"Cannot subtract {type(other).__name__} from auto")
        return auto(self.ps - other.ps)
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return auto(self.ps * other)
        elif isinstance(other, auto):
            return auto(self.ps * other.ps)
        else:
            raise TypeError(f"Cannot multiply auto with {type(other).__name__}")
    
    # Comparison Magic Methods
    def __eq__(self, other):
        if not isinstance(other, auto):
            return False
        return self.ps == other.ps
    
    def __lt__(self, other):
        if not isinstance(other, auto):
            raise TypeError(f"Cannot compare auto with {type(other).__name__}")
        return self.ps < other.ps
    
    def __gt__(self, other):
        if not isinstance(other, auto):
            raise TypeError(f"Cannot compare auto with {type(other).__name__}")
        return self.ps > other.ps
    
    def __str__(self):
        return f"Auto({self.ps}PS)"
    
    def __len__(self):
        return self.ps


def main(): 
    # Test __init__
    print("\n1. Initialization Tests:")
    a1 = auto(50)
    a2 = auto(60)
    print(f"   a1 = auto(50) -> {a1}")
    print(f"   a2 = auto(60) -> {a2}")
    
    # Test __str__ and __repr__
    print("\n2. String Representation Tests:")
    print(f"   str(a1) = {str(a1)}")
    print(f"   repr(a1) = {repr(a1)}")
    
    # Test __add__
    print("\n3. Addition Test (__add__):")
    a3 = a1 + a2
    print(f"   a1 + a2 = {a1} + {a2} = {a3}")
    print(f"   Expected: Auto(110PS)")
    
    # Test __sub__
    print("\n4. Subtraction Test (__sub__):")
    a4 = a2 - a1
    print(f"   a2 - a1 = {a2} - {a1} = {a4}")
    print(f"   Expected: Auto(10PS)")
    
    # Test __mul__
    print("\n5. Multiplication Tests (__mul__):")
    a5 = a1 * 2
    print(f"   a1 * 2 = {a1} * 2 = {a5}")
    a6 = 3 * a1
    print(f"   3 * a1 = 3 * {a1} = {a6}")
    a7 = a1 * a2
    print(f"   a1 * a2 = {a1} * {a2} = {a7}")
    
    # Test __eq__
    print("\n7. Equality Test (__eq__):")
    a8 = auto(50)
    print(f"   a1 == a8: {a1 == a8} (both 50PS)")
    print(f"   a1 == a2: {a1 == a2} (50PS vs 60PS)")
    
    # Test __lt__
    print("\n9. Less Than Test (__lt__):")
    print(f"   a1 < a2: {a1 < a2} (50 < 60)")
    print(f"   a2 < a1: {a2 < a1} (60 < 50)")
    
    # Test __gt__
    print("\n10. Greater Than Test (__gt__):")
    print(f"   a2 > a1: {a2 > a1} (60 > 50)")
    print(f"   a1 > a2: {a1 > a2} (50 > 60)")

    # Test Type Checking
    print("\n13. Type Checking Tests:")
    try:
        result = a1 + 10
    except TypeError as e:
        print(f"   a1 + 10:{e}")
    
    try:
        result = a1 - "text"
    except TypeError as e:
        print(f"   a1 - 'text':{e}")
    
    try:
        result = a1 < 50
    except TypeError as e:
        print(f"   a1 < 50:{e}")

if __name__ == "__main__":
    main()