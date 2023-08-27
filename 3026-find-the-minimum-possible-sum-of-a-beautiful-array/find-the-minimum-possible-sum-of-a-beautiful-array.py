class Solution(object):
    def minimumPossibleSum(self, n, target):
        """
        :type n: int
        :type target: int
        :rtype: int
        """
        arr = [0] * n
        total = n * (n + 1) // 2
        print(total)
        for i in range(n):
            arr[i] = i + 1
        L = 0
        R = n - 1
        while L < R:
            t = arr[L] + arr[R]
            if t == target:
                if target <= n:
                    to_add = arr[-1] + 1
                else:
                    to_add = max(target, arr[-1] + 1)
                total += to_add - arr[R]
                arr.append(to_add)
                L += 1
                R -= 1
            elif t < target:
                L += 1
            else:
                R -= 1
        return total    