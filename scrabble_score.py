scrabble_points = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1,
    'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8,
    'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1,
    'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1,
    'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
}

def calculate_word_score(word):
    "Calculate the total score of a word based on Scrabble point values."
    return sum(scrabble_points.get(letter.upper(), 0) for letter in word)

def main():
    print("Enter words to calculate Scrabble scores. Type 'quit' or 'q' to stop.")
    
    while True:
        word = input(">: ").strip()
        
        if word.lower() in ['quit', 'q']:
            break
        
        score = calculate_word_score(word)
        print(f"{word.upper()} is worth {score} points.")


if __name__ == "__main__":
    main()

