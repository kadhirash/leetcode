class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort() # time O(nlogn)
        array_len = len(products)
        ans = []
        input_char = ""

        for chr in searchWord:
            tmp = []
            input_char += chr
            insertion_index = self.binary_search(products, input_char) # find where input_char can be inserted in-order in the products array
            for word_ind in range(insertion_index, min(array_len, insertion_index+3)): # check the following 3 words, if valid
                if products[word_ind].startswith(input_char):
                    tmp.append(products[word_ind])
            ans.append(tmp)
        return ans

    def binary_search(self, array, target): # bisect.bisect_left implementation
        lo = 0
        hi = len(array)

        while lo < hi:
            mid = (lo + hi) //2
            if array[mid] < target: lo = mid + 1
            else: hi = mid
        return lo
        