# Count characters of first string in hashtable
# Count characters of second string in another hashtable
# If character frequencies are the same => Valid Anagram 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # base case
        if len(s) != len(t):
            return False

        s_Dic, t_Dic = {}, {}

        for i in range(len(s)):
            s_Dic[s[i]] = s_Dic.get(s[i], 0) + 1 # add one the current count
            t_Dic[t[i]] = t_Dic.get(t[i], 0) + 1
        
        return s_Dic == t_Dic