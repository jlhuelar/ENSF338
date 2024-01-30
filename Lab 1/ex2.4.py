import timeit

def vowel_checker(word, vowels):
    return sum(char in vowels for char in word)

def calculate_average_vowels():
    word_counter = 0
    vowel_counter = 0
    vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
    
    with open(r'Lab 1/pg2701.txt', 'r', encoding='utf-8') as file:
        for i, line in enumerate(file, 1):
            if i >= 41:
                words = line.split()
                word_counter += len(words)
                for word in words:
                    vowel_counter += vowel_checker(word.lower(), vowels)

    average_vowels_per_word = vowel_counter / word_counter
    return average_vowels_per_word

# Time the code execution 100 times excluding file reading and printing
repetitions = 100
execution_time = timeit.timeit(calculate_average_vowels, number=repetitions)

# Calculate the average time per execution
average_time_per_execution = execution_time / repetitions

print(f'Average time per execution (over {repetitions} repetitions): {average_time_per_execution:.6f} seconds')