# e.g. [1, 3, 7, 9, 13] => target = 12

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        L,R = 0,n-1

        result = numbers[L] + numbers[R]

        while L <= R and result != target:
            if result == target:
                break;

            if result > target:
                R -= 1
            else:
                L += 1

            result = numbers[L] + numbers[R]

        return [L+1, R+1]

        