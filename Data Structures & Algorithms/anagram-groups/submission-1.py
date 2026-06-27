# --------------1. idea:
# track hashmap (key = unique string of input, value = List[str] = anagrams)
# iterate strings: O(m)
# --> iterate hashmap: O(m)
# ----> check if hashmap key is anagram of string 
# ----> yes: add string to values list of that key
# ----> no: add new key with string and values list of one entry of that string
# build result by iterating hashmap
# ----> add values of each key to combined list

# --------------2. idea:
# iterate strings: O(m)
# --> iterate characters in string: O(n)
# ----> build a dictionary from string called: charCounts
# ----> add charCounts to hashmap, as key and value = string, or extended value list of existing key with string
# build result by iterating hashmap: O(m)
# ----> add values of each key to combined list
# => Total time complexity = O(m*n + m) = O(m*n)
# => Total space complexity = O(m*n), worst case means only distinct words which are no anagrams

# --------------3. idea:
# use 2. idea but make a change
# dictionaries are not hashable, therefore dont use a dic with character counts as a key
# instead use a fixed size array with 26 entries (chars a-z)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        
        result = []
        dic = {}

        for word in strs:
            wordCounts = self.getCharCountArray(word)
            if wordCounts in dic:
                dic[wordCounts].append(word)
            else:
                dic[wordCounts] = [word]

        # build result
        for key in dic.keys():
            result.append(dic[key])

        return result

    def getCharCountArray(self, word: str):
        counts = [0]*26
        asciiOrderLowerCaseA = 97

        for c in word:
            counts[asciiOrderLowerCaseA - ord(c)] += 1
        
        return tuple(counts)
        



