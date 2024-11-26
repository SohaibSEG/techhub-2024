
def find_next(char, word, pattern):
    for i in range(len(word)):
        if word[i] == char and pattern[i] == "*":
            return i
    return -1

def guess( char, word, pattern):
    index = find_next(char, word, pattern)
    if index == -1:
        return None
    pattern[index] = char
    return pattern

word = "Hello"
pattern = "*" * len(word)

print(f"Guess the hidden word in : {pattern} World")

while "*" in pattern:
    char = input("Enter a character: ")
    new_pattern = guess( char, list(word), list(pattern))
    if new_pattern is None:
        print("Character not in the word")
    else:
        pattern = new_pattern
        print(f"Guess the hidden word in : {''.join(pattern)} World")
        
        