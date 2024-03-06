import collections
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

anagrams = collections.defaultdict(list)
for word in strs:
    count = [0] * 26  # Count occurrences of each character
    for char in word:
        count[ord(char) - ord('a')] += 1
        # Convert count to a tuple to use as a key in the dictionary
    key = tuple(count)
    anagrams[key].append(word)

print(anagrams)

