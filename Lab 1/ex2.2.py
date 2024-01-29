def vowel_checker(word, vowels): # function to check vowels in a text file
    return sum(char in vowels for char in word) # checks the list of vowels and checks the character in a word if it includes a vowel

word_counter = 0 # word counter used in avg numbers of vowels per word
vowel_counter = 0 # vowel counter used in avg numbers of vowels per word
vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y'] # list of vowels used in vowel checker

with open(r'pg2701.txt', 'r', encoding='utf-8') as file: #opening the file 
        for i, line in enumerate(file, 1):
            if i >= 41:     # starting the read at "CHAPTER 1. Loomings."
                words = line.split()
                word_counter += len(words)
                for word in words:
                    vowel_counter += vowel_checker(word.lower(), vowels)


average_vowels_per_word = vowel_counter / word_counter     

print(f'Average vowels per word starting from line 41: {average_vowels_per_word:.2f}')
    