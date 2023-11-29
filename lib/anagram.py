
class Anagram:
    # Initializing the class

    def __init__(self, word):
        self.word = word

    def match(self,word_list):
        # An empty list to store the anagrams
        anagrams = []

        # Looping through the word list
        for potential_word in word_list:
            #Checking if word is the same as original and anagram of potential word
            if potential_word != self.word and self.is_word(potential_word):
                anagrams.append(potential_word)
        return anagrams
        
    # Method for sorting the list of letters

    def is_word(self, potential_word):

            #   Comparing the sorted letters
        return sorted ((potential_word).lower()) == sorted((self.word).lower())