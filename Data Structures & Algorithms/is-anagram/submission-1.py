class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
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