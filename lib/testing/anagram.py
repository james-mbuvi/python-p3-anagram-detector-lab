# # your code goes here!
# class Anagram:
#     def __init__(self, word):
#         self.word = word



#     def match(self, words):
#         anagram = []

#     for w in words :
#         if  

            
#     pass


class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, words):
        anagrams = []
        for w in words:
            if sorted(w.lower()) == sorted(self.word) and w.lower() != self.word:
                anagrams.append(w)
        return anagrams
