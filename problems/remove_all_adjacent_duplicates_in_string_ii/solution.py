class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # Clarifications:
            # the answer is unique
            # s only consists of lower case english letters
        # To Do:
            # return s w/o duplicates
        # Example:
            # deeedbbcccbdaa, k = 3     # remove e
                # ddbbcccbdaa           # remove c
                # ddbbbdaa              # remove b
                # dddaa                 # remove d
                # aa
        
        # Strategy:
            # Use a stack to hold string
                # Have a tuple in the stack (char, counter)
            # iterate through the string
                # when comparing the [-1][0] increment counter
                    # if [-1][1] == k, then pop off k amount
            # else append 
            # make stack -> string and return
                # .join in python and a for loop 
        
        
        ans = [['#',0]]
        for char in s:
            if ans[-1][0] == char:
                ans[-1][1] += 1
                if ans[-1][1] == k:
                    ans.pop()
            else:
                ans.append([char,1])
        
        string = ''
        for i in range(len(ans)):
            string += ans[i][0] * ans[i][1]
        return string