class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for elem in strs:
            encoded += f'{len(elem)}#{elem}'
        
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        
        print(f"Encoded: {s}")

        i = 0
        while i < len(s):
            # collect chars until we hit a "#"
            # this is required for str larger than 9 (e.g. 10)
            strLengthAsString = ""

            while s[i] != "#":
                strLengthAsString += s[i]
                print(f"Building str length...: {strLengthAsString}")
                i += 1

            lengthOfStrLengthAsString = len(strLengthAsString)
            print(f"length of str length...: {lengthOfStrLengthAsString}")

            strLength = (int)(strLengthAsString)
            start = i + 1
            end = i + 1 + strLength

            print(f'Start index to slice: {start}')
            print(f'End index to slice: {end}')
            decoded.append(s[start : end])

            i += strLength + 1
            #print(f'Set Index to beginning of next string length: {i}, char = {s[i]}')
        
        return decoded
