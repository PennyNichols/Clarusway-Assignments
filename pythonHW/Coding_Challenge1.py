# sort a list of strings into groups of Anagrams
# words spelled using the same letters in a different order
# display each Anagram group as a separate list inside of a list
# desired output: [['eat', 'tea', 'ate'],['tan', 'nat'],['bat'],['cat', 'tac']]
# output lists can be in any order

strs = ["eat", "tea", "tan", "ate", "nat", "bat", "cat", "tac"]

# sort each word one at a time, if sorted word is not already a sorted key, add key and value to dict
# if sorted word is already key, add to value 

d = {}

for word in strs :
    sorted_key = "".join(sorted(word))  # joining with empty string gives list of words instead of list of letters of word

    if sorted_key in d :
        d[sorted_key].append(word)
    else :
        d[sorted_key] = [word]
print(list(d.values()))