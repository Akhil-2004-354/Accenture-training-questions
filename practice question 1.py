
S = input("Enter a string: ")
C = input("Enter a character to search: ")

def count_characters(S, C):
    return S.count(C)

result = count_characters(S, C)
print(f"The character {C} occurs {result} times.")