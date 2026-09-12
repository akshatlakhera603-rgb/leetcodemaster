class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def solve(i, curr, total):

            if total == target:
                ans.append(curr.copy())
                return

            if i == len(candidates) or total > target:
                return

            # INCLUDE
            curr.append(candidates[i])
            solve(i, curr, total + candidates[i])
            curr.pop()

            # EXCLUDE
            solve(i + 1, curr, total)

        solve(0, [], 0)

        return ans