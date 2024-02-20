
"""
    1. Signature, Purpose, stud.
    2. Define examples (unit tests)
    3. Template and inventory
    4. Code the function body.
    5. Debug and refine.
"""



# (Signature) String -> String
# (Purpose)   Define a function that pluralizes the given word. (Appends "s" to it.)
def pluralize(word): 
    return word + "s"


def main():
    # Define Examples (unit tests)
    assert pluralize("pencil") == "pencils"
    assert pluralize("word") == "words"
    print("Success")



if __name__ == "__main__":
    main()