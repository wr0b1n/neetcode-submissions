# --------------First idea:
# track hashmap (key = unique string of input, value = List[str] = anagrams)
# iterate strings: O(m)
# --> iterate hashmap: O(m)
# ----> check if hashmap key is anagram of string 
# ----> yes: add string to values list of that key
# ----> no: add new key with string and values list of one entry of that string
# build result by iterating hashmap
# ----> add values of each key to combined list

# --------------Better idea:
# iterate strings: O(m)
# --> iterate characters in string: O(n)
# ----> build a dictionary from string called: charCounts
# ----> add charCounts to hashmap, as key and value = string, or extended value list of existing key with string
# build result by iterating hashmap: O(m)
# ----> add values of each key to combined list
# => Total time complexity = O(m*n + m) = O(m*n)
# => Total space complexity = O(m*n), worst case means only distinct words which are no anagrams


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        
        result = []
        dic = {}

        for word in strs:
            wordCounts = self.getCharHashmap(word)
            # Convert the dictionary items to a sorted tuple so it can be used as a hashable key
            key = tuple(sorted(wordCounts.items()))
            if key in dic:
                dic[key].append(word)
            else:
                dic[key] = [word]

        # build result
        for key in dic.keys():
            result.append(dic[key])

        return result

    def getCharHashmap(self, word: str) -> Dict[str, int]:
        dic = {}

        for c in word:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1
        
        return dic
        



