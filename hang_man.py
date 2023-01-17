import random
import string 


random_word_list = ['booger', 'bacon', 'protein', 'notepad', 'silver', 'sneakers', 'boots', 'apple', 'watermelon', 'socks']

class Hangman():
    def __init__(self):
        self.guessed_letters = []
        
    
    
    def user(self):
        
        attempts = 7
        
        secret_word = random.choice(random_word_list)
        
        hidden_word = ' _' * len(secret_word)
        
        alphabet = set(string.ascii_lowercase)
        
        print(secret_word)
        print(hidden_word)
        
        
        secret_word_letters = set(secret_word)
        
        used_letters = set()
        
        
        
        while len(secret_word_letters) > 0 and attempts > 0:
            
            print (f'You have, {attempts} attempts, and you have used these letters: ', ''.join(used_letters))
            
            
            word_list = [letter if letter in used_letters else '-' for letter in secret_word]
            
            print(word_list)
            
            
            guessed_letters = input("what letter will you guess this time?").lower()
            
            if guessed_letters in alphabet - used_letters:
                used_letters.add(guessed_letters)
                
                if guessed_letters in secret_word_letters:
                    secret_word_letters.remove(guessed_letters)
                    
                else:
                    attempts = attempts - 1
                    print('That letter is not in the word.' )
            
            elif guessed_letters in used_letters:
                print("You already guessed that letter. Try again.")
                
            else:
                print("Invalid character. Try again.")
        
        if attempts == 0:
            print(f'Ran out of attempts. The word was {secret_word}. Game Over.')
            
        else:
            print(f'You guessed the word, {secret_word}!!')
  
        
hangman = Hangman()

hangman.user()
        
        
    



