
def vowel_checker(word) #checks and iterates over a word for a vowel. If a vowel, is found add +1 to the vowel counter
    
    return any(char in vowels for char in word)


#create a loop or something to make file read starting at line 41
with open(r'pg2701.txt', 'r') as file:
    word_counter = 0
    vowel_counter = 0
    vowels = ['a','A','e','E','i','I','o','O','u','U','y','Y']


     for i, line in enumerate(file.readlines(), 0):
          if i >= 41
            words = line.split()
            for word in words:
                if vowel_checker(word):
                    vowel_counter += 1


    data = file.read()
    lines = data.split()


        
        
        # Iterate through the words in each line
        



#output
    average_vowels_per_word = vowel_counter / word_counter
    print(f"Average vowels per word: {average_vowels_per_word:.2f}")