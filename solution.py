class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max = 0
        for x in range(len(accounts)):
            total = 0
            for i in range(len(accounts[x])):
                total= total + accounts[x][i]
            if total > max:
                max = total
        return max
