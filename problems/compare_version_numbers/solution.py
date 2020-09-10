class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        #if version1 > version2 return 1; 
        # if version1 < version2 return -1;
        #otherwise return 0.
        
        v1 = version1.split('.')
        v2 = version2.split('.')
        
        for i in range(max(len(v1),len(v2))):
            if i < len(v1):
                i_1 = int(v1[i])
            elif i >=len(v1):
                i_1 = 0
            if i < len(v2):
                i_2 = int(v2[i])
            else:
                i_2 = 0
            if i_1 != i_2:
                if i_1 > i_2:
                    return 1
                else:
                    return -1
        return 0 