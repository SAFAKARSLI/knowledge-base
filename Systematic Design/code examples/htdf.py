
"""
Define a function that returns "even" or "odd" according to the given number.
"""


# 1. Signature, purpose and stub.
"""
 Signature: Number -> "String"
 Purpose:   Returns "even" if n%2 is zero, "odd" otherwise.
 Stub: def even_or_odd(n): return "a"
"""

# 3. Templates and inventory.
"""
def even_or_odd(n):
    if (n ...):
        return ...
    else:
        return ...
"""

# 4. Code the function body.
def even_or_odd(n):

    if (n % 2 == 0):
        print("even")
        return "even"
    else:
        print("odd")
        return "odd"


def main():
    print("Executing the " + repr(__name__))
    
    # 2. Define examples (unit tests)
    assert even_or_odd(1) == "odd"
    assert even_or_odd(2) == "even"
    assert even_or_odd(0) == "even"
    assert even_or_odd(2.2) == "odd"


if __name__ == "__main__":
    main()


