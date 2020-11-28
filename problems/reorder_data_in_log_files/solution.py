class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        res = []
        # get the letter-log first
        for string in logs:
            if string.split()[1].isalpha():
                res.append(string)
        # sort the letter-log 
        res.sort(key = lambda x: (x.split()[1:], x.split()[0]))
        # get the digits-log using its original order
        for log in logs:
            if log.split()[1].isdigit():
                res.append(log)
        return res