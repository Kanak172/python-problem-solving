class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        s = "".join(str(i) for i in range(1, n+1))

        perms = {i+1: "".join(p) for i,p in enumerate(permutations(s))}

        for key, value in perms.items():
            if key == k:
                return value
        