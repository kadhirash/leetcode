class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # hash map to keep track of key, val
        # if common prefix, return prefix
            # else return -1 
        
        
        result = [ ]
        
        for i in zip(*strs):
            if len(set(i)) != 1:
                break
            result.append(i[0])
        return ''.join(result)
        