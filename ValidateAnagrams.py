def anagram(word1,word2):
    word1=word1.lower()
    word2=word2.lower()
    return sorted(word1)==sorted(word2)
print(anagram("cool","loco"))
print(anagram("men","women"))

'''An Anagram is a word or phrase that forms a different word or phrase when the letters of a word are rearranged.
 For example, the words “despair” and “praised” are anagrams. The validation of anagram words is one of the 
 favourite questions in coding interviews. The idea is to write an algorithm to check if the input word 
 creates a meaningful word when rearranged. So to validate an anagram using Python, 
 we need to input two words and check if word1 in any case matches word2 after rearranging the words. 
 Here is how to validate anagrams using Python: '''