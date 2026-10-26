class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        combinations = []
        combination = []

        def backtrack(target, index):
            if target == 0:
                combinations.append(combination.copy())
                return
            if index == len(candidates) or target < 0:
                return

            # notInclude
            nextIndex = index + 1
            while nextIndex < len(candidates) and candidates[index] == candidates[nextIndex]:
                nextIndex += 1
            backtrack(target, nextIndex)

            # include
            combination.append(candidates[index])
            backtrack(target - candidates[index], index + 1)
            combination.pop()

        backtrack(target, 0)
        return combinations