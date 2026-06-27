# Count characters of first string in hashtable
# Remove occuring characters of second string from hashtable
# If Hashtable is empty in the end => Valid Anagram 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # base case
        if len(s) != len(t):
            return False

        dic = {}
        for c in s:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1

        print(dic)

        for c in t:
            if c in dic:
                dic[c] -= 1
                if dic[c] == 0:
                    dic.pop(c)
            else:
                return False

        if dic == {}:
            return True

        return False