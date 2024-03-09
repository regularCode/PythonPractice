class Solution(object):
    def numRollsToTarget(self, dices, faces, target):
        """
        :type n: int
        :type k: int
        :type target: int
        :rtype: int
        """

        def recursion(dice_no, target_so_far, mem):
            if dice_no > 0 and target_so_far == 0:
                return 0
            if target_so_far < 0:
                return 0
            if dice_no == 0:
                return 1 if target_so_far == 0 else 0
            if mem[dice_no][target_so_far] != -1:
                return mem[dice_no][target_so_far]
            ans = 0
            for i in range(1, faces + 1):
                ans = (ans + recursion(dice_no - 1, target_so_far - i, mem)) % 1000000007

            mem[dice_no][target_so_far] = ans
            return ans

        mem = [[-1 for _ in range(target + 1)] for _ in range(dices + 1)]

        return recursion(dices, target, mem)

    def numRoolsToTargetTab(self, dices, faces, target):
        mem = [[0 for _ in range(target + 1)] for _ in range(dices + 1)]

        mem[0][0] = 1

        for dice in range(1, dices+1):
            for targ in range(1, target+1):
                for face in range(1, faces+1):
                    if (targ - face) >= 0:
                        mem[dice][targ] = (mem[dice][targ] + mem[dice-1][targ-face]) % 1000000007

        return mem[dices][target]
