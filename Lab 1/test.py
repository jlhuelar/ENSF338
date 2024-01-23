def count_vowels(word):
    vowels = "AEIOUaeiou"
    return sum(1 for char in word if char in vowels)

with open(r'pg2701.txt', 'r') as file: #error file cannot open
    total_words = 0
    total_vowels = 0
    
    # Skip lines until reaching line 41
    for _ in range(40):
        file.readline()
    
    # Read the file from line 41 onwards
    for line in file:
        # Split each line into words
        words = line.split()
        
        # Iterate through the words in each line
        for word in words:
            total_words += 1
            total_vowels += count_vowels(word)

# Calculate the average number of vowels per word
if total_words > 0:
    average_vowels_per_word = total_vowels / total_words
    print(f"Average vowels per word: {average_vowels_per_word:.2f}")